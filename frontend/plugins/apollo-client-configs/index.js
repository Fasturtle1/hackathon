import { HttpLink } from 'apollo-link-http'
import { from } from 'apollo-link'
import { BatchHttpLink } from 'apollo-link-batch-http'
import { InMemoryCache } from 'apollo-cache-inmemory'
import { errorLink as errorHandler } from './error-handler'
import { middleware } from './middleware'

export default ctx => {
  const { ssrMiddleware, csrfMiddleware, userStatusMiddleware } = middleware(
    ctx
  )
  const errorLink = errorHandler(ctx)
  const production = process.env.NODE_ENV === 'production'

  // Настраиваем соединение в зависимости от среды
  const opts = {
    // Для разработки необходимо указывать credentials: include так как порты серверов разные
    credentials: production ? 'same-origin' : 'include',
    // Для разработки используем локальный сервер на другом порту
    uri: production ? '/api_v1' : 'http://localhost:8000/api_v1'
  }

  /*
   ** Для продакшена используем накопление запросов в один (batching) с макс. интервалом ожидания 50 мс
   ** https://www.apollographql.com/docs/link/links/batch-http.html
   */
  if (production) {
    opts.batchInterval = 50
  }

  const httpLink = production ? new BatchHttpLink(opts) : new HttpLink(opts)

  // Оптимизация из доков Vue для SSR
  const cache = new InMemoryCache()
  if (process.client) {
    if (typeof window !== 'undefined') {
      const state = window.__APOLLO_STATE__
      if (state) {
        cache.restore(state.defaultClient)
      }
    }
  }

  const link = errorLink.concat(
    from([csrfMiddleware, ssrMiddleware, userStatusMiddleware, httpLink])
  )

  // Create the apollo client
  return {
    link,
    cache,
    // Set this on the server to optimize queries when SSR or temporary disable query force-fetching
    ...(process.server ? { ssrMode: true } : { ssrForceFetchDelay: 100 })
  }
}

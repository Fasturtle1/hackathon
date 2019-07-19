import { generateUid } from '@/utils'
export const state = () => ({
  errors: []
})

export const mutations = {
  pushError({ errors }, error) {
    errors.push(error)
  },
  shiftError: ({ errors }) => errors.shift(),
  hideError({ errors }, id) {
    const error = errors.find(e => e.id === id)
    if (error) {
      error.show = false
    }
  }
}

export const getters = {
  errorsGetter: ({ errors }) => errors
}

export const actions = {
  pushError(ctx, error) {
    const id = generateUid()
    ctx.commit('pushError', { id, text: error, show: true })
    setTimeout(() => {
      ctx.commit('hideError', id)
    }, 5000)
  },
  async nuxtServerInit({ dispatch }, ctx) {
    const isLoggedIn = ctx.app.$cookies.get('isLoggedIn')
    if (isLoggedIn) {
      await dispatch('auth/getCurrentUser')
    }
  }
}

<template>
  <div>
    <div v-for="user in allUsers" :key="user.id">
      {{ user.firstName }} {{ user.lastName }} {{ user.login }}
    </div>
    <v-btn @click="refetch()">TEST</v-btn>
  </div>
</template>

<script>
import gql from 'graphql-tag'

export default {
  name: 'Test',
  data() {
    return {
      allUsers: null
    }
  },
  apollo: {
    allUsers: {
      query: gql`
        {
          allUsers {
            id
            firstName
            lastName
            login
          }
        }
      `,
      update(data) {
        return data.allUsers
      }
    }
  },
  methods: {
    refetch() {
      this.allUsers = []
      this.$apollo.queries.allUsers.refetch()
    }
  }
}
</script>

<style scoped></style>

<template>
  <div>
    <!-- <notifications
      group="commonNotification"
      :max="1"
      position="top right"
      width="450px"
    /> -->
    <v-btn @click="test">TEST</v-btn>
    <!-- <div v-for="(user, index) in allUsers" :key="index">
      {{ user.firstName }}
    </div> -->
    <v-btn @click="notif">TEST2</v-btn>
  </div>
</template>

<script>
import { allUsers } from '~/graphql/users/queries'

export default {
  data() {
    return {
      allUsers: []
    }
  },
  apollo: {
    allUsers: {
      query: allUsers,
      update(data) {
        return data.allUsers
      },
      prefetch: false
    }
  },
  mounted() {},
  methods: {
    test() {
      this.$apollo
        .query({
          query: allUsers,
          fetchPolicy: 'no-cache'
        })
        .then(({ data }) => {
          this.allUsers = data.allUsers
        })
    },
    notif() {}
  }
}
</script>

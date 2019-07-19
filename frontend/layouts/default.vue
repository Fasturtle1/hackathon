<template>
  <v-app id="inspire">
    <alarms />
    <v-navigation-drawer v-model="drawer" fixed app>
      <v-list dense>
        <v-list-item to="/">
          <v-list-item-action>
            <v-icon>home</v-icon>
          </v-list-item-action>
          <v-list-item-content>
            <v-list-item-title>Home</v-list-item-title>
          </v-list-item-content>
        </v-list-item>
        <v-list-item to="/inspire">
          <v-list-item-action>
            <v-icon>contact_mail</v-icon>
          </v-list-item-action>
          <v-list-item-content>
            <v-list-item-title>Contact</v-list-item-title>
          </v-list-item-content>
        </v-list-item>
      </v-list>
    </v-navigation-drawer>
    <v-app-bar color="indigo" dark fixed app>
      <v-app-bar-nav-icon @click.stop="drawer = !drawer"></v-app-bar-nav-icon>
      <v-toolbar-title>Application</v-toolbar-title>
      <v-spacer />
      <notifications />
      <v-icon v-if="$$user.loggedIn" @click="logout">logout</v-icon>
    </v-app-bar>
    <v-content>
      <v-container fluid>
        <nuxt />
      </v-container>
    </v-content>
    <v-footer color="indigo" app>
      <span class="white--text">&copy; 2017</span>
    </v-footer>
  </v-app>
</template>

<script>
import Alarms from '@/components/common/Alarms'
import Notifications from '@/components/notifications/Notifications'

export default {
  components: { Alarms, Notifications },
  props: {
    source: {
      type: String,
      default: ''
    }
  },
  data: () => ({
    drawer: false
  }),
  methods: {
    logout() {
      this.$$auth.logout()
      // this.$store.commit('auth/logout')
    }
  }
}
</script>

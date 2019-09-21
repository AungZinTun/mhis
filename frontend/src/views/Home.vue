<template>
  <div class="home">
    <div class="container mt-2">
      <!-- {{notify}} -->
    {{notify}}
          <li v-for="noti in notify" v-bind:key="noti.id">
           {{ noti.name }}
          </li>

      <div class="my-4">
        <p v-show="LoadingNotify">...loading...</p>
        <button
          v-show="next"
          @click="getnotify"
          class="btn btn-sm btn-outline-success"
          >Load More
        </button>
      </div>
    </div>
  </div>
</template>

<script>
import { apiService } from "@/common/api.service.js";
export default {
  name: "home",
  data() {
    return {
      notify: [],
      next: null,
      LoadingNotify: false
    }
  },
  methods: {
    getNotifies() {
      // make a GET Request to the notifys list endpoint and populate the notifys array
      let endpoint = "/api";
      if (this.next) {
        endpoint = this.next;
      }
      this.LoadingNotify = true;
      apiService(endpoint)
        .then(data => {
          this.notify.push(...data.results)
          this.LoadingNotify = false;

          if (data.next) {
            this.next = data.next;
          } else {
            this.next = null;
          }
        })
    }
  },
  created() {
    this.getNotifies()
    document.title = "Notify Register";
    // console.log(this.notify);
  }
};
</script>

<style scoped>
.notify-author {
  font-weight: bold;
  color: #DC3545;
}

.notify-link {
  font-weight: bold;
  color: black;
}

.notify-link:hover {
  color: #343A40;
  text-decoration: none;
}
</style>

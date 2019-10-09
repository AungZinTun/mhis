<template>
  <div class="home">
    <div class="container mt-2">
      <!-- {{notify}} -->
      <!-- {{notify}} -->
      <table class="table table-striped">
        <thead>
          <tr>
            <th scope="col">name</th>
            <th scope="col">phone</th>
            <th scope="col">age</th>
            <th scope="col">sex</th>
            <th scope="col">township</th>
            <th scope="col">specimen_collected_date</th>
          </tr>
        </thead>
        <tbody>
          <tr v-for="noti in notify" v-bind:key="noti.id">
            <td>{{ noti.name }}</td>
            <td>{{noti.phone}}</td>
            <td>{{noti.age}}</td>
            <td>{{noti.sex}}</td>
            <td>{{noti.township}}</td>
            <td>{{noti.specimen_collected_date}}</td>
          </tr>
        </tbody>
      </table>

      <div class="my-4">
        <p v-show="LoadingNotify">...loading...</p>
        <button v-show="next" @click="getNotifies" class="btn btn-sm btn-outline-success">Load More</button>
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
    };
  },
  methods: {
    getNotifies() {
      // make a GET Request to the notifys list endpoint and populate the notifys array
      let endpoint = "/api";
      if (this.next) {
        endpoint = this.next;
      }
      this.LoadingNotify = true;
      apiService(endpoint).then(data => {
        this.notify.push(...data.results);
        this.LoadingNotify = false;

        if (data.next) {
          this.next = data.next;
        } else {
          this.next = null;
        }
      });
    }
  },
  created() {
    this.getNotifies();
    document.title = "Notify Register";
    console.log(this.notify);
  }
};
</script>

<style scoped>
.notify-author {
  font-weight: bold;
  color: #dc3545;
}

.notify-link {
  font-weight: bold;
  color: black;
}

.notify-link:hover {
  color: #343a40;
  text-decoration: none;
}
</style>

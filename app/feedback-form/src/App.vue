<template>
  <div class="full-screen bg-light">
    <feedback-form-popup v-if="showFormPopup" @close-popup="closePopup"></feedback-form-popup>
    <div class="d-flex flex-column w-100 h-100 justify-content-center align-items-center" v-else>
      <button @click="showFormPopup = true" class="btn btn-primary">Fill Feedback Form</button>
      <table class="table table-striped mt-4 w-75 shadow">
        <thead>
          <tr>
            <th scope="col">No</th>
            <th scope="col">Rating</th>
            <th scope="col">Created At</th>
          </tr>
        </thead>
        <tbody>
          <tr v-for="feedback in feedbacks" :key="feedback.id">
            <th scope="row">{{ feedback.id }}</th>
            <td>{{ feedback.rating }}</td>
            <td>{{ feedback.date_created }}</td>
          </tr>
        </tbody>
      </table>
      <h2 v-if="feedbacks.length == 0" class="text-center">No Data Found</h2>
    </div>
  </div>
</template>

<script>
import FeedbackFormPopup from './components/FeedbackFormPopup.vue';

export default {
  components: { FeedbackFormPopup },
  data () {
    return {
        showFormPopup: false,
        feedbacks: []
      }
  },
  methods: {
    getFeedbackData() {
      this.$http.get("http://127.0.0.1:8000/feedbacks")
        .then(response => {
          console.log(response.body);
          this.feedbacks = response.body
        })
    },
    closePopup() {
      this.showFormPopup = false
      this.getFeedbackData()
    }
  },
  mounted() {
    this.getFeedbackData()
  }
}
</script>

<style>
  .full-screen {
    height: 100vh;
    width: 100%;
  }
</style>

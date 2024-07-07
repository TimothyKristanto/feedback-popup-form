<template>
  <div class="full-screen bg-light">
    <feedback-form-popup v-if="showFormPopup" @close-popup="closePopup"></feedback-form-popup>
    <div class="d-flex flex-column w-100 h-100 align-items-center" v-else>
      <button @click="showFormPopup = true" class="btn btn-primary mt-5">Fill Feedback Form</button>
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
  components: { FeedbackFormPopup }, // use the FeedbackFormPopup as component in this page
  data () {
    return {
        showFormPopup: false, // to define whether we enable the popup form or not
        feedbacks: [] // to define the feedbacks data which will be shown inside the table
      }
  },
  methods: {
    // get all the feedback data from the API
    getFeedbackData() {
      this.$http.get("http://127.0.0.1:8000/feedbacks") // call the API with get method
        .then(response => {
          console.log(response.body);
          this.feedbacks = response.body // put the feedback data inside feedbacks variable
        })
    },
    // close the popup and update the feedback data
    closePopup() {
      this.showFormPopup = false // close the popup
      this.getFeedbackData() // update the feedback data
    }
  },
  mounted() {
    this.getFeedbackData() // get all the feedback data on app mounted
  }
}
</script>

<style>
  .full-screen {
    height: 100vh;
    width: 100%;
  }
</style>

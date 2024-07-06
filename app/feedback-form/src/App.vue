<template>
  <div class="full-screen bg-light">
    <feedback-form-popup v-if="showFormPopup" @close-popup="showFormPopup = false"></feedback-form-popup>
    <div class="d-flex w-100 h-100 justify-content-center align-items-center" v-else>
      <button @click="showFormPopup = true" class="btn btn-primary">Fill Feedback Form</button>
      <!-- show data from database inside table here -->
    </div>
  </div>
</template>

<script>
import FeedbackFormPopup from './components/FeedbackFormPopup.vue';

export default {
  components: { FeedbackFormPopup },
  data () {
    return {
        showFormPopup: false
      }
  },
  methods: {
    
  }
}
</script>

<style>
  .full-screen {
    height: 100vh;
    width: 100%;
  }
</style>

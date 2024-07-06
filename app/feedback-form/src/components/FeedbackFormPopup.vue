<template>
    <div class="full-screen d-flex justify-content-center align-items-center bg-light">
      <div class="bg-white w-50 h-50 p-4 rounded-corner-lg d-flex align-items-center shadow flex-column">
        <b-progress :value="progress" :max="max" class="mb-3 w-100 progress"></b-progress>
        <div v-if="progress == 1" class="mh-100">
          <h2 class="font-weight-bold"> {{ question }} </h2>
          <div class="d-flex flex-row mt-4">
            <div v-for="star in stars" :key="star.id" class="d-flex flex-column mx-4 align-items-center w-75">
              <img @click="changeRating(star.id)" @mouseover="changeStarImage(star.id)" @mouseleave="changeStarImage(0)" :src="getImageByDirectory(star.image)" alt="" class="star">
              <h5>{{ star.id }}</h5>
              <h6 v-if="star.id == 1" class="text-center">Very dissatisfied</h6>
              <h6 v-else-if="star.id == 5" class="text-center">Very satisfied</h6>
            </div>
          </div>
        </div>
        <div v-else-if="progress == 2" class="d-flex w-100 h-75 justify-content-center align-items-center">
          <h1>Thank you for filling the survey</h1>
        </div>
        
        <button v-if="progress == 1 && rating != 0" class="btn btn-primary w-25 mt-4" @click="submitFeedback">Submit</button>
        <button v-if="progress == 2" class="btn btn-primary w-25" @click="closePopup">Close</button>
      </div>
    </div>
  </template>
  
  <script>
  export default {
    data () {
      return {
        question: "How would you rate your satisfaction with our product?",
        progress: 1,
        max: 2,
        rating: 0,
        stars: [
          {"id":1, "image": "star.svg"},
          {"id":2, "image": "star.svg"},
          {"id":3, "image": "star.svg"},
          {"id":4, "image": "star.svg"},
          {"id":5, "image": "star.svg"}
        ],
      }
    },
    methods: {
      changeRating(rate) {
        this.rating = rate
        this.changeStarImage(rate)
      },
      changeStarImage(hoveredStarId) {
        this.stars.forEach(star => {
          if (star.id <= hoveredStarId) {
            star.image = "star-fill.svg"
          } else {
            if (star.id > this.rating) {
              star.image = "star.svg"
            }
          }
        });
      },
      getImageByDirectory(dir) {
        return require("../assets/" + dir)
      },
      closePopup() {
        this.$emit("close-popup")
      },
      submitFeedback() {
        this.$http.post("http://127.0.0.1:8000/feedbacks", {"rating": this.rating})
        .then(response => {
          console.log(response)
          this.progress = 2
        })
      }
    }
  }
  </script>
  
  <style>
  .full-screen {
    height: 100vh;
    width: 100%;
  }
  
  .rounded-corner-lg {
    border-radius: 20px;
  }
  
  .star{
    width: 50px !important;
    height: 50px !important;
    cursor: pointer;
  }
  </style>
  
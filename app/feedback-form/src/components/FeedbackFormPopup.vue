<template>
  <div
    class="full-screen d-flex justify-content-center align-items-center bg-light"
  >
    <div
      class="bg-white w-50 h-50 p-4 rounded-corner-lg d-flex align-items-center shadow flex-column"
    >
      <b-progress
        :value="progress"
        :max="max"
        class="mb-3 w-100 progress"
      ></b-progress>
      <div v-if="progress != 6" class="mh-100">
        <h2 class="font-weight-bold">{{ progress }}. {{ question }}</h2>
        <div class="d-flex flex-row mt-4">
          <div
            v-for="star in stars"
            :key="star.id"
            class="d-flex flex-column mx-4 align-items-center w-75"
          >
            <img
              @click="changeRating(star.id)"
              @mouseover="changeStarImage(star.id)"
              @mouseleave="changeStarImage(0)"
              :src="getImageByDirectory(star.image)"
              alt=""
              class="star"
            />
            <h5>{{ star.id }}</h5>
            <h6 v-if="star.id == 1" class="text-center">Very dissatisfied</h6>
            <h6 v-else-if="star.id == 5" class="text-center">Very satisfied</h6>
          </div>
        </div>
      </div>
      <div
        v-else-if="progress == 6"
        class="d-flex w-100 h-75 justify-content-center align-items-center"
      >
        <h1>Thank you for filling the survey</h1>
      </div>

      <div class="d-flex flex-row mt-4 w-100 justify-content-center">
        <button
          v-if="progress != 6 && progress != 1"
          class="btn btn-danger w-25 me-5"
          @click="navigateBack"
        >
          Back
        </button>

        <button
          v-if="progress != 6 && rating != 0"
          class="btn btn-primary w-25"
          @click="submitFeedback"
        >
          Next
        </button>
      </div>

      <button
        v-if="progress == 6"
        class="btn btn-primary w-25"
        @click="closePopup"
      >
        Close
      </button>
    </div>
  </div>
</template>

<script>
export default {
  data() {
    return {
      question: "How would you rate your satisfaction with our product?", // represents the question inside the feedback form progress
      progress: 1, // represents the current feedback form progress
      max: 6, // represents the max feedback form progress
      rating: 0, // represents the rating from the user
      progressFinished: false,
      stars: [
        // represents the star images in the feedback form, each star has an id
        { id: 1, image: "star.svg" },
        { id: 2, image: "star.svg" },
        { id: 3, image: "star.svg" },
        { id: 4, image: "star.svg" },
        { id: 5, image: "star.svg" },
      ],
    };
  },
  created() {
    this.getFeedbackByProgress();
  },
  methods: {
    getFeedbackByProgress() {
      this.$http
        .get("http://127.0.0.1:8000/feedbacks/" + this.progress) // call the API with get method
        .then((response) => {
          console.log(response.body);
          if (response.body.length !== 0) {
            this.changeRating(response.body[0].rating); // put the feedback data inside feedbacks variable
            this.progressFinished = true;
          } else {
            this.changeRating(0); // put the feedback data inside feedbacks variable
            this.progressFinished = false;
          }
        });
    },
    navigateBack() {
      this.progress -= 1;
      this.getFeedbackByProgress();
    },
    // to change the rating when one of the star buttons pressed
    changeRating(rate) {
      this.rating = rate; // change the rating based on the rate value
      this.changeStarImage(rate); // change the star images
    },
    changeStarImage(hoveredStarId) {
      this.stars.forEach((star) => {
        if (star.id <= hoveredStarId) {
          // change the star image to star-fill.svg if the star id is lower or equal to the hovered or clicked star id
          // because we only want to block all the the star images which star id is lower or equal to the hovered or clicked star id
          star.image = "star-fill.svg";
        } else {
          if (star.id > this.rating) {
            // we do not want to block the star images if their star id is lower or equal to the hovered or clicked star id
            // thus we change the star image to star.svg
            star.image = "star.svg";
          }
        }
      });
    },
    // get an image based on a certain directory
    getImageByDirectory(dir) {
      return require("../assets/" + dir); // return the image acquired from the specified directory
    },
    // call parent closePopup function
    closePopup() {
      this.$emit("close-popup");
    },
    // call the api to submit the feedback
    submitFeedback() {
      if (this.progressFinished) {
        this.progress += 1;
        this.progressFinished = false;
        this.getFeedbackByProgress();
      } else {
        this.$http
          .post("http://127.0.0.1:8000/feedbacks", {
            id: this.progress,
            rating: this.rating,
          }) // call the API with post method
          .then((response) => {
            console.log(response);
            this.changeRating(0);
            this.progress += 1; // change the feedback form progress to 2 to indicate that the user has already finished filling the form
          });
      }
    },
  },
};
</script>

<style>
.full-screen {
  height: 100vh;
  width: 100%;
}

.rounded-corner-lg {
  border-radius: 20px;
}

.star {
  width: 50px !important;
  height: 50px !important;
  cursor: pointer;
}
</style>

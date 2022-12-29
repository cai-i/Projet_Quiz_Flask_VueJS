<template>
  <h1>Home page</h1>
  <!-- <div v-for="scoreEntry in registeredScores">
    {{ scoreEntry.playerName }} - {{ scoreEntry.score }}
  </div> -->
</template>

<script>
import quizApiService from "@/services/QuizApiService";

export default {
  name: "HomePage",
  data() {
    return {
      registeredScores : [],
    };
  },
  async created() {
    // console.log(quizApiService.getQuizInfo())
    // var quizInfoPromise = quizApiService.getQuizInfo();
    // var quizInfoApiResult = await quizInfoPromise;
    // this.registeredScores = quizInfoApiResult.data.scores;
		// console.log("Composant Home page 'created'");
  }
};
</script>
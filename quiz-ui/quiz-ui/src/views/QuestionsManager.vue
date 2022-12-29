<template>
  <header>

  <h1>QuizPage</h1>

  </header>

{{this.playerName}}

</template>

<script>
import quizApiService from "@/services/QuizApiService";
import participationStorageService from "@/services/ParticipationStorageService";

export default {
  name: "QuestionsPage",
  data() {
    return {
      registeredQuestions : [],
      playerName : ""
    };
  },
  mounted() {
      console.log("name:", participationStorageService.getPlayerName());
      this.playerName = participationStorageService.getPlayerName()
  }
};
</script>
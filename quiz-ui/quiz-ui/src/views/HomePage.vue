<template>
<div class="text-center">

  <h1 class="pt-12 pb-6">Home page</h1>

  <div class="p-6" v-if="myName" >
  Mon propre score : 
  {{myScoreString}}
  </div>

  <div v-for="scoreEntry in registeredScores">
    {{ scoreEntry.playerName }} - {{ scoreEntry.score }}
  </div>

</div>
</template>

<script>
import quizApiService from "@/services/QuizApiService";
import participationStorageService from "@/services/ParticipationStorageService";

export default {
  name: "HomePage",
  data() {
    return {
      nyName : null,
      myScoreString : null,
      registeredScores : []
    };
  },
  async created() {
    console.log(quizApiService.getQuizInfo());
    var quizInfoPromise = quizApiService.getQuizInfo();
    var quizInfoApiResult = await quizInfoPromise;
    this.registeredScores = quizInfoApiResult.data.scores;
		console.log("Composant Home page 'created'");
    this.myOwnScore();
    participationStorageService.clear();
  },
  methods:{
    myOwnScore() {
      console.log("get my own score");
      this.myName =  participationStorageService.getPlayerName();
      this.myScoreString = this.myName + " - " + participationStorageService.getParticipationScore();
    }
  }
};
</script>
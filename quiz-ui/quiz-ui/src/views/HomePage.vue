<template>
  <h1>Home page</h1>


  <div v-if="myName" >
<br>
  Mon propre score : 
  {{myScoreString}}
  </div>
<br>

  <div v-for="scoreEntry in registeredScores">
    {{ scoreEntry.playerName }} - {{ scoreEntry.score }}
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
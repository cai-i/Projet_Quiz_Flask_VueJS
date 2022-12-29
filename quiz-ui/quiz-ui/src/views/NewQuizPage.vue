<template>
  <header>

  <h1>NewQuizPage</h1>

  <form id="username" action="" method="post">
    <label for="name">Saisissez votre nom : </label>
    <input type="text" id="name" v-model="username" />
    <button type="submit" @click="launchNewQuiz">GO!</button>
  </form>

  </header>
</template>




<script>
import participationStorageService from "@/services/ParticipationStorageService";

export default {
  name: "NewQuizPage",
  data() { 
    return {
      username:null
    };  
  },
  methods:{
    launchNewQuiz(){
      console.log("Launch new quiz with", this.username);
      participationStorageService.savePlayerName(this.username);
      this.$router.push('/questions');
    }
  }
}
</script>



<style scoped>

  #username label, input {
    display: block;
    margin: 8px 0px;
  }

</style>
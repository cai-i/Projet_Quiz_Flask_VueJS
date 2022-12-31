<template>
<div :style="myStyle">

  <h1 class="py-8 px-8 text-xl font-bold text-red-800">NewQuizPage</h1>

  <div class="mt-16 grid gap-4 place-content-center">
  <form class="shadow-md border rounded px-8 py-8 mb-4 bg-white bg-opacity-50" id="username" action="" method="post">
    <label class="block text-rose-700 text-sm font-bold mb-2" for="name">
      Saisissez votre nom : 
    </label>
    <input class="shadow appearance-none border border-red-500 rounded w-full py-2 px-3 text-gray-700 mb-3 leading-tight focus:outline-none focus:shadow-outline" type="text" id="name" v-model="username" />
    <button class="bg-rose-700 hover:bg-rose-900 text-white font-bold w-full py-2 px-3 rounded focus:outline-none focus:shadow-outline" type="submit" @click="launchNewQuiz">GO!</button>
  </form>
  </div>

</div>
</template>



<script>
import participationStorageService from "@/services/ParticipationStorageService";

export default {
  name: "NewQuizPage",
  data() { 
    return {
      username:null,
      myStyle: { 
        textAlign: "center",
        paddingBottom:"20em",
        backgroundSize: "100% auto",
        backgroundImage: "url(https://images4.alphacoders.com/146/thumb-1920-146664.jpg)" 
      }
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


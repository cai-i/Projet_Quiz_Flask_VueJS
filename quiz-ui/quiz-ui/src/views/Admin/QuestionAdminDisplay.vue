<template>
  <div class="px-12 mb-2">
    <div class="border rounded px-6 py-4 mt-4 mb-6 bg-white bg-opacity-40">

      <!-- Des classes tailwind grid et col-span ont été utilisés pour aligner les textes et inputs -->
      <div class="mt-3">
        <p class="grid grid-cols-8 gap-4">
          <p class="col-span-1 pt-2 font-semibold">Thème: </p>
          <p class="col-span-7"><input class="shadow appearance-none border focus:border-pink-700 rounded h-10 w-full px-3 py-2 text-gray-700 mb-3 leading-tight focus:outline-none focus:shadow-outline" type="text" v-model="this.question.questionTitle" placeholder="titre de la question"></p>
        </p>
      </div>

      <div class="mt-3">
        <p class="grid grid-cols-8 gap-4">
          <p class="col-span-1 pt-2 font-semibold">Question: </p>
          <p class="col-span-7"><input class="shadow appearance-none border focus:border-pink-700 rounded w-full h-10 px-3 py-2 text-gray-700 mb-3 leading-tight focus:outline-none focus:shadow-outline" type="text" v-model="this.question.questionText" placeholder="texte de la question"></p>
        </p>
      </div>
    </div>
    
    <!-- Suppression d'un possibleAnswer par le svg trash can --> 
    <div v-for="(answer, index) in this.question.possibleAnswers">
      <div class="flex gap-2">
        <input class="mb-2" type="radio" name="answer" v-model="correctAnswerPosition" :value="index" />
        <input class="shadow appearance-none border focus:border-pink-700 rounded w-full px-3 py-2 text-gray-700 mb-3 leading-tight focus:outline-none focus:shadow-outline" type="text" v-model="answer.text" placeholder="Réponse">
        <button @click="removePossibleAnswer(index)">
          <svg class="w-6 h-6 mb-2 hover:fill-orange-200" fill="none" stroke="DarkRed" viewBox="0 0 24 24" xmlns="http://www.w3.org/2000/svg"><path stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="M19 7l-.867 12.142A2 2 0 0116.138 21H7.862a2 2 0 01-1.995-1.858L5 7m5 4v6m4-6v6m1-10V4a1 1 0 00-1-1h-4a1 1 0 00-1 1v3M4 7h16"></path></svg>
        </button>
      </div>
    </div>

    <!-- Ajout d'un possibleAnswer par le svg + -->
    <button @click="addPossibleAnswers">
      <svg class="w-6 h-6 mt-2 hover:fill-orange-200" fill="none" stroke="DarkRed" viewBox="0 0 24 24" xmlns="http://www.w3.org/2000/svg"><path stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="M12 9v3m0 0v3m0-3h3m-3 0H9m12 0a9 9 0 11-18 0 9 9 0 0118 0z"></path></svg>
    </button>
    <!-- Gestion de position directement dans un input, peut être améliorée pour plus d'ergonomie -->
    <div>
      Position de la question : <input class="w-16 mt-2 shadow appearance-none border focus:border-pink-700 rounded px-3 py-2 text-gray-700 mb-3 leading-tight focus:outline-none focus:shadow-outline" type="number" min=1 v-model="this.question.position" />
    </div>

    <!-- Gestion d'image avec un background par défaut si this.question.questionImage est null -->
    <div class="max-w-md max-h-fit mt-4 mb-2 ">
      <div class="bg-orange-100 shadow grid grid-cols-10">
        <div class="col-span-2"> 
          <div v-if="this.question.questionImage">
            <img
              v-if="this.question.questionImage"
              class ="w-32 h-20"
              :src="this.question.questionImage"
            />
          </div>
          <div v-else>
            <p class="bg-slate-200 w-22 h-20"></p>
          </div>
        </div>
        <div class="col-span-8 mt-6 px-4">
          <ImageUpload @file-change="imageFileChangedHandler" />
        </div>
      </div>
    </div>

    <!-- Sauvegarde de la question -->
    <div class="grid grid-cols-8 mt-6">
      <div class="col-span-7"></div> 
      <button @click="saveQuestion" class="col-span-1 w-32 bg-rose-700 hover:bg-rose-900 text-white font-bold py-2 px-2 rounded focus:outline-none focus:shadow-outline" type="button">
        Sauvegarder
      </button>
    </div>
  </div>
  
</template>

<script>
import quizApiService from "@/services/QuizApiService";
import ImageUpload from "@/services/ImageUpload.vue";

export default {
  components: {
    ImageUpload,
  },
  name: "QuestionDisplay",
  props: {
    question: {
      type: Object,
    },
  },
  data() {
    return {
      correctAnswerPosition: null
    };
  },
  async created() {
    for (let i = 0 ; i < this.question.possibleAnswers.length; i++){
      if (this.question.possibleAnswers[i].isCorrect){
        this.correctAnswerPosition = i;
      }
    }

  },
  methods:{
    imageFileChangedHandler(b64String) {
      this.question.questionImage = b64String;
    },
    addPossibleAnswers() {
      this.question.possibleAnswers.push({"text": "", "isCorrect": false});
    },

    // Le second param de splice permet de spécifier le nombre d'élément à supprimer à partir de index, un dans notre cas
    removePossibleAnswer(index) {
      this.question.possibleAnswers.splice(index, 1);
    },

    // Ce fichier est utilisé pour la création et la modification, la détection se fait au niveau de l'id
    async saveQuestion(){
      for (let i = 0 ; i < this.question.possibleAnswers.length; i++){
          this.question.possibleAnswers[i].isCorrect = (i != this.correctAnswerPosition) ? false : true;
      }

      if(this.question.id == null){
        var postQuestionPromise = quizApiService.postQuestion(this.question);
        await postQuestionPromise;
      }
      else{
        var putQuestionPromise = quizApiService.putQuestion(this.question);
        await putQuestionPromise;
      }

      // Refresh la page
      location.reload();
    }
  }
};
</script>

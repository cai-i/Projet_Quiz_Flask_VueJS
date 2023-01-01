<template>
  <div
    class="shadow-md border rounded px-12 pb-8 bg-white bg-opacity-60"
  >
    <div class="border rounded px-6 py-4 mt-8 mb-6 bg-white bg-opacity-40">
      <div class="mt-3 font-bold">
        <p class="grid grid-cols-10 font-bold gap-4">
          <p class="col-span-1 pt-2">Thème: </p>
          <p class="col-span-9"><input class="shadow appearance-none border focus:border-pink-700 rounded w-full px-3 py-2 text-gray-700 mb-3 leading-tight focus:outline-none focus:shadow-outline" type="text" v-model="this.question.questionTitle" placeholder="titre de la question"></p>
        </p>
      </div>

      <div class="mt-3 font-bold">
        <p class="grid grid-cols-10 font-bold gap-4">
          <p class="col-span-1 pt-2">Question: </p>
          <p class="col-span-9"><input class="shadow appearance-none border focus:border-pink-700 rounded w-full px-3 py-2 text-gray-700 mb-3 leading-tight focus:outline-none focus:shadow-outline" type="text" v-model="this.question.questionText" placeholder="texte de la question"></p>
        </p>
      </div>
    </div>

    <div
      v-for="answer in this.question.possibleAnswers"
    >
      <input class="shadow appearance-none border focus:border-pink-700 rounded w-full px-3 py-2 text-gray-700 mb-3 leading-tight focus:outline-none focus:shadow-outline" type="text" v-model="answer.text" placeholder="Réponse">
    </div>

    <div class="max-w-md max-h-fit mt-6 m-auto mb- ">
      
      <div class="mb-4">
        <ImageUpload @file-change="imageFileChangedHandler" />
      </div>
      <img
        v-if="this.question.questionImage"
        :src="this.question.questionImage"
      />
    </div>
    <div class="grid grid-cols-10">
      <div class="col-span-9"></div> 
      <button @click="save" class="col-span-1 bg-rose-700 hover:bg-rose-900 text-white font-bold py-2 px-2 rounded focus:outline-none focus:shadow-outline" type="button">
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
      picked: true,
      myTextStrokeRule: {
        textShadow:
          "0 3px 3px white, 0 -3px 3px white, 3px 0 3px white, -3px 0 3px white",
        webkitTextStroke: "0.1px",
        webkitTextStrokeColor: "white",
      },
    };
  },
  methods:{
    imageFileChangedHandler(b64String) {
      this.image = b64String;
    },

    async save(){
      console.log(this.question);
      var putQuestionPromise = quizApiService.putQuestion(this.question);
      var putQuestionApiResult = await putQuestionPromise;
      console.log(putQuestionApiResult);
    }
  }
};
</script>

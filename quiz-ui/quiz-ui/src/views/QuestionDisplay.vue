<template>
<div class="text-center shadow-md border rounded px-8 pb-8 bg-white bg-opacity-50">

  <div class="mt-6 grid place-content-center">
    {{this.question.questionTitle}}
  </div>

  <div class="block text-rose-700 text-sm font-bold mb-8 ">
    {{this.question.questionText}}
  </div>

  <div class="bg-white bg-opacity-50 m-2 p-2 shadow-md border rounded " v-for="answer in this.question.possibleAnswers" >
    <a @click="$emit('click-on-answer', answer.isCorrect)">{{answer.text}}</a>
  </div>

  <div class="max-w-md max-h-fit mt-6 m-auto">
    <img v-if="this.question.questionImage" :src="this.question.questionImage" />
  </div>
  
</div>
</template>

<script>
import participationStorageService from "@/services/ParticipationStorageService";

export default {
  name: "QuestionDisplay",
  props: {
    question: {
      type: Object
    }
  },
  emits: ["click-on-answer"]
};
</script>
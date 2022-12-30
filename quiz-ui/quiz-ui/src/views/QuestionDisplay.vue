<template>

  

  <img v-if="this.question.questionImage" :src="questionImage" />
  
{{this.question.questionTitle}}

{{this.question.questionText}}

  <div v-for="answer in this.question.possibleAnswers" >
    <a @click="$emit('click-on-answer', answer.isCorrect)">{{answer.text}}</a>
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
<template>

  
  <!--div v-for="answer in question.possibleAnswers": key="answer.id">
    <a @click="$emit('click-on-answer', 2)">{{answer}}</a>
  </div-->

  <img v-if="questionImage" :src="questionImage" />
  

  {{this.type}}
  <br>

  {{this}}
  {{this.question}}
  {{this.questionText+"1"}}
  {{this.questionTitle}}


  <button>
    <a @click="$emit('click-on-answer', 2)">answer1</a>
  </button>

prout
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
  emits: ["click-on-answer"],
  data() {
    return{
      question:{
        questionText:this.questionText,
        questionTitle:this.questionTitle
      }
    };
  }
};
</script>
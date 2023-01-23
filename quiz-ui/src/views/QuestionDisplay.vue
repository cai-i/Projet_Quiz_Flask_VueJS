<template>
  <div
    class="mt-3 text-2xl font-bold grid place-content-center"
    :style="myTextStrokeRule"
  >
    - {{ this.question.questionTitle }} -
  </div>

    <img id="imgBox"
      class="w-1/3 h-auto m-6 mb-10 object-cover mx-auto"
      v-if="this.question.questionImage"
      :src="this.question.questionImage"
    />

 <div class="p-4 pb-8 border rounded bg-white bg-opacity-40 ">
    <div class="block text-rose-700 text-xl font-bold mb-6">
      {{ this.question.questionText }}
    </div>

    <ul>
      <li v-for="(answer,idx) in this.question.possibleAnswers" :key="idx">
        <button id="answerButtons"
          class="mx-auto w-4/5 bg-opacity-80 hover:bg-opacity-100 shadow-md border rounded block m-2 p-2 hover:font-semibold"
          @click="
            $emit(
              'click-on-answer',
              this.question.possibleAnswers.indexOf(answer) + 1
            )
          "
          :class="[idx+1 === selectedAnswer ? 'border-teal-700 border-2 bg-opacity-60 bg-teal-400' : 'bg-white']"
        >
          {{ answer.text }}
        </button>
        </li>
    </ul>
  </div>
</template>

<script>

export default {
  name: "QuestionDisplay",
  props: {
    question: {
      type: Object,
    },
    selectedAnswer:0
  },
  emits: ["click-on-answer"],
  data() {
    return {
      myTextStrokeRule: {
        textShadow:
          "0 3px 3px white, 0 -3px 3px white, 3px 0 3px white, -3px 0 3px white",
        webkitTextStroke: "0.1px",
        webkitTextStrokeColor: "white",
      },
    };
  },
};
</script>


<style scoped>
/* changer des parametres selon la taille de la fenetre */
@media (max-width: 550px) { 
  #imgBox{    
    width: 80%;
  }    
  #answerButtons{
    width: 100%;
  }
}
@media (min-width:550px) and (max-width: 768px) { 
  #imgBox{    
    width: 50%;
  }    
  #answerButtons{
    width: 90%;
  }
}
@media (min-width:768px) and (max-width: 1024px) { 
  #imgBox{    
    width: 50%;
  }    
}
</style>
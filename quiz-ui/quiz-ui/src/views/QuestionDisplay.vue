<template>

     <div
        class="mt-3 text-2xl font-bold grid place-content-center"
        :style="myTextStrokeRule"
      >
        - {{ this.question.questionTitle }} -
      </div>


    <div class="m-2 p-2">
      <img
        class="w-1/3 h-auto m-4 object-cover mx-auto"
        v-if="this.question.questionImage"
        :src="this.question.questionImage"
      />
    </div>

 <div class="p-4 border rounded px-2  bg-white bg-opacity-40 ">
    
    
      <div class="block text-rose-700 text-xl font-bold mb-3">
        {{ this.question.questionText }}
      </div>

    <button
      class="mx-auto bg-white bg-opacity-80 hover:bg-opacity-100 shadow-md border rounded block w-4/5 m-2 p-2 hover:font-bold"
      v-for="answer in this.question.possibleAnswers"
      @click="
        $emit(
          'click-on-answer',
          this.question.possibleAnswers.indexOf(answer) + 1
        )
      "
    >
      {{ answer.text }}
    </button>

    </div>

</template>

<script>

export default {
  name: "QuestionDisplay",
  props: {
    question: {
      type: Object,
    },
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

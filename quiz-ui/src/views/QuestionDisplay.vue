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

 <div class="p-4 pb-8 border rounded bg-white bg-opacity-40 ">
    <div class="block text-rose-700 text-xl font-bold mb-6">
      {{ this.question.questionText }}
    </div>

    <ul>
      <li v-for="(answer,idx) in this.question.possibleAnswers" :key="idx">
        <button
          class="mx-auto w-4/5 bg-opacity-80 hover:bg-opacity-100 shadow-md border rounded block m-2 p-2 hover:font-bold"
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

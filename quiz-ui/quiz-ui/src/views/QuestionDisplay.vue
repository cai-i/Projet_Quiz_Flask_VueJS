<template>
  <div
    class="text-center shadow-md border rounded px-8 pb-8 bg-white bg-opacity-60"
  >
    <div class="border rounded px-2 mt-8 mb-8 bg-white bg-opacity-40">
      <div
        class="mt-3 font-bold grid place-content-center"
        :style="myTextStrokeRule"
      >
        - {{ this.question.questionTitle }} -
      </div>

      <div class="block text-rose-700 text-xl font-bold mb-3">
        {{ this.question.questionText }}
      </div>
    </div>

    <button
      class="bg-white bg-opacity-80 hover:bg-opacity-100 m-2 p-2 shadow-md border rounded block w-full hover:font-bold"
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

    <div class="max-w-md max-h-fit mt-6 m-auto">
      <img
        v-if="this.question.questionImage"
        :src="this.question.questionImage"
      />
    </div>
  </div>
</template>

<script>
import participationStorageService from "@/services/ParticipationStorageService";

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

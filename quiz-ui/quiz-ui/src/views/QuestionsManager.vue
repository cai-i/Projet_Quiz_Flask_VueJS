<template>
  <div :style="myStyle">
    <h1
      class="py-8 px-8 text-2xl font-bold text-red-800"
      :style="myTextStrokeRule"
    >
      Notre quiz saura t-il vous mettre en PLS ?

      <div class="font-bold text-black text-lg" v-if="username">
        Joueur : {{ this.username }} ne semble pas encore foutu
      </div>
    </h1>


  <div
    class="ml-24 mr-24 p-8 text-center shadow-md border rounded px-8 bg-white bg-opacity-60"
  >

    <div
      class="p-2 font-bold text-xl text-yellow-700 border bg-white bg-opacity-50"
    >
      <button
          class="align-middle mr-4 p-2 rounded bg-white bg-opacity-40 hover:bg-opacity-30 hover:text-black"
          @click="
            if (this.currentQuestionPosition - 1 > 0) {
              this.currentQuestionPosition--;
              loadQuestionByPosition();
            }
          "
        >
   
      <svg xmlns="http://www.w3.org/2000/svg" fill="none" viewBox="0 0 24 24" stroke-width="1.5" stroke="currentColor" class="w-6 h-6">
        <path stroke-linecap="round" stroke-linejoin="round" d="M19.5 12h-15m0 0l6.75 6.75M4.5 12l6.75-6.75" />
      </svg>


      </button>

      Question {{ this.currentQuestionPosition }} /
      {{ this.totalNumberOfQuestion }}

      
      <button
        class="align-middle ml-4 p-2 rounded bg-white bg-opacity-40 hover:bg-opacity-30 hover:text-black"
        @click="
          if (this.currentQuestionPosition + 1 <= this.totalNumberOfQuestion) {
            this.currentQuestionPosition++;
            loadQuestionByPosition();
          }
        "
      >
      <svg xmlns="http://www.w3.org/2000/svg" fill="none" viewBox="0 0 24 24" stroke-width="1.5" stroke="currentColor" class="w-6 h-6">
        <path stroke-linecap="round" stroke-linejoin="round" d="M4.5 12h15m0 0l-6.75-6.75M19.5 12l-6.75 6.75" />
      </svg>

      </button>
    </div>

    <div class="mt-4 px-8">
      <QuestionDisplay
        :question="currentQuestion"
        @click-on-answer="answerClickedHandler"
      />
    </div>

  </div>

  </div>
</template>

<script>
import QuestionDisplay from "../views/QuestionDisplay.vue";
import quizApiService from "@/services/QuizApiService";
import participationStorageService from "@/services/ParticipationStorageService";

export default {
  name: "QuestionsPage",
  components: {
    QuestionDisplay,
  },
  data() {
    return {
      totalNumberOfQuestion: 0,
      currentQuestionPosition: 1,
      username: null,
      answers: [],
      currentQuestion: {
        questionTitle: "",
        questionText: "",
        questionImage: "",
        possibleAnswers: [],
      },
      myStyle: {
        textAlign: "center",
        paddingBottom: "10em",
        backgroundSize: "100% auto",
        backgroundAttachment: "fixed, scroll, local",
        backgroundImage: "url(https://wallpaper.dog/large/20523548.jpg)",
      },
      myTextStrokeRule: {
        textShadow:
          "0 4px 3px CadetBlue, 0 -4px 3px CadetBlue, 4px 0 3px CadetBlue, -4px 0 3px CadetBlue",
        webkitTextStroke: "0.1px",
        webkitTextStrokeColor: "white",
      },
    };
  },
  async created() {
    var quizInfoPromise = quizApiService.getQuizInfo();
    var quizInfoApiResult = await quizInfoPromise;
    this.totalNumberOfQuestion = quizInfoApiResult.data.size;
    this.username = participationStorageService.getPlayerName();
    this.answers = Array(this.totalNumberOfQuestion).fill(0);
    this.loadQuestionByPosition();
  },
  methods: {
    async loadQuestionByPosition() {
      console.log("load Question By Position");
      var quizInfoPromise = quizApiService.getQuestion(
        this.currentQuestionPosition
      );
      var quizInfoApiResult = await quizInfoPromise;
      this.currentQuestion.questionTitle = quizInfoApiResult.data.title;
      this.currentQuestion.questionText = quizInfoApiResult.data.text;
      this.currentQuestion.questionImage = quizInfoApiResult.data.image;
      this.currentQuestion.possibleAnswers =
        quizInfoApiResult.data.possibleAnswers;
    },
    async answerClickedHandler(answer) {
      console.log("answer Clicked Handler");
      this.answers[this.currentQuestionPosition - 1] = answer;
      if (this.currentQuestionPosition + 1 > this.totalNumberOfQuestion)
        return this.endQuiz();
      this.currentQuestionPosition++;
      this.loadQuestionByPosition();
    },
    async endQuiz() {
      console.log("end Quiz");
      var username = participationStorageService.getPlayerName();
      var quizInfoPromise = quizApiService.submitAnswers(
        this.username,
        this.answers
      );
      var quizInfoApiResult = await quizInfoPromise;
      var score = quizInfoApiResult.data.score;
      participationStorageService.saveParticipationScore(score);
      this.$router.push("/score");
    },
  },
};
</script>

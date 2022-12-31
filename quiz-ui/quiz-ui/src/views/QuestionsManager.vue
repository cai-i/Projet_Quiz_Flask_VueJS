<template>
  <div :style="myStyle">
    <h1
      class="py-8 px-8 text-2xl font-bold text-red-800"
      :style="myTextStrokeRule"
    >
      Notre quiz saura t-il vous mettre en PLS ?
    </h1>

    <h1
      class="mt-2 font-bold text-xl text-yellow-700 border bg-white bg-opacity-50"
    >
      Question {{ this.currentQuestionPosition }} /
      {{ this.totalNumberOfQuestion }}
    </h1>

    <div class="py-8 px-8">
      <QuestionDisplay
        :question="currentQuestion"
        @click-on-answer="answerClickedHandler"
      />
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
      answers: [],
      currentScore: 0,
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
    async answerClickedHandler(answer, answerCorrect) {
      console.log("answer Clicked Handler");
      this.answers[this.currentQuestionPosition - 1] = answer;
      this.currentQuestionPosition++;
      //if (answerCorrect)
      //  this.currentScore++;
      if (this.currentQuestionPosition > this.totalNumberOfQuestion)
        return this.endQuiz();
      this.loadQuestionByPosition();
    },
    async endQuiz() {
      console.log("end Quiz");
      //var score = this.currentScore;
      var username = participationStorageService.getPlayerName();
      var quizInfoPromise = quizApiService.submitAnswers(
        username,
        this.answers
      );
      var quizInfoApiResult = await quizInfoPromise;
      var score = quizInfoApiResult.data.score;
      participationStorageService.saveParticipationScore(score);
      this.$router.push("/");
    },
  },
};
</script>

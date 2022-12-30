<template>
  <header>
    <h1>QuizPage</h1>
  </header>

<h1>Question {{ this.currentQuestionPosition }} / {{ this.totalNumberOfQuestion }}</h1>
<QuestionDisplay :question=currentQuestion @click-on-answer="answerClickedHandler" />
 
</template>



<script>
import QuestionDisplay from '../views/QuestionDisplay.vue'
import quizApiService from "@/services/QuizApiService";
import participationStorageService from "@/services/ParticipationStorageService";

export default {
  name: "QuestionsPage",
  components: {
    QuestionDisplay
  },
  data() {
    return {
      totalNumberOfQuestion:0,
      currentQuestionPosition:1,
      currentScore:0,
      currentQuestion: {
        questionTitle:"",
        questionText:"",
        questionImage:"",
        possibleAnswers:[],
      }
    };
  },
  async created() {    
      var quizInfoPromise = quizApiService.getQuizInfo();
      var quizInfoApiResult = await quizInfoPromise;
      this.totalNumberOfQuestion = quizInfoApiResult.data.size;
      this.loadQuestionByPosition();
  },
  methods:{
    async loadQuestionByPosition() {
      console.log("load Question By Position");
      var quizInfoPromise = quizApiService.getQuestion(this.currentQuestionPosition);
      var quizInfoApiResult = await quizInfoPromise;
      this.currentQuestion.questionTitle = quizInfoApiResult.data.title;
      this.currentQuestion.questionText = quizInfoApiResult.data.text;
      this.currentQuestion.questionImage = quizInfoApiResult.data.image;
      this.currentQuestion.possibleAnswers = quizInfoApiResult.data.possibleAnswers;
    },
    async answerClickedHandler(answerCorrect) {
      console.log("answer Clicked Handler");  
      if (answerCorrect)
        this.currentScore++;
      this.currentQuestionPosition++;
      if (this.currentQuestionPosition>this.totalNumberOfQuestion)
        return this.endQuiz();
      this.loadQuestionByPosition();
    },
    async endQuiz() {
      console.log("end Quiz");
      participationStorageService.saveParticipationScore(this.currentScore);
      this.$router.push('/');
    }
  }
};
</script>
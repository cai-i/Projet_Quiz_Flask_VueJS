<template>
  <header>
    <h1>QuizPage</h1>
  </header>

<h1>Question {{ this.currentQuestionPosition }} / {{ this.totalNumberOfQuestion }}</h1>
<!--
-->
<QuestionDisplay :question="currentQuestion" @click-on-answer="answerClickedHandler" />


<!--
<QuestionDisplay :question.questionTitle="questionTitle"
  :question.questionText="questionText"
  :question.questionImage="questionImage"
  :question.possibleAnswers="possibleAnswers"
   @click-on-answer="answerClickedHandler" />

-->

</template>



<script>
import quizApiService from "@/services/QuizApiService";
import QuestionDisplay from '../views/QuestionDisplay.vue'

export default {
  name: "QuestionsPage",
  components: {
    QuestionDisplay
  },
  data() {
    answers:[];
    return {
      totalNumberOfQuestion:0,
      currentQuestionPosition:1,
      post:{
        currentQuestion: {
          questionTitle:"",
          questionText:"",
          questionImage:"",
          possibleAnswers:[],
        }
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
      console.log(quizInfoApiResult);
      this.questionTitle = quizInfoApiResult.data.title;
      this.questionText = quizInfoApiResult.data.text;
      this.questionImage = quizInfoApiResult.data.image;
      this.possibleAnswers = quizInfoApiResult.data.possibleAnswers;
      console.log(this.questionTitle);
    },
    async answerClickedHandler(answerPosition) {
      console.log("answer Clicked Handler");     
      //this.answers.push(answerPosition);
      this.currentQuestionPosition ++;
      this.loadQuestionByPosition();
    },
    async endQuiz() {
      console.log("end Quiz");
      
    }
  }
};
</script>
<template>
  <div v-if="!this.loading">
    <div class="bg-orange-100 ">
      <div class="w-5/6 mx-auto ">
      <section class="">
        <p class="relative py-8 text-5xl flex items-center ">
            <svg xmlns="http://www.w3.org/2000/svg" fill="none" viewBox="0 0 24 24" stroke-width="1.5" stroke="currentColor" class="w-12 h-12 mr-2 text-red-700">
                <path stroke-linecap="round" stroke-linejoin="round" d="M4.26 10.147a60.436 60.436 0 00-.491 6.347A48.627 48.627 0 0112 20.904a48.627 48.627 0 018.232-4.41 60.46 60.46 0 00-.491-6.347m-15.482 0a50.57 50.57 0 00-2.658-.813A59.905 59.905 0 0112 3.493a59.902 59.902 0 0110.399 5.84c-.896.248-1.783.52-2.658.814m-15.482 0A50.697 50.697 0 0112 13.489a50.702 50.702 0 017.74-3.342M6.75 15a.75.75 0 100-1.5.75.75 0 000 1.5zm0 0v-3.675A55.378 55.378 0 0112 8.443m-7.007 11.55A5.981 5.981 0 006.75 15.75v-1.5" />
            </svg>
            <span class="font-bold text-red-700">Admin</span>
        </p>
        <p class="text-2xl flex items-center px-6">Edition des questions</p>
        <h1 class="py-8 px-6 text-2xl font-bold text-red-800">
            Notre quiz saura t-il vous mettre en PLS ?
      </h1>
        <ul>
            <li v-for="index in this.totalNumberOfQuestion" :key="index">
                
                
                <h1 class="mt-2 px-12 ml-6 font-bold text-xl text-yellow-700 border bg-white bg-opacity-50">
                    Question {{ index }} / {{ this.totalNumberOfQuestion }}
                </h1>
                
                <div class="py-8 ml-6">
                  <QuestionAdminDisplay :question=registeredQuestions[index-1] />
                </div>
            </li>
        </ul>
      </section>
    </div>
    </div>
    </div>
  </template>
<script>

import QuestionAdminDisplay from "./QuestionAdminDisplay.vue";
import quizApiService from "@/services/QuizApiService";

export default {
  components: {
    QuestionAdminDisplay,
  },
  data() {
    return {
      registeredQuestions : [],
      totalNumberOfQuestion: 1,
      currentQuestionPosition: 1,
      loading: true
    };
  },
  async created() {   
    var quizInfoPromise = quizApiService.getQuizInfo();
    var quizInfoApiResult = await quizInfoPromise;
    this.totalNumberOfQuestion = quizInfoApiResult.data.size;
    
    this.loadAllQuestions().then(
      response => {
          this.loading = false;
          console.log(this.registeredQuestions);
      }
    )
    
  },
  methods: {
      async loadAllQuestions() {
        for(let index = 1; index <= this.totalNumberOfQuestion; index++ ){
          var currentQuestion = {
            id: 0,
            questionText:"",
            questionTitle:"",
            questionImage:"",
            position: 0,
            possibleAnswers:[],
          }
          var questionPromise = quizApiService.getQuestion(index);
          var questionApiResult = await questionPromise;
          console.log(questionApiResult);
          currentQuestion.id = questionApiResult.data.id;
          currentQuestion.position = questionApiResult.data.position;
          currentQuestion.questionTitle = questionApiResult.data.title;
          currentQuestion.questionText = questionApiResult.data.text;
          currentQuestion.questionImage = questionApiResult.data.image;
          currentQuestion.possibleAnswers = questionApiResult.data.possibleAnswers;
          this.registeredQuestions.push(currentQuestion);
        }
      },
      
  }
}
</script>

<template>
    <h1>Question List page</h1>
    <!-- <ul>
        <li v-for="index in this.totalNumberOfQuestion" :key="index">
            <h1 class="py-8 px-8 text-2xl font-bold text-red-800">
                Notre quiz saura t-il vous mettre en PLS ?
            </h1>
            
            <h1 class="mt-2 font-bold text-xl text-yellow-700 border bg-white bg-opacity-50">
                Question {{ index }} / {{ this.totalNumberOfQuestion }}
            </h1>
            
            <div class="py-8 px-8">
                <QuestionAdminDisplay :question=registeredQuestions[index] />
            </div>
        </li>
    </ul> -->
  </template>

<script>

  import quizApiService from "@/services/QuizApiService";
  
  export default {
    data() {
      return {
        registeredQuestions : [],
        totalNumberOfQuestion: 0,
        currentQuestion: {
            questionTitle:"",
            questionText:"",
            questionImage:"",
            possibleAnswers:[],
        },
      };
    },
    async created() {    
      var quizInfoPromise = quizApiService.getQuizInfo();
      var quizInfoApiResult = await quizInfoPromise;
      this.totalNumberOfQuestion = quizInfoApiResult.data.size;

      Array.from({length: this.totalNumberOfQuestion}, (_, i) => i + 1).forEach(index => {
        this.loadQuestionByPosition(index)});
    },
    methods: {
        async loadQuestionByPosition(index) {
            console.log("load Question By Position");
            var questionPromise = quizApiService.getQuestion(index);
            var questionApiResult = await questionPromise;
            this.currentQuestion.questionTitle = questionApiResult.data.title;
            this.currentQuestion.questionText = questionApiResult.data.text;
            this.currentQuestion.questionImage = questionApiResult.data.image;
            this.currentQuestion.possibleAnswers = questionApiResult.data.possibleAnswers;
            this.registeredQuestions.push( this.currentQuestion );
        }
    }
    
    
}
</script>
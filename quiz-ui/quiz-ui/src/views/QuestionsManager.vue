<template>
  <header>

  <h1>QuizPage</h1>
  <div v-for="question in registeredQuestions">
    {{ question.position }} - {{ question.title }}
    {{ question.text }}  
    {{ question.possibleAnswers }}
  </div>

  </header>
  haaaaaaaaa
</template>

<script>
import quizApiService from "@/services/QuizApiService";

export default {
  name: "QuestionsPage",
  data() {
    return {
      registeredQuestions : []
    };
  },
  async created() {
    console.log('quizApiService.getQuestion(position)')
    var quizInfoPromise = quizApiService.getAllQuestion();
    var quizInfoApiResult = await quizInfoPromise;
    this.registeredQuestions = quizInfoApiResult.data;
		console.log("Composant Quiz page 'created'");
  }
};
</script>
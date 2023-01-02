<template>
  
<!-- Le loading permet d'afficher que si les données ont été chargées, sans ça, on voit la page se chargée et c'est un petit peu saccadé
     Si le token d'authentification est null, on est renvoyé à la page de connexion (voir created())
-->
  <div v-if="!this.loading && this.adminMode">
    <div class="bg-orange-50">
      <div class="w-5/6 mx-auto pb-16">
            <p class="relative py-8 text-3xl flex items-center ">
              <span class="font-bold text-red-700">Edition des questions</span>
            </p>
            <div class="flex mt-2 bg-orange-50 border-2 border-orange-200 rounded-md">
              <div class="w-64 bg-orange-100 rounded-l-md border-r border-dashed border-orange-200">
                <div class="flex justify-center items-center h-16 text-orange-800 text-center font-semibold text-3xl">
                  Questions
                </div>

                <!-- Formulaire vide pour l'ajout d'une question, la position est par défaut celle pour être la dernière question -->
                <div class="place-content-center gap-4 border-b-2 flex border-orange-200">
                    <button @click="displayNewForm">
                      <svg class="w-10 h-10 mb-4 hover:fill-orange-200" fill="none" stroke="DarkRed" viewBox="0 0 24 24" xmlns="http://www.w3.org/2000/svg"><path stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="M12 9v3m0 0v3m0-3h3m-3 0H9m12 0a9 9 0 11-18 0 9 9 0 0118 0z"></path></svg>
                    </button>
                    <button @click="removeAllQuestions">
                      <svg class="w-10 h-10 mb-4 hover:fill-orange-200" fill="none" stroke="DarkRed" viewBox="0 0 24 24" xmlns="http://www.w3.org/2000/svg"><path stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="M19 7l-.867 12.142A2 2 0 0116.138 21H7.862a2 2 0 01-1.995-1.858L5 7m5 4v6m4-6v6m1-10V4a1 1 0 00-1-1h-4a1 1 0 00-1 1v3M4 7h16"></path></svg>
                    </button>
                </div>

                <!-- Selection et suppression de question par la position  -->
                <ul>
                  <li v-for="index in this.totalNumberOfQuestion" :key="index">
                    <div class="border-b-2 border-orange-200 grid grid-cols-10">
                      <button @click="selectQuestion(index)" class="col-span-8 border-r-2 border-orange-200 hover:bg-orange-200 pl-10 py-3 text-orange-700 font-semibold">
                        Question {{ index }}
                      </button>
                      <button @click="removeQuestion(index)" class="col-span-2 place-content-center grid hover:bg-orange-200">
                        <svg class="w-5 h-5 hover:fill-orange-200" fill="none" stroke="DarkRed" viewBox="0 0 24 24" xmlns="http://www.w3.org/2000/svg"><path stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="M19 7l-.867 12.142A2 2 0 0116.138 21H7.862a2 2 0 01-1.995-1.858L5 7m5 4v6m4-6v6m1-10V4a1 1 0 00-1-1h-4a1 1 0 00-1 1v3M4 7h16"></path></svg>
                      </button>
                    </div>
                  </li>
                </ul>
                
              </div>

              <!-- Affichage du formulaire: - s'il n y a pas de question, un formulaire vide est affiché, l'id est null, saveQuestion dans QuestionAdminDisplay enverra un post à la validation
                                            - sinon, la première question sera chargée lors du chargement de la page puis celle selectionnée, l'id est detectée, saveQuestion dans QuestionAdminDisplay enverra un put à la validation
              -->
              
              <div class="flex-grow">
                <div class="py-8 ml-6">
                  <div v-if="this.currentQuestion.id == null" class="text-orange-600 px-4 font-semibold text-2xl">Nouvelle question</div>
                  <QuestionAdminDisplay :question=this.currentQuestion />
                </div>
              </div>

          </div>
        </div>
      </div>
    </div>
</template>

<script>

import QuestionAdminDisplay from "./QuestionAdminDisplay.vue";
import quizApiService from "@/services/QuizApiService";
import participationStorageService from "@/services/ParticipationStorageService";

export default {
  components: {
    QuestionAdminDisplay,
  },
  data() {
    return {
      currentQuestion: {
        id: null,
        questionText:"",
        questionTitle:"",
        questionImage:"",
        position: 1,
        possibleAnswers:[],
      },
      totalNumberOfQuestion: 1,
      loading: true,
      adminMode: true
    };
  },
  async created() {
    var token = participationStorageService.getAuthentificationToken();
    if(token != null){
      this.adminMode = true;
      var quizInfoPromise = quizApiService.getQuizInfo();
      var quizInfoApiResult = await quizInfoPromise;
      this.totalNumberOfQuestion = quizInfoApiResult.data.size;
      if(this.totalNumberOfQuestion > 0){
        this.loadQuestion(1).then(
          response => {
              this.loading = false;
          }
        );
      }
      else { this.loading = false;}
    }
    else {
      this.$router.push("/admin");
    }
  },
  methods: {
    selectQuestion(index){
      this.loadQuestion(index);
    },

    // Cela ne semble pas possible de delete une question par sa position, un getQuestionByPosition est utilisé
    async removeQuestion(index){
      var questionPromise = quizApiService.getQuestionByPosition(index);
      var questionApiResult = await questionPromise;
      var removeQuestionPromise = quizApiService.removeQuestion(questionApiResult.data.id);
      await removeQuestionPromise;
      location.reload();
    },
    async removeAllQuestions(){
      var questionsPromise = quizApiService.removeAllQuestions();
      await questionsPromise;
      location.reload();
    },
    displayNewForm(){
      this.currentQuestion.id = null;
      this.currentQuestion.position = this.totalNumberOfQuestion + 1;
      this.currentQuestion.questionTitle = "";
      this.currentQuestion.questionText = "";
      this.currentQuestion.questionImage = "";
      this.currentQuestion.possibleAnswers = [];
    },

    // Similaire à celui de QuestionManager, mais l'id et la position ont été ajoutée car utile pour le put et/ou post
    async loadQuestion(position) {
        var questionPromise = quizApiService.getQuestionByPosition(position);
        var questionApiResult = await questionPromise;
        this.currentQuestion.id = questionApiResult.data.id;
        this.currentQuestion.position = questionApiResult.data.position;
        this.currentQuestion.questionTitle = questionApiResult.data.title;
        this.currentQuestion.questionText = questionApiResult.data.text;
        this.currentQuestion.questionImage = questionApiResult.data.image;
        this.currentQuestion.possibleAnswers = questionApiResult.data.possibleAnswers;
      }
    },
  }
</script>

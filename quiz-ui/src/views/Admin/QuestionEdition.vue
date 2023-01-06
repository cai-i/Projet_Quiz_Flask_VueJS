<template>
  
<!-- Le loading permet d'afficher que si les données ont été chargées, sans ça, on voit la page se chargée et c'est un petit peu saccadé
     Si le token d'authentification est null, on est renvoyé à la page de connexion (voir created())
-->
  <div v-if="!this.loading && this.adminMode">
    <div class="bg-orange-50 mt-8">
        <div class="flex bg-orange-50 border-2 border-orange-200 rounded-md">
          <div class="w-64 bg-orange-100 rounded-l-md border-r border-dashed border-orange-200">
            <div class="flex justify-center items-center h-16 text-orange-800 text-center font-semibold text-3xl">
              Questions
            </div>

            <!-- Formulaire vide pour l'ajout d'une question, la position est par défaut celle pour être la dernière question -->
            <div class="place-content-center gap-4 border-b-2 flex border-orange-300">
                <button @click="displayNewForm">
                  <svg class="w-10 h-10 mb-4 hover:fill-orange-300 " :class="{ ['fill-orange-300'] : this.isDisplayingNewForm}" fill="none" stroke="DarkRed" viewBox="0 0 24 24" xmlns="http://www.w3.org/2000/svg"><path stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="M12 9v3m0 0v3m0-3h3m-3 0H9m12 0a9 9 0 11-18 0 9 9 0 0118 0z"></path></svg>
                </button>
                <button id="modal-switch" @click="toggleModal">
                  <svg class="w-10 h-10 mb-4 hover:fill-orange-300" fill="none" stroke="DarkRed" viewBox="0 0 24 24" xmlns="http://www.w3.org/2000/svg"><path stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="M19 7l-.867 12.142A2 2 0 0116.138 21H7.862a2 2 0 01-1.995-1.858L5 7m5 4v6m4-6v6m1-10V4a1 1 0 00-1-1h-4a1 1 0 00-1 1v3M4 7h16"></path></svg>
                </button>
            </div>

            <!-- Selection et suppression de question par la position  -->
            <ul>
              <li v-for="index in this.totalNumberOfQuestion" :key="index">
                <div class="border-b-2 border-orange-300 grid grid-cols-10">
                  <button @click="selectQuestion(index)" class="col-span-8 grid grid-cols-10 border-r-2 border-orange-300 hover:bg-orange-300 text-orange-700 font-semibold" :class="[this.selectedQuestion === index ? 'bg-orange-300' : 'bg-orange-200']">
                    <p class="col-span-2 bg-orange-100 rounded-full grid place-content-center px-3 mx-1 py-1 my-2 text-base"> {{index}} </p> 
                    <p class="col-span-8 truncate px-4 py-3">{{ registeredTitles[index-1] }}</p>
                  </button>
                  <button @click="removeQuestion(index)" class="col-span-2 place-content-center grid hover:bg-orange-300">
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
              <QuestionAdminDisplay :question=this.currentQuestion :totalNumberOfQuestion="this.totalNumberOfQuestion" />
            </div>
          </div>

          <div v-if="showModal" class="fixed inset-0 z-50 outline-none focus:outline-none justify-center items-center flex">
            <Modal @toggle-modal="toggleModal" @remove-all-questions="removeAllQuestions"/>
          </div>
          <div v-if="showModal" class="opacity-25 fixed inset-0 z-40 bg-black"></div>
        </div>
    </div>
  </div>
  <div v-else class="h-screen bg-orange-100 justify-center mt-32 grid">
    <svg aria-hidden="true" class="mr-2 w-20 h-20 text-gray-200 animate-spin dark:text-gray-600 fill-red-700" viewBox="0 0 100 101" fill="none" xmlns="http://www.w3.org/2000/svg">
        <path d="M100 50.5908C100 78.2051 77.6142 100.591 50 100.591C22.3858 100.591 0 78.2051 0 50.5908C0 22.9766 22.3858 0.59082 50 0.59082C77.6142 0.59082 100 22.9766 100 50.5908ZM9.08144 50.5908C9.08144 73.1895 27.4013 91.5094 50 91.5094C72.5987 91.5094 90.9186 73.1895 90.9186 50.5908C90.9186 27.9921 72.5987 9.67226 50 9.67226C27.4013 9.67226 9.08144 27.9921 9.08144 50.5908Z" fill="currentColor"/>
        <path d="M93.9676 39.0409C96.393 38.4038 97.8624 35.9116 97.0079 33.5539C95.2932 28.8227 92.871 24.3692 89.8167 20.348C85.8452 15.1192 80.8826 10.7238 75.2124 7.41289C69.5422 4.10194 63.2754 1.94025 56.7698 1.05124C51.7666 0.367541 46.6976 0.446843 41.7345 1.27873C39.2613 1.69328 37.813 4.19778 38.4501 6.62326C39.0873 9.04874 41.5694 10.4717 44.0505 10.1071C47.8511 9.54855 51.7191 9.52689 55.5402 10.0491C60.8642 10.7766 65.9928 12.5457 70.6331 15.2552C75.2735 17.9648 79.3347 21.5619 82.5849 25.841C84.9175 28.9121 86.7997 32.2913 88.1811 35.8758C89.083 38.2158 91.5421 39.6781 93.9676 39.0409Z" fill="currentFill"/>
    </svg>
  </div>
</template>

<script>

import QuestionAdminDisplay from "./QuestionAdminDisplay.vue";
import quizApiService from "@/services/QuizApiService";
import participationStorageService from "@/services/ParticipationStorageService";
import Modal from "./Modal.vue";

export default {
  components: {
    QuestionAdminDisplay,
    Modal
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
      showModal: false,
      adminMode: false,
      isDisplayingNewForm: false,
      selectedQuestion: 1,
      registeredTitles: []
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
        Promise.all([this.loadAllTitles(), this.loadQuestion(1)]).then((response) => {
          this.loading = false;
        })
      }
      else {
        this.loading = false;
      }
    }
  },
  methods: {
    selectQuestion(index){
      this.isDisplayingNewForm = false;
      this.selectedQuestion = index;
      this.loadQuestion(index);
    },
    toggleModal(){
      this.showModal = !this.showModal;
    },
    displayNewForm(){
      this.selectedQuestion = 0;
      this.isDisplayingNewForm = true;

      this.currentQuestion.id = null;
      this.currentQuestion.position = this.totalNumberOfQuestion + 1;
      this.currentQuestion.questionTitle = "";
      this.currentQuestion.questionText = "";
      this.currentQuestion.questionImage = "";
      this.currentQuestion.possibleAnswers = [];
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
    },
    async loadAllTitles() {
        for(let index = 1; index <= this.totalNumberOfQuestion; index++ ){
          var questionPromise = quizApiService.getQuestionByPosition(index);
          var questionApiResult = await questionPromise;
          var title = questionApiResult.data.title;
          this.registeredTitles.push(title);
        }
    },
  }
}
</script>

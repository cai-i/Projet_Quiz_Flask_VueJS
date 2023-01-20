<template>
  
  <div :style="myStyle">
  
    <div class="w-5/6 mx-auto">
      <div v-if="this.loading" class="p-8 pt-24">
        <!-- Loading animation elements -->
        <loadAnim></loadAnim>
      </div>
      <div v-else >
        <div v-if="this.totalNumberOfQuestion !== 0">
          <h1
            class="py-8 px-8 text-3xl font-bold text-red-600"
            :style="myTextStrokeRule"
          >
            Impressionnez-nous !
          </h1>
          <div class="flex items-center mb-4 gap-4">
            <div class="flex items-center gap-4 grow text-left font-bold text-black text-xl" v-if="username" :style="myTextStrokeRule">
              Joueur : {{ this.username }} 
            </div>
            <div class="place-content-end">

              <button class="flex items-center gap-2 bg-rose-700 hover:bg-rose-900 text-white font-bold py-2 px-4 rounded focus:outline-none focus:shadow-outline"
              @click="this.endQuiz()">
                <svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 20 20" fill="currentColor" class="w-5 h-5">
                  <path d="M3.105 2.289a.75.75 0 00-.826.95l1.414 4.925A1.5 1.5 0 005.135 9.25h6.115a.75.75 0 010 1.5H5.135a1.5 1.5 0 00-1.442 1.086l-1.414 4.926a.75.75 0 00.826.95 28.896 28.896 0 0015.293-7.154.75.75 0 000-1.115A28.897 28.897 0 003.105 2.289z" />
                </svg>
                Terminer
              </button>
            </div>
          </div>

          <div
            class="text-center shadow-md border rounded bg-white bg-opacity-60"
          >
            
            <div class="mb-16 mt-8 mx-16 ">
              <div
                class="flex place-content-center gap-6 p-2 rounded font-bold text-xl text-sky-700 border bg-white bg-opacity-50"
              >
                <button
                    class="px-1 py-1 align-middle rounded hover:bg-white hover:bg-opacity-50 hover:text-black"
                    @click="
                      if (this.currentQuestionPosition - 1 > 0) {
                        this.currentQuestionPosition--;
                        loadQuestionByPosition();
                      }
                    "
                  >
                  <svg xmlns="http://www.w3.org/2000/svg" fill="none" viewBox="0 0 24 24" stroke-width="2.5" stroke="currentColor" class="w-6 h-6">
                    <path stroke-linecap="round" stroke-linejoin="round" d="M15.75 19.5L8.25 12l7.5-7.5" />
                  </svg>
                </button>

                Question {{ this.currentQuestionPosition }} /
                {{ this.totalNumberOfQuestion }}
                
                <button
                  class="px-1 py-1 rounded hover:bg-white hover:bg-opacity-50 hover:text-black"
                  @click="
                    if (this.currentQuestionPosition + 1 <= this.totalNumberOfQuestion) {
                      this.currentQuestionPosition++;
                      loadQuestionByPosition();
                    }
                    else this.endQuiz();
                  "
                >
                  <svg xmlns="http://www.w3.org/2000/svg" fill="none" viewBox="0 0 24 24" stroke-width="2.5" stroke="currentColor" class="w-6 h-6">
                    <path stroke-linecap="round" stroke-linejoin="round" d="M8.25 4.5l7.5 7.5-7.5 7.5" />
                  </svg>
                </button>
              </div>

              <QuestionDisplay
                :question="currentQuestion" :selectedAnswer="answers[this.currentQuestionPosition-1]"
                @click-on-answer="answerClickedHandler"
              />
            </div>
          </div>
        </div>
        <div v-else class="py-40 text-white font-bold text-3xl items-center justify-center">
          <h1 class="text-5xl mb-3 animate-bounce"> Oops ! </h1> 
          Il n'y a pas encore de question.
        </div>
      </div>
    </div>
  </div>
</template>

<script>
import QuestionDisplay from "../views/QuestionDisplay.vue";
import quizApiService from "@/services/QuizApiService";
import participationStorageService from "@/services/ParticipationStorageService";
import LoadAnim from './Components/LoadAnim.vue';

export default {
  name: "QuestionsPage",
  components: {
    QuestionDisplay,LoadAnim
  },
  data() {
    return {
      loading: true,
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
        backgroundImage: 
        // "url(https://wallpaper.dog/large/20523548.jpg)",
        // "url(https://img.rawpixel.com/private/static/images/website/2022-05/upwk82583677-wikimedia-image-kows5907.jpg?w=1200&h=1200&dpr=1&fit=clip&crop=default&fm=jpg&q=75&vib=3&con=3&usm=15&cs=srgb&bg=F4F4F3&ixlib=js-2.2.1&s=94d8d8d28d58bcee9ebf690dfa3917c8)",
        // "url(https://live.staticflickr.com/65535/51216709489_0de8256b15_b.jpg)",

        "url(https://c.pxhere.com/photos/7f/7a/fish_ink_painting_china_wind-1235431.jpg!d)",
      },
      myTextStrokeRule: {
        textShadow:
          "0 4px 6px white, 0 -4px 6px CadetBlue, 4px 0 3px CadetBlue, -4px 0 3px CadetBlue",
        webkitTextStroke: "0.3px",
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
    if(this.totalNumberOfQuestion > 0){
      this.loadQuestionByPosition().then(
        response => {
            this.loading = false;
        }
      );
    }
    else if (this.totalNumberOfQuestion === 0){
      this.loading = false;
    }
    console.log("QuestionsPage created");
  },
  methods: {
    async loadQuestionByPosition() {
      console.log("load Question By Position");
      var quizInfoPromise = quizApiService.getQuestionByPosition(
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
      this.username = participationStorageService.getPlayerName();
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


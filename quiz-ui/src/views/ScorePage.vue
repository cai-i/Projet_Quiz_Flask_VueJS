<template>
  <div
    class="py-11 bg-cover bg-center bg-no-repeat bg-fixed"
    style="
      background-image: url(./assets/imgs/city_night.jpg);
    "
  >

    <div class="w-5/6 mx-auto">
      <div v-if="this.statsLoaded">
        <!--message pour le joueur-->
        <div
          v-if="this.userScore"
          class="m-2 font-bold font-mono text-pink-400 text-center text-3xl"
          :style="myTextStrokeRule"
        >
          <div
            v-if="this.userRank === 1"
          >
            Bravo {{ this.userName }}, vous êtes premier !!
            <div class="animate-pulse ml-4 mr-4 mt-2">Pour l'instant...</div>
          </div>

          <div
            v-else-if="this.rate > 2 / 3"
          >
            Bravo {{ this.userName }},
            <div class="animate-bounce ml-4 mr-4 mt-2">sentez-vous supérieur</div>
            à {{ this.registeredScores.length - this.userRank }}
            joueurs aujourd'hui !
          </div>

          <div
            v-else-if="this.rate > 1 / 3"
          >
            Bof, dans la moyenne...
            <div class="inline-flex">
              <div class="animate-bounce ml-4 mr-4">ouf</div>
              ?
            </div>
          </div>

          <div
            v-else
          >
            Aïe {{ this.userName }}, vous vous êtes fait
            <div class="inline-flex">
              <div class="animate-bounce">détruire</div>
              !
            </div>
          </div>
        </div>

        <div class="items-center max-w-fit mx-auto">
          <div
            class="dynamicCard flex items-center place-content-center gap-4 rounded-t-2xl rounded-l-2xl mt-8 p-6 bg-slate-400 shadow-black/40 shadow-inner"
            
          >
            <!-- Cercle de score animé -->
            <ScoreLoadAnim 
              :nbr_questions="this.nbr_questions" 
              :userScore="this.userScore">    
            </ScoreLoadAnim>

            <!-- Stats du joueur   -->
            <div class="p-6 flex flex-col gap-4 text-3xl text-left">
              <div class="font-mono">
                <p class="text-red-700">Score :</p>
                <p class="font-bold text-center">
                  {{ this.userScore }} / {{ nbr_questions }}
                </p>
              </div>
              <div class="font-mono">
                Rang :
                <p class="font-bold text-center">
                  {{ this.userRank }} / {{ this.registeredScores.length }}
                </p>
              </div>
            </div>

              <!-- Les deux boutons pour clean les variables -->
            <div class="flex flex-col gap-4">
              <button
                class="flex place-content-center items-center gap-4 w-28 h-28 item-center text-white rounded-full bg-gray-800/80 hover:bg-gray-800"
                @click="this.restartGame();"
              >
                <p class="link link-underline link-underline-white"> Rejouer ! 
                </p>
              </button>
            </div>
          </div>

          <div class="place-content-end mb-12 flex">
            <button
              class="items-center gap-4 py-2 w-48 border border-slate-400 item-center text-white rounded-b-lg bg-gray-800/80 hover:bg-gray-900"
              @click="this.toggleShowAnswers();"
            >
              <p v-if="this.showAnswers">Fermer les réponses</p>
              <p v-else>Consulter les réponses</p>
            </button>
          </div>

        </div>
        
      </div>

      <div v-else class="p-8 pt-24">
        <!-- Loading animation elements -->
        <LoadAnim></LoadAnim>
      </div>

      <div v-if="this.showAnswers">

        <div class="w-2/3 mx-auto mb-14">
            <template
              v-for="(item, index) in registeredAnswers"
              v-bind:key="item.questionText"
            >
              <div class="items-center flex p-2 mb-4">
                <p class="px-2 rounded-l-lg bg-slate-700 text-white text-xl">{{ index+1 }}</p>
                <div class="w-full p-2 rounded-r-lg bg-slate-300 shadow">
                  <p class="text-black">{{ item.questionText }} </p>
                  <p class="text-green-700 font-semibold">{{ item.answer }}</p>
                </div>
              </div>

            </template>
        </div>
      </div>
      <!-- Début tableau -->
        <ScoresTable>
          <!-- image de fond du tableau -->
          <div class="bg-neutral-500 bg-opacity-50 absolute inset-0"></div>
        </ScoresTable>
    </div>
  </div>
</template>


<script>
import quizApiService from "@/services/QuizApiService";
import participationStorageService from "@/services/ParticipationStorageService";
import ScoresTable from './Components/ScoresTable.vue';
import ScoreLoadAnim from './Components/ScoreLoadAnim.vue';
import LoadAnim from './Components/LoadAnim.vue';

export default {
  name: "ScorePage",
  components: { ScoresTable, ScoreLoadAnim, LoadAnim },
  data() {
    return {
      registeredScores: [],
      registeredAnswers: [],
      nbr_questions: 0,
      userName: "",
      userRank: 1,
      userScore: 0,
      rate: "",
      statsLoaded: false,
      showAnswers: false,
      myTextStrokeRule: {
        textShadow:
          "0 4px 8px white, 0 -2px 8px CadetBlue",
        webkitTextStroke: "0.3px",
        webkitTextStrokeColor: "white",
      },
    };
  },
  async created() {
    console.log(quizApiService.getQuizInfo());
    var quizInfoPromise = quizApiService.getQuizInfo();
    var quizInfoApiResult = await quizInfoPromise;
    this.registeredScores = quizInfoApiResult.data.scores;
    this.nbr_questions = quizInfoApiResult.data.size;
    // charger les stats du joueur
    this.scoreStats();
    this.statsLoaded = true;
    // Nettoyer les données du joueur, commenter si test
    //participationStorageService.clear();
    console.log("Composant Score page 'created'");

    for(let index = 1; index <= this.nbr_questions; index++ ){
      var questionPromise = quizApiService.getQuestionByPosition(index);
      var questionApiResult = await questionPromise;
      var questionText = questionApiResult.data.text;
      
      var answerPromise = quizApiService.getAnswerByPosition(index);
      var answerApiResult = await answerPromise;
      var answer = answerApiResult.data.text;
      console.log(answerApiResult)

      var result = {questionText: "", answer: ""}
      result.questionText = questionText;
      result.answer = answer;
      this.registeredAnswers.push(result);
    }
  },
  methods: {
    successRate: function (value) {
      this.rate = String((value * 100) / this.nbr_questions);
      return this.rate;
    },
    scoreStats: function () {
      this.userName = participationStorageService.getPlayerName();
      this.userScore = participationStorageService.getParticipationScore();
      for (var scoreEntry in this.registeredScores) {
        if (
          this.registeredScores[scoreEntry].playerName === this.userName &&
          this.registeredScores[scoreEntry].score == this.userScore
        )
          this.userRank = parseInt(scoreEntry) + 1;
      }
    },
    restartGame: function () {
      this.$router.push("/questions");
    },
    async toggleShowAnswers() {        
      this.showAnswers = !this.showAnswers;
    }
  }
};
</script>



<style scoped>
/* animation pour le background */
.ScorePageBody {
  width: 100%;
  height: 100%;
  padding-bottom: 10em;
  background: linear-gradient(-45deg, #ee7752, #e73c7e, #23a6d5, #23d5ab);
  background-size: 400% 400%;
  animation: gradient 10s ease infinite;
}

@keyframes gradient {
  0% {
    background-position: 0% 50%;
  }
  50% {
    background-position: 100% 50%;
  }
  100% {
    background-position: 0% 50%;
  }
}

/* changer dynamiquement la carte de présentation du joueur */
@media (max-width: 700px) { 
  .dynamicCard{
   flex-direction: column;
  }    
}

/* animation pour score button */
.link-underline {
  border-bottom-width: 0;
  background-image: linear-gradient(transparent, transparent), linear-gradient(#fff, #fff);
  background-size: 0 2px;
  background-position: 0 100%;
  background-repeat: no-repeat;
  transition: background-size .5s ease-in-out;
}

.link-underline-white {
  background-image: linear-gradient(transparent, transparent), linear-gradient(rgb(190, 164, 114), rgb(167, 160, 128))
}

.link-underline:hover {
  background-size: 100% 2px;
  background-position: 0 100%
}
</style>

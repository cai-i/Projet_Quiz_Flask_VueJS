<template>
  <div
    class="bg-cover bg-center bg-no-repeat bg-fixed"
    style="
      background-image: url(https://img.rawpixel.com/private/static/images/website/2022-05/upwk82583677-wikimedia-image-kows5907.jpg?w=1200&h=1200&dpr=1&fit=clip&crop=default&fm=jpg&q=75&vib=3&con=3&usm=15&cs=srgb&bg=F4F4F3&ixlib=js-2.2.1&s=94d8d8d28d58bcee9ebf690dfa3917c8);
    "
  >
    <!-- 
          // "url(https://img.rawpixel.com/private/static/images/website/2022-05/upwk82583677-wikimedia-image-kows5907.jpg?w=1200&h=1200&dpr=1&fit=clip&crop=default&fm=jpg&q=75&vib=3&con=3&usm=15&cs=srgb&bg=F4F4F3&ixlib=js-2.2.1&s=94d8d8d28d58bcee9ebf690dfa3917c8)",
          // "url(https://live.staticflickr.com/65535/51216709489_0de8256b15_b.jpg)", 
          -->

    <div class="p-16">
      <div v-if="this.statsLoaded">
        <!--message pour le joueur-->
        <div
          v-if="this.userScore"
          class="m-2 font-bold font-mono text-pink-400 text-center text-3xl"
          :style="myTextStrokeRule"
        >
          <div
            v-if="this.userRank < this.registeredScores.length / 3"
            class="inline-flex"
          >
            Bravo {{ this.userName }},
            <div class="animate-bounce ml-4 mr-4">sentez-vous supérieur</div>
            à {{ this.registeredScores.length - this.userRank }}
            joueurs aujourd'hui !
          </div>

          <div
            v-if="this.userRank > (this.registeredScores.length * 2) / 3"
            class="inline-flex"
          >
            Aïe {{ this.userName }}, vous vous êtes fait
            <div class="animate-bounce ml-4 mr-4">détruire</div>
            !
          </div>

          <div
            v-if="
              this.userRank >= this.registeredScores.length / 3 &&
              this.userRank <= (this.registeredScores.length * 2) / 3
            "
            class="inline-flex"
          >
            Bof, dans la moyenne...
            <div class="animate-bounce ml-4 mr-4">ouf</div>
            ?
          </div>
        </div>

        <div class="flex items-center">
          <div
            class="max-w-fit mx-auto flex items-center place-content-center gap-4 rounded-2xl mt-8 mb-8 p-6 bg-slate-400 shadow-black/40 shadow-inner"
          >
            <!-- Cercle de score animé -->
            <div v-if="this.circleStyle['--sratio']" class="skill">
              <div class="outer">
                <div class="inner">
                  <div class="number">
                    {{ this.scoreDisplay }}
                  </div>
                </div>
              </div>
              <svg
                xmlns="http://www.w3.org/2000/svg"
                version="1.1"
                width="160px"
                height="160px"
              >
                <defs>
                  <linearGradient id="GradientColor">
                    <stop offset="0%" stop-color="#e91e63" />
                    <stop offset="100%" stop-color="#673ab7" />
                  </linearGradient>
                </defs>
                <circle
                  cx="80"
                  cy="80"
                  r="70"
                  stroke-linecap="round"
                  :style="circleStyle"
                />
              </svg>
            </div>

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
              class="flex place-content-center items-center gap-4 w-24 h-24 item-center rounded-full bg-gray-800/80 hover:bg-gray-700 text-white"
              @click="this.restartGame();"
            >
              <p> Rejouer ! </p>
            </button>

          </div>
          </div>
          
        </div>
      </div>

      <div v-else class="p-8 pt-24">
        <!-- Loading animation elements -->
        <div class="outerCircle"></div>
        <div class="innerCircle"></div>
        <div class="icon"></div>
      </div>
      <!-- Début tableau -->
      <ScoresTable>
        <!-- image de fond du tableau -->
        <div class="ScorePageBody absolute inset-0"></div>
      </ScoresTable>
    </div>
  </div>
</template>

<script>
import quizApiService from "@/services/QuizApiService";
import participationStorageService from "@/services/ParticipationStorageService";
import ScoresTable from './Components/ScoresTable.vue';

export default {
  name: "ScorePage",
  data() {
    return {
      registeredScores: [],
      nbr_questions: 0,
      userName: "",
      userRank: 1,
      userScore: 0,
      rate: "",
      scoreDisplay: "",
      statsLoaded: false,
      circleStyle: {
        "--sratio": null,
        animationPlayState: "paused",
      },
      myTextStrokeRule: {
        textShadow:
          "0 4px 6px white, 0 -4px 6px orange, 4px 0 3px CadetBlue, -4px 0 3px CadetBlue",
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
    // compter pour l'animation du score
    this.scoreLoading();
    // Nettoyer les données du joueur, commenter si test
    //participationStorageService.clear();
    console.log("Composant Score page 'created'");
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
      this.circleStyle["--sratio"] =
        472 * (1 + 0.05 - this.userScore / this.nbr_questions) - 1;
      if (this.userScore == 0) this.circleStyle["--sratio"] = 470;
    },
    scoreLoading: function () {
      this.circleStyle.animationPlayState = "running";
      // Cas score de 0
      if (this.userScore == 0) {
        return (this.scoreDisplay = "0%");
      }
      // Cas score sup a 0
      var counter = 0;
      var incr = parseInt((10 * this.userScore) / this.nbr_questions, 10);
      setInterval(() => {
        if (counter >= (100 * this.userScore) / this.nbr_questions - 10) {
          incr = 1;
        }
        if (counter >= (100 * this.userScore) / this.nbr_questions) {
          clearInterval();
        } else {
          counter += incr;
          this.scoreDisplay = counter + "%";
        }
      });
    },
    restartGame: function () {
      this.$router.push("/start-new-quiz-page");
    },
  },
  components: { ScoresTable }
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

/* Animation pour le score rate  */
.skill {
  width: 160px;
  height: 160px;
  position: relative;
}

.outer {
  height: 160px;
  width: 160px;
  border-radius: 50%;
  padding: 20px;
  box-shadow: 6px 6px 10px -1px rgba(0, 0, 0, 0.25),
    -6px -6px 10px -1px rgba(255, 255, 255, 0.25);
}

.inner {
  height: 120px;
  width: 120px;
  border-radius: 50%;
  display: flex;
  align-items: center;
  justify-content: center;
  box-shadow: inset 4px 4px 6px -1px rgba(0, 0, 0, 0.25),
    inset -4px -4px 6px -1px rgba(255, 255, 255, 0.25),
    -0.5px -0.5px 0px rgba(255, 255, 255, 0.5),
    0.5px 0.5px 0px rgba(0, 0, 0, 0.15), 0px 12px 10px rgba(0, 0, 0, 0.05);
}

.number {
  font-size: xxx-large;
  font-weight: bold;
  color: #555;
}

circle {
  fill: none;
  stroke: url(#GradientColor);
  stroke-width: 20px;
  stroke-dasharray: 472;
  stroke-dashoffset: 472;
  animation: anim 2s linear forwards;
}

svg {
  position: absolute;
  transform: rotate(-90deg);
  top: 0;
  left: 0;
}

@keyframes anim {
  100% {
    stroke-dashoffset: var(--sratio);
  }
}

/* Loading animation */
.outerCircle {
  background-color: transparent;
  border: 8px solid rgba(97, 82, 72, 0.9);
  opacity: 0.9;
  border-right: 5px solid transparent;
  border-left: 5px solid transparent;
  border-radius: 100px;
  width: 103px;
  height: 103px;
  margin: 0 auto;
  -moz-animation: spinPulse 3s infinite ease-in-out;
  -webkit-animation: spinPulse 3s infinite ease-in-out;
}
.innerCircle {
  background-color: transparent;
  border: 5px solid rgba(189, 215, 60, 0.6);
  opacity: 0.9;
  border-left: 5px solid transparent;
  border-right: 5px solid transparent;
  border-radius: 100px;
  top: -100px;
  width: 92px;
  height: 92px;
  margin: 0 auto;
  position: relative;
  -moz-animation: spinoffPulse 1s infinite linear;
  -webkit-animation: spinoffPulse 1s infinite linear;
}

@-moz-keyframes spinPulse {
  0% {
    -moz-transform: rotate(160deg);
    opacity: 0;
    box-shadow: 0 0 1px #bdd73c;
  }
  50% {
    -moz-transform: rotate(145deg);
    opacity: 1;
  }
  100% {
    -moz-transform: rotate(-320deg);
    opacity: 0;
  }
}
@-moz-keyframes spinoffPulse {
  0% {
    -moz-transform: rotate(0deg);
  }
  100% {
    -moz-transform: rotate(360deg);
  }
}
@-webkit-keyframes spinPulse {
  0% {
    -webkit-transform: rotate(160deg);
    opacity: 0;
    box-shadow: 0 0 1px #bdd73c;
  }
  50% {
    -webkit-transform: rotate(145deg);
    opacity: 1;
  }
  100% {
    -webkit-transform: rotate(-320deg);
    opacity: 0;
  }
}
@-webkit-keyframes spinoffPulse {
  0% {
    -webkit-transform: rotate(0deg);
  }
  100% {
    -webkit-transform: rotate(360deg);
  }
}
</style>

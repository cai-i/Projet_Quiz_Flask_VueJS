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
          </div>

<!-- Les deux boutons pour clean les variables -->
          <div class="flex flex-col gap-4">
            <button
              class="flex place-content-center items-center gap-4 w-36 h-16 item-center rounded-xl bg-red-700 hover:bg-red-800 text-white"
              @click="this.restartGame();"
            >
              <!-- <svg
                xmlns="http://www.w3.org/2000/svg"
                viewBox="0 0 20 20"
                fill="currentColor"
                class="w-5 h-5 "
              >
                <path
                  fill-rule="evenodd"
                  d="M2 10a8 8 0 1116 0 8 8 0 01-16 0zm6.39-2.908a.75.75 0 01.766.027l3.5 2.25a.75.75 0 010 1.262l-3.5 2.25A.75.75 0 018 12.25v-4.5a.75.75 0 01.39-.658z"
                  clip-rule="evenodd"
                />
              </svg> -->

              Rejouer !
            </button>

            <button
              class="flex place-content-center items-center gap-4 w-36 h-16 item-center rounded-xl bg-red-700 hover:bg-red-800 text-white"
              @click="this.$router.push('/')"
            >
              <!-- <svg
                xmlns="http://www.w3.org/2000/svg"
                viewBox="0 0 20 20"
                fill="currentColor"
                class="w-5 h-5"
              >
                <path
                  fill-rule="evenodd"
                  d="M9.293 2.293a1 1 0 011.414 0l7 7A1 1 0 0117 11h-1v6a1 1 0 01-1 1h-2a1 1 0 01-1-1v-3a1 1 0 00-1-1H9a1 1 0 00-1 1v3a1 1 0 01-1 1H5a1 1 0 01-1-1v-6H3a1 1 0 01-.707-1.707l7-7z"
                  clip-rule="evenodd"
                />
              </svg> -->
              Accueil
            </button>
          </div>
        </div>
      </div>

      <div v-else class="p-8 pt-24">
        <!-- Loading animation elements -->
        <div class="outerCircle"></div>
        <div class="innerCircle"></div>
        <div class="icon"></div>
      </div>

      <!-- Tableau de isa-->
      <div class="w-full mb-12">
        <div
          class="relative flex flex-col min-w-0 break-words w-full mb-6 shadow-lg bg-red-700 text-white font-bold"
        >
          <!-- fond du tableau -->
          <div class="ScorePageBody absolute inset-0"></div>
          <div class="w-full backdrop-blur">
            <!-- titre du tableau -->
            <div class="rounded-t mb-0 px-4 py-3 bg-black bg-opacity-50">
              <div class="items-center relative w-full px-4 max-w-full">
                <h3 class="font-semibold text-3xl text-white text-center">
                  Scores des Top Participants
                </h3>
              </div>
            </div>

            <!-- composition du tableau -->
            <div class="block w-full overflow-x-auto">
              <table class="items-center w-full bg-transparent border-collapse">
                <thead class="flex text-white w-full">
                  <!-- noms des colonnes du tableau -->
                  <tr class="flex w-full mb-2 bg-red-800 text-red-400 text-xl">
                    <th
                      class="px-6 py-3 ml-6 border font-semibold border-l-0 border-r-0 border-red-900"
                      style="width: 95px"
                    >
                      Rang
                    </th>
                    <th
                      class="px-6 py-3 ml-2 border font-semibold border-l-0 border-r-0 border-red-900"
                      style="width: 250px"
                    >
                      Nom d'utilisateur
                    </th>
                    <th
                      class="px-6 py-3 ml-10 border font-semibold border-l-0 border-r-0 border-red-900"
                      style="width: 150px"
                    >
                      Score
                    </th>
                    <th
                      class="px-6 py-3 border font-semibold border-l-0 border-r-0 border-red-900"
                      style="width: 250px"
                    >
                      Taux de réussite
                    </th>
                    <th
                      class="px-6 py-3 ml-28 border font-semibold border-l-0 border-r-0 border-red-900"
                    >
                      Date de soumission
                    </th>
                  </tr>
                </thead>
                <!-- affiche les élements dans le tableau de scores -->
                <tbody
                  class="flex flex-col items-center justify-between overflow-y-scroll w-full"
                  style="height: 70vh"
                >
                  <!-- tbody class="bg-grey-light flex flex-col items-center justify-between overflow-y-scroll w-full" -->
                  <template
                    v-for="(scoreEntry, rank) in registeredScores"
                    v-bind:key="scoreEntry.date"
                  >
                    <tr class="flex w-full mb-4 items-center text-xl">
                      <td class="px-6 py-2 ml-10" style="width: 95px">
                        {{ rank + 1 }}
                      </td>
                      <td class="px-6 py-2 flex items-center">
                        <img
                          src="https://media.istockphoto.com/id/1300845620/vector/user-icon-flat-isolated-on-white-background-user-symbol-vector-illustration.jpg?s=170667a&w=0&k=20&c=bsbD0qLFJ6fSUCXG_iyo7JBnmKi6T-uUblC8FNZFJoU="
                          class="h-12 w-12 bg-white rounded-full border"
                          alt="..."
                        />
                        <span
                          class="ml-3 font-bold text-white text-xl"
                          style="width: 200px"
                        >
                          {{ scoreEntry.playerName }}
                        </span>
                      </td>
                      <td class="px-6 py-2 ml-6" style="width: 80px">
                        {{ scoreEntry.score }}
                      </td>
                      <td class="px-6 py-2" style="width: 380px">
                        <div class="flex items-center">
                          <span class="mr-2 text-xl">
                            {{ successRate(scoreEntry.score) }}
                          </span>
                          <span class="mr-2 text-xl"> % </span>
                          <div class="relative w-full">
                            <div
                              class="overflow-hidden h-2 text-xs flex rounded bg-red-200"
                            >
                              <div
                                class="h-full progressbar bg-yellow-500"
                                :style="{ width: `${rate}%` }"
                              ></div>
                            </div>
                          </div>
                        </div>
                      </td>
                      <td class="px-14 py-2" style="width: 410px">
                        {{ scoreEntry.date }}
                      </td>
                    </tr>
                  </template>
                </tbody>
              </table>
            </div>
          </div>
        </div>
      </div>
    </div>
  </div>
</template>

<script>
import quizApiService from "@/services/QuizApiService";
import participationStorageService from "@/services/ParticipationStorageService";

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
      this.userName = participationStorageService.clear();
      this.$router.push("/start-new-quiz-page");
    },
  },
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

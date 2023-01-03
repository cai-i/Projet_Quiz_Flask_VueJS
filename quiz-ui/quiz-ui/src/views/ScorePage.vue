<template>

  <div class="bg-neutral-300">
    <div class="hover:animate-pulse p-4 block text-3xl text-center">
      <p>
        Score de {{ this.userName }} : {{ this.userScore }} /
        {{ nbr_questions }}
      </p>
      <p>
        Vous êtes au rang : {{ this.userRank }} /
        {{ this.registeredScores.length }}
      </p>

      <!--message pour le joueur-->
      <div class="mt-4">
        <p v-if="this.userRank < this.registeredScores.length / 3">
          Bravo, sentez vous supérieur à
          {{ this.registeredScores.length - this.userRank }}
          personnes aujourd'hui !
        </p>

        <p v-if="this.userRank > (this.registeredScores.length * 2) / 3">
          Bravo, vous vous êtes fait DE-FON-CE.E !
        </p>

        <p
          v-if="
            this.userRank >= this.registeredScores.length / 3 &&
            this.userRank <= (this.registeredScores.length * 2) / 3
          "
        >
          Bof, dans la moyenne... ouf ? (OvO)
        </p>
      </div>
    </div>


      <div class="container">
        <div class="row">
            <div class="col-md-3 col-sm-6">
                <div class="progress cent"
                :class="[this.userScore===100 ? 'text-green-700' : this.userScore>50 ? 'text-yellow-700' : 'text-red-700']">
                    <span class="progress-left">
                        <span class="progress-bar"></span>
                    </span>
                    <span class="progress-right">
                        <span class="progress-bar"></span>
                    </span>
                    <div class="progress-value">
                      <div v-if="100*this.userScore/nbr_questions"> 
                      {{100*this.userScore/nbr_questions}}%
                      </div>                      
                      <div v-else> 
                      ???
                      </div>
                    </div>
                </div>
            </div>
        </div>
      </div>

    <!-- Tableau de isa-->
    <div class="w-full mb-12 px-12">
      <div
        class="relative flex flex-col min-w-0 break-words w-full mb-6 shadow-lg rounded bg-red-700 text-pink-800 font-bold"
      >
        <!-- fond du tableau -->
        <div
          class="absolute inset-0 bg-cover bg-center bg-no-repeat bg-fixed"
          style="
            background-image: url(https://wallpaper.dog/large/5459726.jpg);
          "
        ></div>
        <div class="w-full backdrop-blur">
          <!-- titre du tableau -->
          <div class="rounded-t mb-0 px-4 py-3 bg-black bg-opacity-50">
            <div class="items-center relative w-full px-4 max-w-full">
              <h3 class="font-semibold text-3xl text-white text-center">
                Scores des Top participants (puis du reste)
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
    };
  },
  async created() {
    console.log(quizApiService.getQuizInfo());
    var quizInfoPromise = quizApiService.getQuizInfo();
    var quizInfoApiResult = await quizInfoPromise;
    this.registeredScores = quizInfoApiResult.data.scores;
    this.nbr_questions = quizInfoApiResult.data.size;

    this.userName = participationStorageService.getPlayerName();
    this.userScore = participationStorageService.getParticipationScore();
    console.log(this.userScore);
    for (var scoreEntry in this.registeredScores) {
      if (
        this.registeredScores[scoreEntry].playerName === this.userName &&
        this.registeredScores[scoreEntry].score == this.userScore
      )
        this.userRank = parseInt(scoreEntry) + 1;
    }
    console.log("Composant Score page 'created'");
  },
  methods: {
    successRate: function (value) {
      this.rate = String((value * 100) / this.nbr_questions);
      return this.rate;
    },
  },
};
</script>

<style scoped>

.progress{
    background: none;
    margin: 0 auto;
    box-shadow: none;
    width: 150px;
    height: 150px;
    line-height: 150px;
    position: relative;
}
.progress:after{
    content: "";
    border-radius: 50%;
    border: 15px solid #f2f5f5;
    position: absolute;
    width: 100%;
    height: 100%;
    top: 0;
    left: 0;
}
.progress > span{
    position: absolute;
    top: 0;
    z-index: 1;
    width: 50%;
    height: 100%;
    overflow: hidden;
}
.progress .progress-bar{
    border-width: 15px;
    border-style: solid;
    position: absolute;
    width: 100%;
    height: 100%;
    background: none;
    top: 0;
}
.progress .progress-left{
    left: 0;
}
.progress .progress-left .progress-bar{
    left: 100%;
    border-top-right-radius: 80px;
    border-bottom-right-radius: 80px;
    border-left: 0;
    -webkit-transform-origin: center left;
    transform-origin: center left;
}
.progress .progress-right{
    right: 0;
}
.progress .progress-right .progress-bar{
    left: -100%;
    border-top-left-radius: 80px;
    border-bottom-left-radius: 80px;
    border-right: 0;
    -webkit-transform-origin: center right;
    transform-origin: center right;
}
.progress .progress-value{
    font-size: 34px;
    font-weight: bold;
    text-align: center;
    width: 100%;
    height: 100%;
    position: absolute;
}

@keyframes loading-1{
    0%{
        -webkit-transform: rotate(0deg);
        transform: rotate(0deg);
        border-color:red;
    }
    50%{
        -webkit-transform: rotate(180deg);
        transform: rotate(180deg);
        border-color:red;
    }
    55%, 60%, 70%, 80%, 90% {
        -webkit-transform: rotate(180deg);
        transform: rotate(180deg);
        border-color: orange;
    }
    98%{
        -webkit-transform: rotate(180deg);
        transform: rotate(180deg);
        border-color: orange;
    }
    100%{
        -webkit-transform: rotate(180deg);
        transform: rotate(180deg);
        border-color: green;
    }
}
@keyframes loading-2{
    0%{
        -webkit-transform: rotate(0deg);
        transform: rotate(0deg);
        border-color: red;
    }
    10%{
        -webkit-transform: rotate(18deg);
        transform: rotate(18deg);
        border-color: orange;
    }
    95%{
        -webkit-transform: rotate(171deg);
        transform: rotate(171deg);
        border-color: orange;
    }
    100%{
        -webkit-transform: rotate(180deg);
        transform: rotate(180deg);
        border-color: green;
    }
}

.progress.cent .progress-right .progress-bar{
    animation: loading-1 2s linear forwards ;
    /*animation-play-state: paused;*/
}
.progress.cent .progress-left .progress-bar{
    animation: loading-2 1s linear forwards 1s;
    /*animation-play-state: paused;*/
}

.progress.stop .progress-left .progress-bar{
    animation-play-state: running;
}

/*
.progress.qvd .progress-right .progress-bar{
    animation: loading-1 2s linear forwards ;
}
.progress.qvd .progress-left .progress-bar{
    animation: loading-2 1s linear forwards 1s;
}

.progress.qv .progress-right .progress-bar{
    animation: loading-1 2s linear forwards ;
}
.progress.qv .progress-left .progress-bar{
    animation: loading-2 1s linear forwards;
}
.progress.sxd .progress-right .progress-bar{
    animation: loading-1 2s linear forwards ;
}
.progress.sxd .progress-left .progress-bar{
    animation: loading-2 1s linear forwards 1s;
}

.progress.sxt .progress-right .progress-bar{
    animation: loading-1 2s linear forwards ;
}
.progress.sxt .progress-left .progress-bar{
    animation: loading-2 1s linear forwards 1s;
}

.progress.cqt .progress-right .progress-bar{
    animation: loading-1 2s 4s linear forwards ;
}

.progress.qrt .progress-right .progress-bar{
    animation: loading-1 2s linear forwards ;
}

.progress.trt .progress-right .progress-bar{
    animation: loading-1 2s linear forwards ;
}

.progress.vgt .progress-right .progress-bar{
    animation: loading-1 2s linear forwards ;
}

.progress.dix .progress-right .progress-bar{
    animation: loading-1 2s linear forwards ;
}
*/

</style>
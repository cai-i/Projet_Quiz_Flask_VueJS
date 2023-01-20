<template>
  <div class="relative flex flex-col min-w-0 break-words w-full mb-6 shadow-lg rounded text-white">
    <!-- fond du tableau -->
    <slot></slot>
    <!-- vrai contenu tableau (ps:floute le fond pour mieux voir les écritures) -->
    <div class="w-full backdrop-blur">
      <!-- titre du tableau -->
      <div class="relative w-full px-7 py-3">
        <h3 class="my-3 font-semibold text-3xl">
          Scores des participants
        </h3>
        <p class="text-xl"> Nombre de participants : {{nbr_participants}} </p>
      </div>
      <!-- composition du tableau -->
      <div class="block w-full overflow-x-auto">
        <table class="table-auto items-center w-full bg-transparent border-collapse">
          <!-- noms des colonnes du tableau -->
          <thead class="flex w-full">
            <tr class="flex w-full mb-2 py-4 items-center bg-gray-800/80 text-xl border border-black">
              <th class="ml-11 font-semibold" style="width: 95px;">
                Rang
              </th>
              <th class="font-semibold" style="width: 250px;">
                Nom d'utilisateur
              </th>
              <th class="font-semibold" style="width: 150px;">
                Score
              </th>
              <th class="font-semibold" style="width: 352px;">
                Taux de réussite
              </th>
              <th class="font-semibold"  style="width: 300px;">
                Date de soumission
              </th>
            </tr>
          </thead>
          <!-- affiche les élements dans le tableau de scores -->
          <tbody v-if="registeredScores.length===0" class="text-white text-center">
            <p class="py-7 text-xl"> 
              Malheureusement il n'y a pas encore de joueur, mais soyez le premier à nous impressionner !
            </p>
          </tbody>
          <tbody v-selse class="flex flex-col items-center justify-between overflow-y-auto w-full max-h-[520px]">
            <!-- boucle dans la liste des participants -->
            <template
              v-for="scoreEntry in registeredScores"
              v-bind:key="scoreEntry.date"
            >
              <tr class="flex w-full py-3 items-center text-xl text-center">
                <!-- rang -->
                <td class="ml-11" style="width: 95px;">
                  {{get_rank(scoreEntry.reussite, position)}}
                </td>
                <!-- nom du joueur -->
                <td class="px-6 flex items-center text-left" style="width:250px;">
                  <img
                    src="https://media.istockphoto.com/id/1300845620/vector/user-icon-flat-isolated-on-white-background-user-symbol-vector-illustration.jpg?s=170667a&w=0&k=20&c=bsbD0qLFJ6fSUCXG_iyo7JBnmKi6T-uUblC8FNZFJoU="
                    class="h-12 w-12 bg-white rounded-full border"
                    alt="..."
                  />
                  <span class="ml-3 text-xl font-bold" style="width:202px;">
                    {{ scoreEntry.playerName }} 
                  </span>
                </td>
                <!-- score -->
                <td style="width: 150px;">
                  {{ scoreEntry.score }}
                </td>
                <!-- pourcentage de réussite -->
                <td class="px-6 flex items-centers" style="width: 80px;">
                  <p class="mr-2">
                    {{scoreEntry.reussite}}
                  </p>
                  <p class="mr-2">
                    %
                  </p>
                </td>
                <!-- barre de progression -->
                <td class="px-3">
                  <div style="width: 250px;">
                    <div class="relative w-full">
                      <div class="overflow-hidden h-2 text-xs flex rounded bg-red-200">
                        <div
                          class="h-full progressbar bg-yellow-500"
                          :style="{width: `${String(set_reussite(scoreEntry.reussite))}%`}"
                        >
                        </div>
                      </div>
                    </div>
                  </div>
                </td>
                <td class="text-center" style="width: 300px;">
                  {{ scoreEntry.date }}
                </td>
              </tr>
            </template>
          </tbody>
        </table>
      </div>
    </div>
  </div>
</template>

<script>

import quizApiService from "@/services/QuizApiService";

export default {
  name: "ScoresTable",
  data() {
    return {
      registeredScores: [],
      currentReussite: 0,
      rank:1,
      nbr_participants:0,
      nbr_questions: 0,
    };
  },
  // récupère les scores des participants depuis l'API
  async created() {
    console.log(quizApiService.getQuizInfo());
    var quizInfoPromise = quizApiService.getQuizInfo();
    var quizInfoApiResult = await quizInfoPromise;
    this.registeredScores = quizInfoApiResult.data.scores;
    this.currentReussite = this.registeredScores[0].reussite;
    this.nbr_participants = this.registeredScores.length;
    this.nbr_questions = quizInfoApiResult.data.size;
    console.log("Composant Home page 'created'"); 
  },
  methods : {
    set_reussite: function(reussite) {
      this.currentReussite = reussite
      return this.currentReussite 
    },
    get_rank: function(reussite) {
      if (reussite != this.currentReussite) {
        this.rank = this.rank + 1
      }
      return this.rank
    }
  }
}
</script>
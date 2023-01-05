<template>
  <div class="relative flex flex-col min-w-0 break-words w-full mb-6 shadow-lg rounded text-white">
    <!-- fond du tableau -->
    <slot></slot>
    <!-- floute le fond pour mieux voir les écritures -->
    <div class="w-full backdrop-blur">
      <!-- titre du tableau -->
      <div class="relative w-full px-7 py-3 max-w-full flex-grow flex-1">
        <h3 class="my-3 font-semibold text-3xl">
          Scores des participants
        </h3>
        <p class="text-xl"> Nombre de participants : {{nbr_participants}} </p>
      </div>
      <!-- composition du tableau -->
      <div class="block w-full overflow-x-auto">
        <table class="items-center w-full bg-transparent border-collapse">
          <!-- noms des colonnes du tableau -->
          <thead class="flex w-full">
            <tr class="flex w-full mb-2 bg-red-800 text-red-400 text-xl">
              <th class="px-6 py-3 ml-8 border font-semibold border-l-0 border-r-0 border-red-900" style="width: 95px;">
                Rang
              </th>
              <th class="px-6 py-3 ml-2 border font-semibold border-l-0 border-r-0 border-red-900" style="width: 250px;">
                Nom d'utilisateur
              </th>
              <th class="px-6 py-3 ml-1 border font-semibold border-l-0 border-r-0 border-red-900" style="width: 150px;">
                Score
              </th>
              <th class="px-6 py-3 ml-8 border font-semibold border-l-0 border-r-0 border-red-900" style="width: 250px;">
                Taux de réussite
              </th>
              <th class="px-6 py-3 ml-[90px] border font-semibold border-l-0 border-r-0 border-red-700">
                Date de soumission
              </th>
            </tr>
          </thead>
          <!-- affiche les élements dans le tableau de scores -->
          <tbody class="flex flex-col items-center justify-between overflow-y-scroll w-full" style="height: 70vh;">
            <!-- boucle dans la liste des participants -->
            <template
              v-for="(scoreEntry, rank) in registeredScores"
              v-bind:key="scoreEntry.date"
            >
              <tr class="flex w-full mb-4 items-center text-xl">
                <!-- rang -->
                <td class="px-6 py-2 ml-12 content-center rounded-full" style="width: 95px;">
                  {{ rank + 1 }}
                </td>
                <!-- nom du joueur -->
                <td class="px-6 py-2 flex items-center">
                  <img
                    src="https://media.istockphoto.com/id/1300845620/vector/user-icon-flat-isolated-on-white-background-user-symbol-vector-illustration.jpg?s=170667a&w=0&k=20&c=bsbD0qLFJ6fSUCXG_iyo7JBnmKi6T-uUblC8FNZFJoU="
                    class="h-12 w-12 bg-white rounded-full border"
                    alt="..."
                  />
                  <span class="ml-3 text-xl font-bold" style="width: 170px;">
                    {{ scoreEntry.playerName }}
                  </span>
                </td>
                <!-- score -->
                <td class="px-6 py-2 ml-6" style="width: 80px;">
                  {{ scoreEntry.score }}
                </td>
                <!-- pourcentage de réussite -->
                <td class="px-6 py-2" style="width: 380px;">
                  <div class="flex items-center">
                    <p class="mr-2">
                      {{successRate(scoreEntry.score)}}
                    </p>
                    <p class="mr-2">
                      %
                    </p>
                    <!-- barre de progression -->
                    <div class="relative w-full">
                      <div class="overflow-hidden h-2 text-xs flex rounded bg-red-200">
                        <div
                          class="h-full progressbar bg-yellow-500"
                          :style="{width: `${rate}%`}"
                        >
                        </div>
                      </div>
                    </div>
                  </div>
                </td>
                <td class="px-14 py-2" style="width: 380px;">
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
      nbr_participants:0,
      nbr_questions: 0,
      rate: ''
    };
  },
  // récupère les scores des participants depuis l'API
  async created() {
    console.log(quizApiService.getQuizInfo());
    var quizInfoPromise = quizApiService.getQuizInfo();
    var quizInfoApiResult = await quizInfoPromise;
    this.registeredScores = quizInfoApiResult.data.scores;
    this.nbr_participants = this.registeredScores.length;
    this.nbr_questions = quizInfoApiResult.data.size;
    console.log("Composant Home page 'created'"); 
  },
  methods: {
    // pour obtenir le taux de réussite d'un participant
    successRate: function(value){
      this.rate= String(value*100/this.nbr_questions)
      return this.rate
    }
  },
}
</script>
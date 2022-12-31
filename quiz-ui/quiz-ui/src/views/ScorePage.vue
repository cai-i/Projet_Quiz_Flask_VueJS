<template>
  <link
    rel="stylesheet"
    href="https://demos.creative-tim.com/notus-js/assets/styles/tailwind.css"
  />
  <link
    rel="stylesheet"
    href="https://demos.creative-tim.com/notus-js/assets/vendor/@fortawesome/fontawesome-free/css/all.min.css"
  />

  <div class="m-4 block text-3xl text-center">
    <p>
      Score de {{ this.userName }} : {{ this.userScore }} / {{ nbr_questions }}
    </p>
    <p>Your rank is {{ this.userRank }} / {{ this.registeredScores.length }}</p>
  </div>

  <div class="w-full mb-12 px-4">
    <div
      class="relative flex flex-col min-w-0 break-words w-full mb-6 shadow-lg rounded bg-red-700 text-white"
    >
      <div
        class="absolute inset-0 bg-cover bg-center bg-no-repeat bg-fixed"
        style="
          background-image: url(https://www.racv.com.au/content/dam/racv/images/content-hub/lifestyle/entertainment-and-events/festivals-and-events/calendar-events/chinese-new-year/900x600GettyImages-1125854093.jpg);
        "
      ></div>
      <div class="w-full backdrop-blur">
        <div class="rounded-t mb-0 px-4 py-3 border-0">
          <div class="flex flex-wrap items-center">
            <div class="relative w-full px-4 max-w-full flex-grow flex-1">
              <h3 class="font-semibold text-3xl text-white">
                Scores des Top 10 participants
              </h3>
            </div>
          </div>
        </div>
        <div class="block w-full overflow-x-auto">
          <table class="items-center w-full bg-transparent border-collapse">
            <thead>
              <tr>
                <th
                  class="px-6 align-middle border border-solid py-3 text-xl border-l-0 border-r-0 whitespace-nowrap font-semibold text-left bg-red-800 text-red-400 border-red-900"
                >
                  Rang
                </th>
                <th
                  class="px-6 align-middle border border-solid py-3 text-xl border-l-0 border-r-0 whitespace-nowrap font-semibold text-left bg-red-800 text-red-400 border-red-900"
                >
                  Nom du participant
                </th>
                <th
                  class="px-6 align-middle border border-solid py-3 text-xl border-l-0 border-r-0 whitespace-nowrap font-semibold text-left bg-red-800 text-red-400 border-red-900"
                >
                  Score
                </th>
                <th
                  class="px-6 align-middle border border-solid py-3 text-xl border-l-0 border-r-0 whitespace-nowrap font-semibold text-left bg-red-800 text-red-400 border-red-900"
                >
                  Taux de réussite
                </th>
                <th
                  class="px-6 align-middle border border-solid py-3 text-xl border-l-0 border-r-0 whitespace-nowrap font-semibold text-left bg-red-800 text-red-400 border-red-900"
                >
                  Date de soumission
                </th>
              </tr>
            </thead>

            <tbody>
              <template
                v-for="scoreEntry in registeredScores.slice(1, 11)"
                v-bind:key="scoreEntry.date"
              >
                <tr>
                  <td
                    class="border-t-0 px-6 align-middle border-l-0 border-r-0 text-xs whitespace-nowrap p-4 text-xl"
                  >
                    {{ registeredScores.slice(1, 11).indexOf(scoreEntry) + 1 }}
                  </td>
                  <td
                    class="border-t-0 px-6 align-middle border-l-0 border-r-0 text-xs whitespace-nowrap p-4 text-left flex items-center"
                  >
                    <img
                      src="https://demos.creative-tim.com/notus-js/assets/img/bootstrap.jpg"
                      class="h-12 w-12 bg-white rounded-full border"
                      alt="..."
                    />
                    <span class="ml-3 font-bold text-white text-xl">
                      {{ scoreEntry.playerName }}
                    </span>
                  </td>
                  <td
                    class="border-t-0 px-6 align-middle border-l-0 border-r-0 text-xs whitespace-nowrap p-4 text-xl"
                  >
                    {{ scoreEntry.score }}
                  </td>
                  <td
                    class="border-t-0 px-6 align-middle border-l-0 border-r-0 text-xs whitespace-nowrap p-4"
                  >
                    <div class="flex items-center">
                      <span class="mr-2 text-xl">
                        {{ (scoreEntry.score * 100) / nbr_questions }}
                      </span>
                      <div class="relative w-full">
                        <div
                          class="overflow-hidden h-2 text-xs flex rounded bg-red-200"
                        >
                          <div
                            style="width: 10%"
                            class="shadow-none flex flex-col text-center whitespace-nowrap text-white justify-center bg-red-500"
                          ></div>
                        </div>
                      </div>
                    </div>
                  </td>
                  <td
                    class="border-t-0 px-6 align-middle border-l-0 border-r-0 text-xs whitespace-nowrap p-4 text-xl"
                  >
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
    for (var scoreEntry in this.registeredScores) {
      if (
        this.registeredScores[scoreEntry].playerName === this.userName &&
        this.registeredScores[scoreEntry].score == this.userScore
      )
        this.userRank = parseInt(scoreEntry) + 1;
    }
    console.log("Composant Score page 'created'");
  },
};
</script>

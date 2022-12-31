<template>
  <link
    rel="stylesheet"
    href="https://demos.creative-tim.com/notus-js/assets/styles/tailwind.css"
  />
  <link
    rel="stylesheet"
    href="https://demos.creative-tim.com/notus-js/assets/vendor/@fortawesome/fontawesome-free/css/all.min.css"
  />

  <section class="relative py-11 px-3 bg-orange-100">
    <a class="text-5xl flex items-center py-1 px-7">
      <svg
        class="w-12 h-12 mr-2 text-red-700"
        xmlns="http://www.w3.org/2000/svg"
        fill="none"
        viewBox="0 0 24 24"
        stroke-width="1.5"
        stroke="currentColor"
      >
        <path
          stroke-linecap="round"
          stroke-linejoin="round"
          d="M2.25 12l8.954-8.955c.44-.439 1.152-.439 1.591 0L21.75 12M4.5 9.75v10.125c0 .621.504 1.125 1.125 1.125H9.75v-4.875c0-.621.504-1.125 1.125-1.125h2.25c.621 0 1.125.504 1.125 1.125V21h4.125c.621 0 1.125-.504 1.125-1.125V9.75M8.25 21h8.25"
        />
      </svg>
      <span class="font-bold text-red-700">Page d'accueil</span>
    </a>
    <div class="px-12 py-8">
      <p>
        Bienvenue sur notre site dans lequel vous allez pouvoir retrouver un
        quiz qui testera l'étendue de vos connaissances sur la culture Chinoise.
      </p>
      <p>
        Saurez-vous vous démarquer par rapport aux autres participants ayant
        déjà testé les limites de leurs connaissances sur la culture Chinoise ?
      </p>
      <p>Un seul moyen de le savoir, faire le tester également !</p>
      <p>Qu'attendez-vous ?</p>
      <p>
        PS : n'hésitez pas à challenger vos amis également en leur envoyant le
        lien de ce quiz
      </p>
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
                  Scores des participants
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
                  v-for="scoreEntry in registeredScores"
                  v-bind:key="scoreEntry.date"
                >
                  <tr>
                    <td
                      class="border-t-0 px-6 align-middle border-l-0 border-r-0 text-xs whitespace-nowrap p-4 text-xl"
                    >
                      {{ rank++ }}
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
    <footer class="relative pt-8 pb-6 mt-8">
      <div class="container mx-auto px-4">
        <div
          class="flex flex-wrap items-center md:justify-between justify-center"
        >
          <div class="w-full md:w-6/12 px-4 mx-auto text-center">
            <div class="text-sm text-blueGray-500 font-semibold py-1">
              Made with
              <a
                href="https://www.creative-tim.com/product/notus-js"
                class="text-blueGray-500 hover:text-gray-800"
                target="_blank"
                >Notus JS</a
              >
              by
              <a
                href="https://www.creative-tim.com"
                class="text-blueGray-500 hover:text-blueGray-800"
                target="_blank"
              >
                Creative Tim</a
              >.
            </div>
          </div>
        </div>
      </div>
    </footer>
  </section>
</template>

<script>
import quizApiService from "@/services/QuizApiService";
import participationStorageService from "@/services/ParticipationStorageService";

export default {
  name: "HomePage",
  data() {
    return {
      registeredScores: [],
      nbr_questions: 0,
      rank: 1,
    };
  },
  async created() {
    console.log(quizApiService.getQuizInfo());
    var quizInfoPromise = quizApiService.getQuizInfo();
    var quizInfoApiResult = await quizInfoPromise;
    this.registeredScores = quizInfoApiResult.data.scores;
    this.nbr_questions = quizInfoApiResult.data.size;
    console.log("Composant Home page 'created'");
  },
  increment_rank() {
    this.rank++;
  },
};
</script>

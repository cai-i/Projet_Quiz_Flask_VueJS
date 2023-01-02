<template>
  <link
    rel="stylesheet"
    href="https://demos.creative-tim.com/notus-js/assets/styles/tailwind.css"
  />
  <link
    rel="stylesheet"
    href="https://demos.creative-tim.com/notus-js/assets/vendor/@fortawesome/fontawesome-free/css/all.min.css"
  />

  <section class="relative py-11 px-12 bg-orange-100 h-full">
    <!-- titre de la page -->
    <a class="w-5/6 mx-auto text-5xl flex items-center py-1 px-7">
      <!-- icon maison -->
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
      <!-- titre text -->
      <span class="font-bold text-red-700">Page d'accueil</span>
    </a>
    <!-- carte de présentation -->
    <div class="flex min-h-screeen items-center justify-center py-5">
      <div class="mx-auto max-w-6xl px-6">
        <div class="flex [&:hover>div]:w-16 [&>div:hover]:w-[25rem]">
          <!-- 1ère image (qu'on voit au complet) -->
          <div class="group relative shadow-lg shadow-black/30 h-96 w-[23rem] cursor-pointer overflow-hidden transition-all duration-200">
            <img class="h-full object-cover group-hover:rotate-12 group-hover:scale-125 transition-all" src="https://img.freepik.com/free-vector/chinese-japanese-bamboo-grass-oriental-wallpaper-tropical-asian-plant-background_1284-53253.jpg?w=2000"/>
            <div class="invisible absolute inset-0 bg-gradient-to-b from-green-500/20 to-black group-hover:visible">
              <div class="absolute inset-x-5 bottom-6">
                <div class="flew gap-3 text-white">
                  <svg xmlns="http://www.w3.org/2000/svg" fill="none" viewBox="0 0 24 24" stroke-width="1.5" stroke="currentColor" class="w-6 h-6">
                    <path stroke-linecap="round" stroke-linejoin="round" d="M12 21v-8.25M15.75 21v-8.25M8.25 21v-8.25M3 9l9-6 9 6m-1.5 12V10.332A48.36 48.36 0 0012 9.75c-2.551 0-5.056.2-7.5.582V21M3 21h18M12 6.75h.008v.008H12V6.75z" />
                  </svg>
                  <div>
                    <p class="font-semibold text-xl text-gray-100">
                      Beyond Builder
                    </p>
                    <p class="text-gray-300">
                      Better Design
                    </p>
                  </div>
                </div>
                <div class="flex justify-end gap-3 text-gray-200">
                  <svg xmlns="http://www.w3.org/2000/svg" fill="none" viewBox="0 0 24 24" stroke-width="1.5" stroke="currentColor" class="w-6 h-6">
                    <path stroke-linecap="round" stroke-linejoin="round" d="M9 12.75L11.25 15 15 9.75M21 12c0 1.268-.63 2.39-1.593 3.068a3.745 3.745 0 01-1.043 3.296 3.745 3.745 0 01-3.296 1.043A3.745 3.745 0 0112 21c-1.268 0-2.39-.63-3.068-1.593a3.746 3.746 0 01-3.296-1.043 3.745 3.745 0 01-1.043-3.296A3.745 3.745 0 013 12c0-1.268.63-2.39 1.593-3.068a3.745 3.745 0 011.043-3.296 3.746 3.746 0 013.296-1.043A3.746 3.746 0 0112 3c1.268 0 2.39.63 3.068 1.593a3.746 3.746 0 013.296 1.043 3.746 3.746 0 011.043 3.296A3.745 3.745 0 0121 12z" />
                  </svg>
                  <svg xmlns="http://www.w3.org/2000/svg" fill="none" viewBox="0 0 24 24" stroke-width="1.5" stroke="currentColor" class="w-6 h-6">
                    <path stroke-linecap="round" stroke-linejoin="round" d="M11.25 4.5l7.5 7.5-7.5 7.5m-6-15l7.5 7.5-7.5 7.5" />
                  </svg>
                </div>
              </div>
            </div>
          </div>
          <!-- 2ère image -->
          <div class="group relative shadow-lg shadow-black/30 h-96 w-16 cursor-pointer overflow-hidden transition-all duration-200">
            <img class="h-full object-cover group-hover:rotate-12 group-hover:scale-125 transition-all" src="https://img.freepik.com/free-vector/seamless-pattern-with-chinese-new-year-zodiac-year-ox-sign-with-asian-elements_38689-995.jpg?w=2000"/>
            <div class="invisible absolute inset-0 bg-gradient-to-b from-green-500/20 to-black group-hover:visible">
              <div class="absolute inset-x-5 bottom-6">
                <div class="flew gap-3 text-white">
                  <svg xmlns="http://www.w3.org/2000/svg" fill="none" viewBox="0 0 24 24" stroke-width="1.5" stroke="currentColor" class="w-6 h-6">
                    <path stroke-linecap="round" stroke-linejoin="round" d="M12 21v-8.25M15.75 21v-8.25M8.25 21v-8.25M3 9l9-6 9 6m-1.5 12V10.332A48.36 48.36 0 0012 9.75c-2.551 0-5.056.2-7.5.582V21M3 21h18M12 6.75h.008v.008H12V6.75z" />
                  </svg>
                  <div>
                    <p class="font-semibold text-xl text-gray-100">
                      Beyond Builder
                    </p>
                    <p class="text-gray-300">
                      Better Design
                    </p>
                  </div>
                </div>
                <div class="flex justify-end gap-3 text-gray-200">
                  <svg xmlns="http://www.w3.org/2000/svg" fill="none" viewBox="0 0 24 24" stroke-width="1.5" stroke="currentColor" class="w-6 h-6">
                    <path stroke-linecap="round" stroke-linejoin="round" d="M9 12.75L11.25 15 15 9.75M21 12c0 1.268-.63 2.39-1.593 3.068a3.745 3.745 0 01-1.043 3.296 3.745 3.745 0 01-3.296 1.043A3.745 3.745 0 0112 21c-1.268 0-2.39-.63-3.068-1.593a3.746 3.746 0 01-3.296-1.043 3.745 3.745 0 01-1.043-3.296A3.745 3.745 0 013 12c0-1.268.63-2.39 1.593-3.068a3.745 3.745 0 011.043-3.296 3.746 3.746 0 013.296-1.043A3.746 3.746 0 0112 3c1.268 0 2.39.63 3.068 1.593a3.746 3.746 0 013.296 1.043 3.746 3.746 0 011.043 3.296A3.745 3.745 0 0121 12z" />
                  </svg>
                  <svg xmlns="http://www.w3.org/2000/svg" fill="none" viewBox="0 0 24 24" stroke-width="1.5" stroke="currentColor" class="w-6 h-6">
                    <path stroke-linecap="round" stroke-linejoin="round" d="M11.25 4.5l7.5 7.5-7.5 7.5m-6-15l7.5 7.5-7.5 7.5" />
                  </svg>
                </div>
              </div>
            </div>
          </div>
          <!-- 3ère image -->
          <div class="group relative shadow-lg shadow-black/30 h-96 w-16 cursor-pointer overflow-hidden transition-all duration-200">
            <img class="h-full object-cover group-hover:rotate-12 group-hover:scale-125 transition-all" src="https://img.freepik.com/free-vector/chinese-japanese-bamboo-grass-oriental-wallpaper-tropical-asian-plant-background_1284-53253.jpg?w=2000"/>
            <div class="invisible absolute inset-0 bg-gradient-to-b from-green-500/20 to-black group-hover:visible">
              <div class="absolute inset-x-5 bottom-6">
                <div class="flew gap-3 text-white">
                  <svg xmlns="http://www.w3.org/2000/svg" fill="none" viewBox="0 0 24 24" stroke-width="1.5" stroke="currentColor" class="w-6 h-6">
                    <path stroke-linecap="round" stroke-linejoin="round" d="M12 21v-8.25M15.75 21v-8.25M8.25 21v-8.25M3 9l9-6 9 6m-1.5 12V10.332A48.36 48.36 0 0012 9.75c-2.551 0-5.056.2-7.5.582V21M3 21h18M12 6.75h.008v.008H12V6.75z" />
                  </svg>
                  <div>
                    <p class="font-semibold text-xl text-gray-100">
                      Beyond Builder
                    </p>
                    <p class="text-gray-300">
                      Better Design
                    </p>
                  </div>
                </div>
                <div class="flex justify-end gap-3 text-gray-200">
                  <svg xmlns="http://www.w3.org/2000/svg" fill="none" viewBox="0 0 24 24" stroke-width="1.5" stroke="currentColor" class="w-6 h-6">
                    <path stroke-linecap="round" stroke-linejoin="round" d="M9 12.75L11.25 15 15 9.75M21 12c0 1.268-.63 2.39-1.593 3.068a3.745 3.745 0 01-1.043 3.296 3.745 3.745 0 01-3.296 1.043A3.745 3.745 0 0112 21c-1.268 0-2.39-.63-3.068-1.593a3.746 3.746 0 01-3.296-1.043 3.745 3.745 0 01-1.043-3.296A3.745 3.745 0 013 12c0-1.268.63-2.39 1.593-3.068a3.745 3.745 0 011.043-3.296 3.746 3.746 0 013.296-1.043A3.746 3.746 0 0112 3c1.268 0 2.39.63 3.068 1.593a3.746 3.746 0 013.296 1.043 3.746 3.746 0 011.043 3.296A3.745 3.745 0 0121 12z" />
                  </svg>
                  <svg xmlns="http://www.w3.org/2000/svg" fill="none" viewBox="0 0 24 24" stroke-width="1.5" stroke="currentColor" class="w-6 h-6">
                    <path stroke-linecap="round" stroke-linejoin="round" d="M11.25 4.5l7.5 7.5-7.5 7.5m-6-15l7.5 7.5-7.5 7.5" />
                  </svg>
                </div>
              </div>
            </div>
          </div>
        </div>
      </div>
    </div>
    <!-- paragraphes de présentation -->
    <div class="w-5/6 mx-auto px-12 py-8">
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
    <div class="w-5/6 mx-auto mb-12 px-12">
      <div class="relative flex flex-col min-w-0 break-words w-full mb-6 shadow-lg rounded bg-red-700 text-white">
        <!-- fond du tableau -->
        <div
          class="absolute inset-0 bg-cover bg-center bg-no-repeat bg-fixed"
          style="background-image: url(https://www.racv.com.au/content/dam/racv/images/content-hub/lifestyle/entertainment-and-events/festivals-and-events/calendar-events/chinese-new-year/900x600GettyImages-1125854093.jpg);"
        ></div>
        <div class="w-full backdrop-blur">
          <!-- titre du tableau -->
          <div class="rounded-t mb-0 px-4 py-3 border-0">
            <div class="flex flex-wrap items-center">
              <div class="relative w-full px-4 max-w-full flex-grow flex-1">
                <h3 class="font-semibold text-3xl text-white">
                  Scores des participants
                </h3>
              </div>
            </div>
          </div>
          <!-- composition du tableau -->
          <div class="block w-full overflow-x-auto">
            <table class="items-center w-full bg-transparent border-collapse">
              <thead class="flex text-white w-full">
                <!-- noms des colonnes du tableau -->
                <tr class="flex w-full mb-2 bg-red-800 text-red-400 text-xl">
                  <th class="px-6 py-3 ml-6 border font-semibold border-l-0 border-r-0 border-red-900" style="width: 95px;">
                    Rang
                  </th>
                  <th class="px-6 py-3 ml-2 border font-semibold border-l-0 border-r-0 border-red-900" style="width: 250px;">
                    Nom d'utilisateur
                  </th>
                  <th class="px-6 py-3 ml-10 border font-semibold border-l-0 border-r-0 border-red-900" style="width: 150px;">
                    Score
                  </th>
                  <th class="px-6 py-3 border font-semibold border-l-0 border-r-0 border-red-900" style="width: 250px;">
                    Taux de réussite
                  </th>
                  <th class="px-6 py-3 ml-28 border font-semibold border-l-0 border-r-0 border-red-900">
                    Date de soumission
                  </th>
                </tr>
              </thead>
              <!-- affiche les élements dans le tableau de scores -->
              <tbody class="flex flex-col items-center justify-between overflow-y-scroll w-full" style="height: 70vh;">                <!-- tbody class="bg-grey-light flex flex-col items-center justify-between overflow-y-scroll w-full" -->
                <template
                  v-for="(scoreEntry, rank) in registeredScores"
                  v-bind:key="scoreEntry.date"
                >
                  <tr class="flex w-full mb-4 items-center text-xl">
                    <td class="px-6 py-2 ml-10" style="width: 95px;">
                      {{ rank + 1 }}
                    </td>
                    <td class="px-6 py-2 flex items-center">
                      <img
                        src="https://media.istockphoto.com/id/1300845620/vector/user-icon-flat-isolated-on-white-background-user-symbol-vector-illustration.jpg?s=170667a&w=0&k=20&c=bsbD0qLFJ6fSUCXG_iyo7JBnmKi6T-uUblC8FNZFJoU="
                        class="h-12 w-12 bg-white rounded-full border"
                        alt="..."
                      />
                      <span class="ml-3 font-bold text-white text-xl" style="width: 200px;">
                        {{ scoreEntry.playerName }}
                      </span>
                    </td>
                    <td class="px-6 py-2 ml-6" style="width: 80px;">
                      {{ scoreEntry.score }}
                    </td>
                    <td class="px-6 py-2" style="width: 380px;">
                      <div class="flex items-center">
                        <span class="mr-2 text-xl">
                          {{successRate(scoreEntry.score)}}
                        </span>
                        <span class="mr-2 text-xl">
                          %
                        </span>
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
                    <td class="px-14 py-2" style="width: 410px;">
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
      rate: ''
    };
  },
  // récupère les scores des participants depuis l'API'
  async created() {
    console.log(quizApiService.getQuizInfo());
    var quizInfoPromise = quizApiService.getQuizInfo();
    var quizInfoApiResult = await quizInfoPromise;
    this.registeredScores = quizInfoApiResult.data.scores;
    this.nbr_questions = quizInfoApiResult.data.size;
    console.log("Composant Home page 'created'"); 
  },
  methods: {
    successRate: function(value){
      this.rate= String(value*100/this.nbr_questions)
      return this.rate
    }
  }
};
</script>

<template>
  <link
    rel="stylesheet"
    href="https://demos.creative-tim.com/notus-js/assets/styles/tailwind.css"
  />
  <link
    rel="stylesheet"
    href="https://demos.creative-tim.com/notus-js/assets/vendor/@fortawesome/fontawesome-free/css/all.min.css"
  />

  <section class="bg-orange-100 h-full">
    <div class="w-5/6 mx-auto py-11">
      <!-- titre de la page -->
      <a class="text-5xl flex items-center py-1 px-7">
        <!-- icon maison -->
        <svg class="w-12 h-12 mr-2 text-red-700" xmlns="http://www.w3.org/2000/svg" fill="none" viewBox="0 0 24 24" stroke-width="1.5" stroke="currentColor">
          <path stroke-linecap="round" stroke-linejoin="round" d="M2.25 12l8.954-8.955c.44-.439 1.152-.439 1.591 0L21.75 12M4.5 9.75v10.125c0 .621.504 1.125 1.125 1.125H9.75v-4.875c0-.621.504-1.125 1.125-1.125h2.25c.621 0 1.125.504 1.125 1.125V21h4.125c.621 0 1.125-.504 1.125-1.125V9.75M8.25 21h8.25"/>
        </svg>
        <!-- titre text -->
        <span class="font-bold text-red-700">Page d'accueil</span>
      </a>
      <!-- carte de présentation -->
      <div class="flex min-h-screeen items-center m-6">
        <div class="mx-auto max-w-6xl">
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
                      <h1 class="font-semibold text-xl text-gray-100">
                        欢迎
                      </h1>
                      <button data-tooltip-target="tooltip-animation" type="button" class="text-white bg-blue-700 hover:bg-blue-800 focus:ring-4 focus:outline-none focus:ring-blue-300 font-medium rounded-lg text-sm px-5 py-2.5 text-center dark:bg-blue-600 dark:hover:bg-blue-700 dark:focus:ring-blue-800">Animated tooltip</button>
                      <div id="tooltip-animation" role="tooltip" class="inline-block absolute invisible z-10 py-2 px-3 text-sm font-medium text-white bg-gray-900 rounded-lg shadow-sm opacity-0 transition-opacity duration-300 tooltip dark:bg-gray-700">
                          Tooltip content
                          <div class="tooltip-arrow" data-popper-arrow></div>
                      </div>
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

      <div class="mb-12">
        <div class="relative flex flex-col min-w-0 break-words w-full mb-6 shadow-lg rounded bg-red-700 text-white">
          <!-- fond du tableau -->
          <div
            class="absolute inset-0 bg-cover bg-center bg-no-repeat bg-fixed"
            style="background-image: url(https://www.racv.com.au/content/dam/racv/images/content-hub/lifestyle/entertainment-and-events/festivals-and-events/calendar-events/chinese-new-year/900x600GettyImages-1125854093.jpg);"
          ></div>
          <div class="w-full backdrop-blur">
            <!-- titre du tableau -->
            <div class="mb-0 px-8 py-3">
                <h3 class="font-semibold text-3xl text-white">
                  Scores des participants
                </h3>
            </div>
            <!-- composition du tableau -->
            <div class="block w-full overflow-x-auto">
              <table class="items-center bg-transparent border-collapse">
                <thead>
                  <!-- noms des colonnes du tableau -->
                  <tr class="grid grid-cols-12 py-3 mb-3 bg-red-800 border-red-900 border text-red-400 text-xl">
                    <th class="col-span-1 font-semibold">Rang</th>
                    <th class="col-span-2 font-semibold">Nom d'utilisateur</th>
                    <th class="col-span-2 font-semibold">Score</th>
                    <th class="col-span-3 font-semibold">Taux de réussite</th>
                    <th class="col-span-4 font-semibold ">Date de soumission</th>
                  </tr>
                </thead>

                <!-- affiche les élements dans le tableau de scores -->
                <tbody class="items-center overflow-y-scroll w-full">                <!-- tbody class="bg-grey-light flex flex-col items-center justify-between overflow-y-scroll w-full" -->
                  <template
                    v-for="(scoreEntry, rank) in registeredScores"
                    v-bind:key="scoreEntry.date"
                  >
                    <tr class="grid grid-cols-12 gap-4 mx-2 mb-4 items-center text-xl">
                      <td class="col-span-1 flex place-content-center">
                        {{ rank + 1 }}
                      </td>

                      <td class="col-span-2 ml-8 flex place-content-center items-center">
                        <img
                          src="https://media.istockphoto.com/id/1300845620/vector/user-icon-flat-isolated-on-white-background-user-symbol-vector-illustration.jpg?s=170667a&w=0&k=20&c=bsbD0qLFJ6fSUCXG_iyo7JBnmKi6T-uUblC8FNZFJoU="
                          class="h-12 w-12 bg-white rounded-full border"
                        />
                        <span class="ml-3 font-bold text-white text-xl" style="width: 200px;">
                          {{ scoreEntry.playerName }}
                        </span>
                      </td>

                      <td class="col-span-2 flex place-content-center">
                        {{ scoreEntry.score }}
                      </td> 

                      <td class="col-span-4 grid grid-cols-10">
                        <div class="col-span-2 items-center">
                          <span class="mr-2 text-xl">
                            {{successRate(scoreEntry.score)}}
                          </span>
                            %
                        </div>
                          <div class="col-span-6 relative w-full">
                            <div class="mt-3 overflow-hidden h-2 text-xs flex rounded bg-red-200">
                              <div
                                class="h-full progressbar bg-yellow-500"
                                :style="{width: `${this.rate}%`}"
                              >
                              </div>
                            </div>
                        </div>
                      </td>

                      <td class="col-span-3 ml-2">
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
  </section>
</template>

<script>
import quizApiService from "@/services/QuizApiService";

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
        successRate(value) {
          this.rate= String(value*100/this.nbr_questions)
          return this.rate;
        }
    }
};
</script>

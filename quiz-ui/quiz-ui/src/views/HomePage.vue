<template>
  <link
    rel="stylesheet"
    href="https://demos.creative-tim.com/notus-js/assets/styles/tailwind.css"
  />
  <link
    rel="stylesheet"
    href="https://demos.creative-tim.com/notus-js/assets/vendor/@fortawesome/fontawesome-free/css/all.min.css"
  />

  <section class="py-11 bg-orange-100 h-full">
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
    <!-- cartes de présentation : carousel -->
    <div id="carousel" class="carousel slide w-5/6 mx-auto py-7 relative" data-bs-ride="carousel">
      <!-- bouton en dessous pour passer d'une slide à l'autre -->
      <div class="carousel-indicators absolute right-0 bottom-14 left-0 flex justify-center p-0 mb-4">
        <button type="button" data-bs-target="#carousel" data-bs-slide-to="0" class="active" aria-current="true" aria-label="Slide 1"></button>
        <button type="button" data-bs-target="#carousel" data-bs-slide-to="1" aria-label="Slide 2" ></button>
        <button type="button" data-bs-target="#carousel" data-bs-slide-to="2" aria-label="Slide 3" ></button>
        <button type="button" data-bs-target="#carousel" data-bs-slide-to="3" aria-label="Slide 4" ></button>
      </div>
      <!-- bouton précédent -->
      <button class="carousel-control-prev absolute top-0 bottom-0 left-0 flex items-center justify-center text-center border-0 hover:outline-none hover:no-underline focus:outline-none focus:no-underline" type="button" data-bs-target="#carousel" data-bs-slide="prev">
        <span class="carousel-control-prev-icon inline-block bg-no-repeat" aria-hidden="true"></span>
        <span class="visually-hidden">Previous</span>
      </button>
      <!-- bouton suivant -->
      <button class="carousel-control-next absolute top-0 bottom-0 right-0 flex items-center justify-center text-center border-0 hover:outline-none hover:no-underline focus:outline-none focus:no-underline" type="button" data-bs-target="#carousel" data-bs-slide="next" >
        <span class="carousel-control-next-icon inline-block bg-no-repeat" aria-hidden="true"></span>
        <span class="visually-hidden">Next</span>
      </button>
      <!-- contenu du carousel -->
      <div class="carousel-inner relative h-[600px] items-center overflow-hidden">
        <!-- 1ère slide -->
        <div class="carousel-item active relative float-left items-center w-full">
          <img class="block object-cover h-[600px] w-full" src="https://live.staticflickr.com/5554/14615975852_eeb8f169f1_b.jpg"/>
          <div class="carousel-caption absolute bottom-0 h-[600px] left-0 right-0 bg-gradient-to-b from-white/10 to-black/80"></div>
          <div class="carousel-caption block absolute text-center bottom-14">
            <h5 class="text-3xl mb-3">欢迎! Welcome! Bienvenue !</h5>
            <p>
              Bienvenue sur notre site dans lequel vous allez pouvoir retrouver un
              quiz qui testera l'étendue de vos connaissances sur la culture Chinoise.
            </p>
          </div>
          <!-- liens image + licence -->
          <div class="absolute bottom-2 right-0 left-0 flex justify-center text-white">
            <div class="flex items-center opacity-50 hover:opacity-100">
              <svg xmlns="http://www.w3.org/2000/svg" fill="none" viewBox="0 0 24 24" stroke-width="1.5" stroke="currentColor" class="w-6 h-6">
                <path stroke-linecap="round" stroke-linejoin="round" d="M2.25 15.75l5.159-5.159a2.25 2.25 0 013.182 0l5.159 5.159m-1.5-1.5l1.409-1.409a2.25 2.25 0 013.182 0l2.909 2.909m-18 3.75h16.5a1.5 1.5 0 001.5-1.5V6a1.5 1.5 0 00-1.5-1.5H3.75A1.5 1.5 0 002.25 6v12a1.5 1.5 0 001.5 1.5zm10.5-11.25h.008v.008h-.008V8.25zm.375 0a.375.375 0 11-.75 0 .375.375 0 01.75 0z" />
              </svg>
              <a class="py-1 px-1 hover:underline" href="https://www.flickr.com/photos/seeminglee/14615975852">
                image
              </a>
            </div>
            <div class="flex items-center opacity-50 hover:opacity-100">
              <svg xmlns="http://www.w3.org/2000/svg" fill="none" viewBox="0 0 24 24" stroke-width="1.5" stroke="currentColor" class="w-6 h-6">
                <path stroke-linecap="round" stroke-linejoin="round" d="M19.5 14.25v-2.625a3.375 3.375 0 00-3.375-3.375h-1.5A1.125 1.125 0 0113.5 7.125v-1.5a3.375 3.375 0 00-3.375-3.375H8.25m0 12.75h7.5m-7.5 3H12M10.5 2.25H5.625c-.621 0-1.125.504-1.125 1.125v17.25c0 .621.504 1.125 1.125 1.125h12.75c.621 0 1.125-.504 1.125-1.125V11.25a9 9 0 00-9-9z" />
              </svg>
              <a class="py-1 px-1 hover:underline" href="https://creativecommons.org/licenses/by-nc/2.0/">
                licence
              </a>
            </div>
          </div>
        </div>
        <!-- 2ème slide -->
        <div class="carousel-item relative float-left items-center w-full">
          <img class="block object-cover h-[600px] w-full" src="https://www.cwa-ni.org/wp-content/uploads/2021/02/Hero_Stefano_Borghi_IMG_3706_Hi.jpg"/>
          <div class="carousel-caption absolute bottom-0 h-[600px] left-0 right-0 bg-gradient-to-b from-white/10 to-black/80"></div>
          <div class="carousel-caption block absolute text-center bottom-14">
            <h5 class="text-3xl mb-3">Montrez nous vos capacités et challengez vous !</h5>
            <p>
              Saurez-vous vous démarquer par rapport aux autres participants ayant
              déjà testé les limites de leurs connaissances sur la culture Chinoise ?
            </p>
          </div>
          <!-- liens image + licence -->
          <div class="absolute bottom-2 right-0 left-0 flex justify-center text-white">
            <div class="flex items-center opacity-50 hover:opacity-100">
              <svg xmlns="http://www.w3.org/2000/svg" fill="none" viewBox="0 0 24 24" stroke-width="1.5" stroke="currentColor" class="w-6 h-6">
                <path stroke-linecap="round" stroke-linejoin="round" d="M2.25 15.75l5.159-5.159a2.25 2.25 0 013.182 0l5.159 5.159m-1.5-1.5l1.409-1.409a2.25 2.25 0 013.182 0l2.909 2.909m-18 3.75h16.5a1.5 1.5 0 001.5-1.5V6a1.5 1.5 0 00-1.5-1.5H3.75A1.5 1.5 0 002.25 6v12a1.5 1.5 0 001.5 1.5zm10.5-11.25h.008v.008h-.008V8.25zm.375 0a.375.375 0 11-.75 0 .375.375 0 01.75 0z" />
              </svg>
              <a class="py-1 px-1 hover:underline" href="https://www.cwa-ni.org/history-of-chinese-new-year/">
                image
              </a>
            </div>
            <div class="flex items-center opacity-50 hover:opacity-100">
              <svg xmlns="http://www.w3.org/2000/svg" fill="none" viewBox="0 0 24 24" stroke-width="1.5" stroke="currentColor" class="w-6 h-6">
                <path stroke-linecap="round" stroke-linejoin="round" d="M19.5 14.25v-2.625a3.375 3.375 0 00-3.375-3.375h-1.5A1.125 1.125 0 0113.5 7.125v-1.5a3.375 3.375 0 00-3.375-3.375H8.25m0 12.75h7.5m-7.5 3H12M10.5 2.25H5.625c-.621 0-1.125.504-1.125 1.125v17.25c0 .621.504 1.125 1.125 1.125h12.75c.621 0 1.125-.504 1.125-1.125V11.25a9 9 0 00-9-9z" />
              </svg>
              <a class="py-1 px-1 hover:underline" href="https://creativecommons.org/licenses/by-nc-nd/4.0/deed.fr">
                licence
              </a>
            </div>
          </div>
        </div>
        <!-- 3ème slide -->
        <div class="carousel-item relative float-left items-center w-full">
          <img class="block object-cover h-[600px] w-full" src="https://upload.wikimedia.org/wikipedia/commons/d/d5/Mid-Autumn_Festival-beijing.jpg"/>
          <div class="carousel-caption absolute bottom-0 h-[600px] left-0 right-0 bg-gradient-to-b from-white/10 to-black/80"></div>
          <div class= "flex space-x-2 mb-2 absolute top-36 left-0 right-9 justify-center rounded-full">
            <RouterLink to="/start-new-quiz-page" tag='div'>
              <svg class="w-44 h-44 text-red-600 animate-pulse" xmlns="http://www.w3.org/2000/svg" fill="none" viewBox="0 0 24 24" stroke-width="1.5" stroke="currentColor">
                <path stroke-linecap="round" stroke-linejoin="round" d="M15.362 5.214A8.252 8.252 0 0112 21 8.25 8.25 0 016.038 7.048 8.287 8.287 0 009 9.6a8.983 8.983 0 013.361-6.867 8.21 8.21 0 003 2.48z" />
                <path stroke-linecap="round" stroke-linejoin="round" d="M12 18a3.75 3.75 0 00.495-7.467 5.99 5.99 0 00-1.925 3.546 5.974 5.974 0 01-2.133-1A3.75 3.75 0 0012 18z" />
              </svg>
            </RouterLink>
          </div>
          <div class="carousel-caption block absolute text-center bottom-14">
            <h5 class="text-3xl mb-3">Pour participer, c'est par ici !</h5>
            <p>Quoi de mieux pour répondre à la question précédente que de faire le quiz également !</p>
            <p>Qu'attendez-vous ? Cliquez vite sur la flamme juste au-dessus avant que les dragons ne le fasse disparaître !</p>
          </div>
          <!-- liens image + licence -->
          <div class="absolute bottom-2 right-0 left-0 flex justify-center text-white">
            <div class="flex items-center opacity-50 hover:opacity-100">
              <svg xmlns="http://www.w3.org/2000/svg" fill="none" viewBox="0 0 24 24" stroke-width="1.5" stroke="currentColor" class="w-6 h-6">
                <path stroke-linecap="round" stroke-linejoin="round" d="M2.25 15.75l5.159-5.159a2.25 2.25 0 013.182 0l5.159 5.159m-1.5-1.5l1.409-1.409a2.25 2.25 0 013.182 0l2.909 2.909m-18 3.75h16.5a1.5 1.5 0 001.5-1.5V6a1.5 1.5 0 00-1.5-1.5H3.75A1.5 1.5 0 002.25 6v12a1.5 1.5 0 001.5 1.5zm10.5-11.25h.008v.008h-.008V8.25zm.375 0a.375.375 0 11-.75 0 .375.375 0 01.75 0z" />
              </svg>
              <a class="py-1 px-1 hover:underline" href="https://commons.wikimedia.org/wiki/File:Mid-Autumn_Festival-beijing.jpg">
                image
              </a>
            </div>
            <div class="flex items-center opacity-50 hover:opacity-100">
              <svg xmlns="http://www.w3.org/2000/svg" fill="none" viewBox="0 0 24 24" stroke-width="1.5" stroke="currentColor" class="w-6 h-6">
                <path stroke-linecap="round" stroke-linejoin="round" d="M19.5 14.25v-2.625a3.375 3.375 0 00-3.375-3.375h-1.5A1.125 1.125 0 0113.5 7.125v-1.5a3.375 3.375 0 00-3.375-3.375H8.25m0 12.75h7.5m-7.5 3H12M10.5 2.25H5.625c-.621 0-1.125.504-1.125 1.125v17.25c0 .621.504 1.125 1.125 1.125h12.75c.621 0 1.125-.504 1.125-1.125V11.25a9 9 0 00-9-9z" />
              </svg>
              <a class="py-1 px-1 hover:underline" href="https://creativecommons.org/licenses/by-sa/2.5/">
                licence
              </a>
            </div>
          </div>
        </div>
        <!-- 4ème slide -->
        <div class="carousel-item relative float-left items-center w-full">
          <img class="block object-cover h-[600px] w-full" src="https://upload.wikimedia.org/wikipedia/commons/3/36/China-Shanghai-YuGarden-the_Lantern_Festival-2012_1828.JPG"/>
          <div class="carousel-caption absolute bottom-0 h-[600px] left-0 right-0 bg-gradient-to-b from-white/10 to-black/80"></div>
          <div class="carousel-caption block absolute text-center bottom-14">
            <h5 class="text-3xl mb-3">Plus on est de fou, plus on rit ! </h5>
            <p>
              N'hésitez pas à challenger vos amis également en leur envoyant le
              lien de ce quiz
            </p>
          </div>
          <!-- liens image + licence -->
          <div class="absolute bottom-2 right-0 left-0 flex justify-center text-white">
            <div class="flex items-center opacity-50 hover:opacity-100">
              <svg xmlns="http://www.w3.org/2000/svg" fill="none" viewBox="0 0 24 24" stroke-width="1.5" stroke="currentColor" class="w-6 h-6">
                <path stroke-linecap="round" stroke-linejoin="round" d="M2.25 15.75l5.159-5.159a2.25 2.25 0 013.182 0l5.159 5.159m-1.5-1.5l1.409-1.409a2.25 2.25 0 013.182 0l2.909 2.909m-18 3.75h16.5a1.5 1.5 0 001.5-1.5V6a1.5 1.5 0 00-1.5-1.5H3.75A1.5 1.5 0 002.25 6v12a1.5 1.5 0 001.5 1.5zm10.5-11.25h.008v.008h-.008V8.25zm.375 0a.375.375 0 11-.75 0 .375.375 0 01.75 0z" />
              </svg>
              <a class="py-1 px-1 hover:underline" href="https://commons.wikimedia.org/wiki/File:China-Shanghai-YuGarden-the_Lantern_Festival-2012_1828.JPG">
                image
              </a>
            </div>
            <div class="flex items-center opacity-50 hover:opacity-100">
              <svg xmlns="http://www.w3.org/2000/svg" fill="none" viewBox="0 0 24 24" stroke-width="1.5" stroke="currentColor" class="w-6 h-6">
                <path stroke-linecap="round" stroke-linejoin="round" d="M19.5 14.25v-2.625a3.375 3.375 0 00-3.375-3.375h-1.5A1.125 1.125 0 0113.5 7.125v-1.5a3.375 3.375 0 00-3.375-3.375H8.25m0 12.75h7.5m-7.5 3H12M10.5 2.25H5.625c-.621 0-1.125.504-1.125 1.125v17.25c0 .621.504 1.125 1.125 1.125h12.75c.621 0 1.125-.504 1.125-1.125V11.25a9 9 0 00-9-9z" />
              </svg>
              <a class="py-1 px-1 hover:underline" href="https://creativecommons.org/licenses/by-sa/3.0/">
                licence
              </a>
            </div>
          </div>
        </div>
      </div>
    </div>
    <!-- transition encore le carousel et le tableau des scores -->
    <div class="w-5/6 mx-auto my-8 text-3xl text-center">
      <p> 
        Vous voulez savoir comment les autres se sont débrouillés ? 
      </p>
      <p> 
        Découvrez le classement des meilleurs joueurs juste en dessous ! 
      </p>
      <div class="flex justify-center items-center mt-7">
        <svg class="w-12 h-12 animate-bounce text-yellow-400" xmlns="http://www.w3.org/2000/svg" fill="none" viewBox="0 0 24 24" stroke-width="1.5" stroke="currentColor">
          <path stroke-linecap="round" stroke-linejoin="round" d="M9 12.75l3 3m0 0l3-3m-3 3v-7.5M21 12a9 9 0 11-18 0 9 9 0 0118 0z" />
        </svg>
      </div>
    </div>
    <!-- Début tableau -->
    <div class="w-5/6 mx-auto mb-12">
      <div class="relative flex flex-col min-w-0 break-words w-full mb-6 shadow-lg rounded bg-red-700 text-white">
        <!-- fond du tableau -->
        <div
          class="absolute inset-0 bg-cover bg-center bg-no-repeat bg-fixed"
          style="background-image: url(https://upload.wikimedia.org/wikipedia/commons/c/cc/Celebration_Chinese_Lantern_Festival.jpg);"
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
                  <th class="px-6 py-3 ml-3 border font-semibold border-l-0 border-r-0 border-red-900" style="width: 95px;">
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
                  <th class="px-6 py-3 ml-[108px] border font-semibold border-l-0 border-r-0 border-red-700">
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
                  <tr class="flex w-full mb-4 items-center text-xl font-bold">
                    <td class="px-6 py-2 ml-6 rounded-full" style="width: 95px;">
                      {{ rank + 1 }}
                    </td>
                    <td class="px-6 py-2 flex items-center">
                      <img
                        src="https://media.istockphoto.com/id/1300845620/vector/user-icon-flat-isolated-on-white-background-user-symbol-vector-illustration.jpg?s=170667a&w=0&k=20&c=bsbD0qLFJ6fSUCXG_iyo7JBnmKi6T-uUblC8FNZFJoU="
                        class="h-12 w-12 bg-white rounded-full border"
                        alt="..."
                      />
                      <span class="ml-3 text-white text-xl" style="width: 200px;">
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
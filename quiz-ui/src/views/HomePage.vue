<template>
  <NavBar></NavBar>
  <section class="py-11 bg-orange-100 h-full">
    <div class="w-5/6 mx-auto">
      <!-- titre de la page -->
      <a class="text-5xl flex items-center py-1 px-7">
        <!-- icon maison -->
        <svg class="w-12 h-12 mr-2 text-red-700" xmlns="http://www.w3.org/2000/svg" fill="none" viewBox="0 0 24 24" stroke-width="1.5" stroke="currentColor">
          <path stroke-linecap="round" stroke-linejoin="round" d="M2.25 12l8.954-8.955c.44-.439 1.152-.439 1.591 0L21.75 12M4.5 9.75v10.125c0 .621.504 1.125 1.125 1.125H9.75v-4.875c0-.621.504-1.125 1.125-1.125h2.25c.621 0 1.125.504 1.125 1.125V21h4.125c.621 0 1.125-.504 1.125-1.125V9.75M8.25 21h8.25"/>
        </svg>
        <!-- titre -->
        <span class="font-bold text-red-700">Page d'accueil</span>
      </a>
      <!-- cartes de présentation du site : carousel -->
      <div id="carousel" class="carousel slide py-7 relative" data-bs-ride="carousel">
        <!-- boutons en dessous pour passer d'une slide à l'autre -->
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
            <CarouselSlide
                backgroundImageURL="https://live.staticflickr.com/5554/14615975852_eeb8f169f1_b.jpg" 
                title="欢迎! Welcome! Bienvenue !"
                imageURL="https://www.flickr.com/photos/seeminglee/14615975852"
                licenseURL="https://creativecommons.org/licenses/by-nc/2.0/"
            >
              <template #paragraphes>
                <p>
                  Bienvenue sur notre site dans lequel vous allez pouvoir retrouver un
                  quiz qui testera l'étendue de vos connaissances sur la culture Chinoise.
                </p>
              </template>
            </CarouselSlide>
          </div>
          <!-- 2ème slide -->
          <div class="carousel-item relative float-left items-center w-full">
            <CarouselSlide
                backgroundImageURL="https://www.cwa-ni.org/wp-content/uploads/2021/02/Hero_Stefano_Borghi_IMG_3706_Hi.jpg" 
                title="Montrez nous vos capacités et challengez vous !"
                imageURL="https://www.cwa-ni.org/history-of-chinese-new-year/"
                licenseURL="https://creativecommons.org/licenses/by-nc-nd/4.0/deed.fr"
            >
              <template #paragraphes>
                <p>
                  Saurez-vous vous démarquer par rapport aux autres participants ayant
                  déjà testé les limites de leurs connaissances sur la culture Chinoise ?
                </p>
              </template>
            </CarouselSlide>
          </div>
          <!-- 3ème slide -->
          <div class="carousel-item relative float-left items-center w-full">
            <CarouselSlide
                backgroundImageURL="https://upload.wikimedia.org/wikipedia/commons/d/d5/Mid-Autumn_Festival-beijing.jpg" 
                title="Pour participer, c'est par ici !"
                imageURL="https://commons.wikimedia.org/wiki/File:Mid-Autumn_Festival-beijing.jpg"
                licenseURL="https://creativecommons.org/licenses/by-sa/2.5/"
            >
              <template #fireButton>
                <div class= "flex absolute left-0 right-8 bottom-56 items-center justify-center rounded-full">
                  <RouterLink to="/start-new-quiz-page" tag='div'>
                    <svg class="w-44 h-44 text-red-600 animate-pulse" xmlns="http://www.w3.org/2000/svg" fill="none" viewBox="0 0 24 24" stroke-width="1.5" stroke="currentColor">
                      <path stroke-linecap="round" stroke-linejoin="round" d="M15.362 5.214A8.252 8.252 0 0112 21 8.25 8.25 0 016.038 7.048 8.287 8.287 0 009 9.6a8.983 8.983 0 013.361-6.867 8.21 8.21 0 003 2.48z" />
                      <path stroke-linecap="round" stroke-linejoin="round" d="M12 18a3.75 3.75 0 00.495-7.467 5.99 5.99 0 00-1.925 3.546 5.974 5.974 0 01-2.133-1A3.75 3.75 0 0012 18z" />
                    </svg>
                  </RouterLink>
                </div>
              </template>
              <template #paragraphes>
                <p>Quoi de mieux pour avoir un aperçu de vos connaissance que de faire le quiz sur la Culture Chinoise !</p>
                <p>Qu'attendez-vous ? Cliquez vite sur la flamme juste au-dessus avant que les dragons ne le fassent disparaître !</p>
              </template>
            </CarouselSlide>
          </div>
          <!-- 4ème slide -->
          <div class="carousel-item relative float-left items-center w-full">
            <CarouselSlide
                backgroundImageURL="https://upload.wikimedia.org/wikipedia/commons/3/36/China-Shanghai-YuGarden-the_Lantern_Festival-2012_1828.JPG" 
                title="Plus on est de fou, plus on rit !"
                imageURL="https://commons.wikimedia.org/wiki/File:China-Shanghai-YuGarden-the_Lantern_Festival-2012_1828.JPG"
                licenseURL="https://creativecommons.org/licenses/by-sa/3.0/"
            >
              <template #paragraphes>
                <p>
                  N'hésitez pas à challenger vos amis également en leur envoyant le
                  lien de ce quiz
                </p>
              </template>
            </CarouselSlide>
          </div>
        </div>
      </div>
      <!-- transition encore le carousel et le tableau des scores -->
      <div class="my-8 text-3xl text-center">
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
      <ScoresTable>
        <!-- image de fond du tableau -->
        <div
          class="absolute inset-0 bg-cover bg-center bg-no-repeat bg-fixed"
          style="background-image: url('https://upload.wikimedia.org/wikipedia/commons/c/cc/Celebration_Chinese_Lantern_Festival.jpg');"
        ></div>
      </ScoresTable>
    </div>
  </section>
</template>

<script>
import NavBar from './Components/NavBar.vue';
import CarouselSlide from './Components/CarouselSlide.vue';
import ScoresTable from './Components/ScoresTable.vue';

export default {
  name: "HomePage",
  components: { NavBar, CarouselSlide, ScoresTable }
};

</script>
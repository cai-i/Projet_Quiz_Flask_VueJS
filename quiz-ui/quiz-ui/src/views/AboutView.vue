<template>
  <div class="about">
    <h1 class="text-3xl font-bold text-amber-400">Qui sommes-nous ?</h1>
    <!-- carte de présentation -->
    <div class="flex items-center justify-center bg-transparent">
      <!-- taille de la carte -->
      <div class="group h-96 w-96 [perspective:1000px]">
        <div class="relative h-full w-full rounded-xl shadow-xl transition-all duration-500 [transform-style:preserve-3d] group-hover:[transform:rotateY(180deg)]">
          <div class="absolute inset-0">
            <img class="h-full w-full rounded-xl object-cover shadow-xl shadow-black/40" src="https://i.pinimg.com/736x/fb/ce/4e/fbce4ed45362cb18bd1bcd7ae4060b74.jpg"/>
          </div>
          <div class="absolute inset-0 h-full w-full rounded-xl bg-black/80 px-12 text-center text-slate-200 [transform:rotateY(180deg)] [backface-visibility:hidden]">
            <div class="flex min-h-full flex-col items-center justify-center">
              <h1 class="text-3xl font-bold">Welcome!</h1>
              <p class="text-lg"> Bienvenue sur notre site</p>
              <p class="text-base"> 
                Si vous êtes là, c'est que la culture chinoise doit vous 
                intéresser un minimum n'est-ce pas ? 
              </p>
              <button class="mt-2 rounded-md bg-neutral-800 py-1 px-2 text-sm hover:bg-neutral-900">
                Read More
              </button>
            </div>
          </div>
        </div>
      </div>
    </div>
    <p>
      Trifecta is a Team of 3 bad bitches who encountered one another in engineering school.
      If love at first sight is real, then the opposite phenomenon would be the perfect 
      description of the emotions whispered by their guts at first glance. Since then, 
      they just try not to kill each other every single day.
    </p>
  </div>
</template>

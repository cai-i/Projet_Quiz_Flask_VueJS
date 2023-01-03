<template>
  <section class="py-11 bg-orange-100 h-full">
    <!-- titre de la page -->
    <a class="w-5/6 mx-auto text-5xl flex items-center py-1 px-7">
      <!-- icon maison -->
      <svg class="w-12 h-12 mr-2 text-red-700" xmlns="http://www.w3.org/2000/svg" fill="none" viewBox="0 0 24 24" stroke-width="1.5" stroke="currentColor">
        <path stroke-linecap="round" stroke-linejoin="round" d="M2.25 21h19.5m-18-18v18m10.5-18v18m6-13.5V21M6.75 6.75h.75m-.75 3h.75m-.75 3h.75m3-6h.75m-.75 3h.75m-.75 3h.75M6.75 21v-3.375c0-.621.504-1.125 1.125-1.125h2.25c.621 0 1.125.504 1.125 1.125V21M3 3h12m-.75 4.5H21m-3.75 3.75h.008v.008h-.008v-.008zm0 3h.008v.008h-.008v-.008zm0 3h.008v.008h-.008v-.008z" />
      </svg>
      <!-- titre text -->
      <span class="font-bold text-red-700">Qui sommes-nous ? </span>
    </a>
    <!-- carte de présentation du projet-->
    <div class="w-5/6 mx-auto flex py-7 items-center justify-center">
      <div class="flex justify-center items-center">
        <div class="group relative items-center justify-center overflow-hidden hover:shadow-black/30 transition-transform-shadow">
          <div class="h-96 w-full">
            <img class="h-full w-full rounded-xl object-cover group-hover:rotate-3 group-hover:scale-125 transition-transform" src="https://as2.ftcdn.net/v2/jpg/02/20/74/63/1000_F_220746363_R5RONDEpbZyDFGmWCPDgVOZW3gJ1SpRk.jpg"/>
          </div>
          <div class="absolute inset-0 bg-gradient-to-b from-transparent via-transparent to-black group-hover:from-black/70 group-hover:via-black/60 group-hover:to-black/70"></div>
          <div class="absolute inset-0 flex flex-col items-center justify-center px-9 text-center translate-y-[50%] group-hover:translate-y-0 transition-all">
            <h1 class="text-3xl font-bold text-white">Welcome!</h1>
            <p class="text-lg text-white"> Bienvenue sur notre site</p>
            <p class="text-base italic text-white mb-3 opacity-0 group-hover:opacity-100 transition-opacity duration-300"> 
              Si vous êtes là, c'est que la culture chinoise doit vous 
              intéresser un minimum n'est-ce pas ? 
            </p>
            <button class="rounded-full shadow shadow-black/60 bg-neutral-900 py-2 px-3.5 text-sm capitalize text-white hover:bg-neutral-900">
              Read More
            </button>
          </div>
        </div>
      </div>
    </div>
    <!-- cartes de présentation des personnes-->
    <!-- <div class="w-5/6 mx-auto py-7 gap-3 justify-center items-center md:flex"> -->
    <div class="w-5/6 mx-auto gap-3 justify-center items-center grid grid-cols-1 place-items-center md:flex">
    <!-- <div class="group relative items-center justify-center overflow-hidden cursor-pointer"> -->
      <!-- 1ère carte -->
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
      <!-- 2ème carte -->
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
      <!-- 3ème carte -->
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
  </section>
</template>

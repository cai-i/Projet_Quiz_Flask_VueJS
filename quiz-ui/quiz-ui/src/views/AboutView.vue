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
    <!-- cartes de présentation des personnes-->
    <div class="w-5/6 mx-auto mt-7 gap-3 justify-center items-center grid grid-cols-1 place-items-center md:flex">
    <!-- <div class="group relative items-center justify-center overflow-hidden cursor-pointer"> -->
      <!-- 1ère carte -->
      <div class="group h-96 w-96 [perspective:1000px]">
        <div class="relative h-full w-full rounded-xl shadow-xl transition-all duration-500 [transform-style:preserve-3d] group-hover:[transform:rotateY(180deg)]">
          <div class="absolute inset-0">
            <img class="h-full w-full rounded-xl object-cover shadow-xl shadow-black/40" src="https://img.rawpixel.com/private/static/images/website/2022-05/px1292817-image-kwvy1xs1.jpg?w=1200&h=1200&dpr=1&fit=clip&crop=default&fm=jpg&q=75&vib=3&con=3&usm=15&cs=srgb&bg=F4F4F3&ixlib=js-2.2.1&s=7c30808c57522f732b2b65e71836deb1"/>
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
            <img class="h-full w-full rounded-xl object-cover shadow-xl shadow-black/40" src="https://upload.wikimedia.org/wikipedia/commons/6/6d/Algorithmically-generated_landscape_artwork_of_forest_with_Shinto_shrine_using_negative_prompt_for_green_trees.png"/>
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
            <img class="h-full w-full rounded-xl object-cover shadow-xl shadow-black/40" src="https://img.rawpixel.com/private/static/images/website/2022-05/px1292817-image-kwvy1xs1.jpg?w=1200&h=1200&dpr=1&fit=clip&crop=default&fm=jpg&q=75&vib=3&con=3&usm=15&cs=srgb&bg=F4F4F3&ixlib=js-2.2.1&s=7c30808c57522f732b2b65e71836deb1"/>
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
    <!-- carte de présentation du projet et licenses-->
    <div class="w-5/6 mx-auto py-7 gap-3 justify-center items-center grid grid-cols-1 place-items-center md:flex">
      <!-- presentation du projet -->
      <div class="group relative items-center justify-center overflow-hidden hover:shadow-black/30 transition-transform-shadow">
        <div class="group h-96 w-96 [perspective:1000px]">
          <img class="h-full w-full rounded-xl object-cover group-hover:rotate-3 group-hover:scale-125 transition-transform" src="https://img.rawpixel.com/s3fs-private/rawpixel_images/website_content/fl46736410561-image-kybehrff.jpg?w=800&dpr=1&fit=default&crop=default&q=65&vib=3&con=3&usm=15&bg=F4F4F3&ixlib=js-2.2.1&s=3d55c9025c84ba7dde4908b23b44bafc"/>
        </div>
        <div class="absolute inset-0 bg-gradient-to-b from-transparent via-transparent to-black group-hover:from-black/70 group-hover:via-black/60 group-hover:to-black/70"></div>
        <div class="absolute inset-0 text-white flex flex-col items-center justify-center px-9 text-center translate-y-[50%] group-hover:translate-y-0 transition-all">
          <h1 class="text-3xl font-bold"> Pourquoi ce quiz ?</h1>
          <p class="italic"> Découvrez sur cette carte pourquoi nous avons été amené à faire une quiz sur la culture chinoise ! </p>
          <p class="text-base italic text-white mb-3 opacity-0 group-hover:opacity-100 transition-opacity duration-300"> 
            Si vous êtes là, c'est que la culture chinoise doit vous 
            intéresser un minimum n'est-ce pas ? 
          </p>
          <button class="rounded-full shadow shadow-black/60 bg-neutral-900 py-2 px-3.5 text-sm capitalize text-white hover:bg-neutral-900">
            Read More
          </button>
        </div>
      </div>
      <!-- licenses -->
      <div class="group relative items-center justify-center overflow-hidden hover:shadow-black/30 transition-transform-shadow">
        <div class="h-96 w-96">
          <img class="h-full w-full rounded-xl object-cover group-hover:rotate-3 group-hover:scale-125 transition-transform" src="https://img.rawpixel.com/s3fs-private/rawpixel_images/website_content/frgreat_wall_china_chinese_10-image-kybdjfx6.jpg?w=800&dpr=1&fit=default&crop=default&q=65&vib=3&con=3&usm=15&bg=F4F4F3&ixlib=js-2.2.1&s=ac2fb5ab469bd13595f89b987f6761b9"/>
        </div>
        <div class="absolute inset-0 bg-gradient-to-b from-transparent via-transparent to-black group-hover:from-black/70 group-hover:via-black/60 group-hover:to-black/70"></div>
        <div class="absolute inset-0 text-white flex flex-col items-center justify-center px-9 text-center translate-y-[70%] group-hover:translate-y-0 transition-all">
          <h1 class="text-3xl font-bold"> Les images</h1>
          <div class="mb-3 text-gray-200">
            <p class="text-base italic opacity-0 group-hover:opacity-100 transition-opacity duration-300"> 
              La plupart de nos images sont sous cette licence Creative Commons : 
            </p>
            <a class="hover:text-yellow-400 hover:underline" href="https://creativecommons.org/publicdomain/zero/1.0/"> 
              Lien
            </a>
          </div>
          <p class="font-bold text-green-400"> Les images : </p> 
          <div class="gap 3 grid grid-cols-2">
            <div class="gap-7 ">
              <a class="py-3 px-3 hover:text-yellow-400" href="https://www.rawpixel.com/image/5924500"> 
                Dragon coloré 
              </a>
              <a class="py-3 px-3 hover:text-yellow-400" href="https://commons.wikimedia.org/wiki/File:Algorithmically-generated_landscape_artwork_of_forest_with_Shinto_shrine_using_negative_prompt_for_green_trees.png">
                Temple rouge
              </a>
              <a class="py-3 px-3 hover:text-yellow-400" href="https://www.rawpixel.com/image/6042497/photo-image-desktop-wallpaper-cloud">
                Nuage rose
              </a>
              <a class="py-3 px-3 hover:text-yellow-400" href="https://www.rawpixel.com/image/6036966/photo-image-public-domain-green-nature">
                Muraille de Chine
              </a>
            </div>
            <div>
              <a class="py-3 px-3 hover:text-yellow-400" href="https://creativecommons.org/licenses/by-sa/4.0/deed.fr">
                Temple rouge
              </a>
            </div>
          </div>
          <div>
              <p class="font-bold text-green-400"> Autres licenses : </p> 
              <a class="py-3 px-3 hover:text-yellow-400" href="https://creativecommons.org/licenses/by-sa/4.0/deed.fr">
                Temple rouge
              </a>
            </div>
        </div>
      </div>
    </div>
  </section>
</template>

<template>
    <!-- image de fond -->
    <img class="block object-cover h-[600px] w-full" :src="backgroundImageURL"/>
    <!-- dégradé de couleur pour mieux voir le texte -->
    <div class="carousel-caption absolute bottom-0 h-[600px] left-0 right-0 bg-gradient-to-b from-white/10 to-black/80"></div>
    <!-- texte -->
    <div class="carousel-caption block absolute text-center bottom-14">
      <slot name="fireButton"></slot>
      <h5 class="text-3xl mb-3"> {{title}} </h5>
      <slot name="paragraphes"></slot>
    </div>
    <!-- liens image + licence -->
    <div class="absolute bottom-2 right-0 left-0 flex justify-center text-white">
      <div class="flex items-center opacity-50 hover:opacity-100">
        <svg xmlns="http://www.w3.org/2000/svg" fill="none" viewBox="0 0 24 24" stroke-width="1.5" stroke="currentColor" class="w-6 h-6">
          <path stroke-linecap="round" stroke-linejoin="round" d="M2.25 15.75l5.159-5.159a2.25 2.25 0 013.182 0l5.159 5.159m-1.5-1.5l1.409-1.409a2.25 2.25 0 013.182 0l2.909 2.909m-18 3.75h16.5a1.5 1.5 0 001.5-1.5V6a1.5 1.5 0 00-1.5-1.5H3.75A1.5 1.5 0 002.25 6v12a1.5 1.5 0 001.5 1.5zm10.5-11.25h.008v.008h-.008V8.25zm.375 0a.375.375 0 11-.75 0 .375.375 0 01.75 0z" />
        </svg>
        <a class="py-1 px-1 hover:underline" :href="imageURL">
          image
        </a>
      </div>
      <div class="flex items-center opacity-50 hover:opacity-100">
        <svg xmlns="http://www.w3.org/2000/svg" fill="none" viewBox="0 0 24 24" stroke-width="1.5" stroke="currentColor" class="w-6 h-6">
          <path stroke-linecap="round" stroke-linejoin="round" d="M19.5 14.25v-2.625a3.375 3.375 0 00-3.375-3.375h-1.5A1.125 1.125 0 0113.5 7.125v-1.5a3.375 3.375 0 00-3.375-3.375H8.25m0 12.75h7.5m-7.5 3H12M10.5 2.25H5.625c-.621 0-1.125.504-1.125 1.125v17.25c0 .621.504 1.125 1.125 1.125h12.75c.621 0 1.125-.504 1.125-1.125V11.25a9 9 0 00-9-9z" />
        </svg>
        <a class="py-1 px-1 hover:underline" :href="licenseURL">
          licence
        </a>
      </div>
    </div>
</template>


<script>
export default {
    props: ['backgroundImageURL', 'title','imageURL', 'licenseURL']
}
</script>
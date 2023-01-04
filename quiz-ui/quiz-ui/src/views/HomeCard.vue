<template>
    <div class="group relative shadow-lg shadow-black/30 h-96 w-16 cursor-pointer overflow-hidden transition-all duration-200">
        <img class="h-full object-cover group-hover:rotate-12 group-hover:scale-125 transition-all" :src="imageURL"/>
        <div class="invisible absolute inset-0 bg-gradient-to-b from-green-500/20 to-black group-hover:visible">
            <div class="absolute inset-x-5 bottom-6">
                <div class="flew gap-3 text-white">
                    <slot name="iconTitle"></slot>
                    <div>
                        <p class="font-semibold text-xl text-gray-100">
                            {{ title }}
                        </p>
                        <p class="text-gray-300">
                            {{ text }}
                        </p>
                    </div>
                </div>
                <div class="flex justify-end gap-3 text-gray-200">
                    <slot name="iconFooterRight1"></slot>
                    <slot name="iconFooterRight2"></slot>
                </div>
            </div>
        </div>
    </div>
</template>

<script>

export default {
    props: ['title', 'text', 'imageURL']
}

</script>
<template>
    <div class="relative w-auto my-6 mx-auto max-w-3xl">
        <!--content-->
        <div class="border-0 rounded-lg shadow-lg relative flex flex-col w-full bg-white outline-none focus:outline-none">
            <!--header-->
            <div class="flex items-start justify-between p-5 border-b border-solid border-slate-200 rounded-t">
                <h3 class="text-3xl font-semibold">Confirmation de la suppression</h3>
                <button class="p-1 ml-auto bg-transparent border-0 text-black opacity-5 float-right text-3xl leading-none font-semibold outline-none focus:outline-none" v-on:click="toggleModal()">
                    <span class="bg-transparent text-black opacity-5 h-6 w-6 text-2xl block outline-none focus:outline-none">×</span>
                </button>
            </div>
            <!--body-->
            <div class="relative p-6 flex-auto">
                <p class="my-4 text-slate-500 text-lg leading-relaxed">
                    Êtes-vous sûr de vouloir supprimer tous les questions?
                </p>
            </div>
            <!--footer-->
            <div class="flex items-center justify-end gap-3 p-6 border-t border-solid border-slate-200 rounded-b">
                <button @click="cancel" class="text-slate-500 bg-transparent border border-solid border-slate-500 hover:bg-slate-500 hover:text-white font-bold uppercase text-sm px-4 py-3 rounded outline-none focus:outline-none  mb-1 ease-linear transition-all duration-150">
                Annuler
                </button>
                <button @click="remove" class="text-red-500 bg-transparent border border-solid border-red-500 hover:bg-red-500 hover:text-white font-bold uppercase text-sm px-4 py-3 rounded outline-none focus:outline-none  mb-1 ease-linear transition-all duration-150">
                Supprimer
                </button>
            </div>
        </div>
    </div>
</template>
<script>

export default {
    methods: {
        cancel(){
            this.$emit('toggle-modal');
        },
        remove(){
            this.$emit('remove-all-questions');
        }
    }
}

</script>
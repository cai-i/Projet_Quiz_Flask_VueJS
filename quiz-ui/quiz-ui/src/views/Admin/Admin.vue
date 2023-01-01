<template>
    <div class="bg-orange-100">
    <section class="w-5/6 mx-auto relative py-6 px-3 h-screen ">
            <p class="text-5xl flex items-center py-1 px-7">
                <svg xmlns="http://www.w3.org/2000/svg" fill="none" viewBox="0 0 24 24" stroke-width="1.5" stroke="currentColor" class="w-12 h-12 mr-2 text-red-700">
                    <path stroke-linecap="round" stroke-linejoin="round" d="M4.26 10.147a60.436 60.436 0 00-.491 6.347A48.627 48.627 0 0112 20.904a48.627 48.627 0 018.232-4.41 60.46 60.46 0 00-.491-6.347m-15.482 0a50.57 50.57 0 00-2.658-.813A59.905 59.905 0 0112 3.493a59.902 59.902 0 0110.399 5.84c-.896.248-1.783.52-2.658.814m-15.482 0A50.697 50.697 0 0112 13.489a50.702 50.702 0 017.74-3.342M6.75 15a.75.75 0 100-1.5.75.75 0 000 1.5zm0 0v-3.675A55.378 55.378 0 0112 8.443m-7.007 11.55A5.981 5.981 0 006.75 15.75v-1.5" />
                </svg>
                <span class="font-bold text-red-700">Admin</span>
            </p>
            <div v-if="!adminMode">
                <div class="mt-16 grid gap-4 place-content-center">
                    <form class="shadow-md border bg-orange-200 border-red-700 rounded px-8 py-8 mb-4">
                        <div class="mb-4">
                            <label class="block text-rose-700 text-sm font-bold mb-2" for="password">
                                Mot de passe
                            </label>
                            <input class="shadow appearance-none border focus:border-red-500 rounded w-full py-2 px-3 text-gray-700 mb-3 leading-tight focus:outline-none focus:shadow-outline" v-model="password" id="password" type="password" placeholder="Votre mot de passe">
                        </div>
                        <button @click="login" class="bg-rose-700 hover:bg-rose-900 text-white font-bold py-2 px-4 rounded focus:outline-none focus:shadow-outline" type="button">
                            Se connecter
                        </button>
                    </form>
                </div>
            </div>
            <div v-else>
                <div class="wrapper">
                    <nav class="grid gap-4 px-8">
                        <i class="fa-solid fa-house"></i>
                            <RouterLink to="/admin/edit" class="block py-3 px-3 hover:bg-orange-200">Editer les questions</RouterLink>
                            <RouterLink to="/admin/list" class="block py-3 px-3 hover:bg-orange-200">Liste des questions</RouterLink>
                    </nav>
                </div>
            </div>
        </section>
    </div>
</template>
  
<script>
import quizApiService from "@/services/QuizApiService";
import participationStorageService from "@/services/ParticipationStorageService";

export default {
  name: "NewQuizPage",
  data() { 
    return {
        password: null,
        adminMode: false
    };  
  },
  mounted() {
      var token = participationStorageService.getAuthentificationToken();
      this.adminMode = (token != null) ? true : false;
    },
  methods:{
    async login(){
        var tokenPromise = quizApiService.getToken(this.password);
        var response = await tokenPromise;
        if (response != null) {
            participationStorageService.saveAuthentificationToken(response.data.token);
            this.adminMode = true;
        }
        else{
            participationStorageService.removeAuthentificationToken();
            this.adminMode = false;
        }

    }
  }
}
</script>

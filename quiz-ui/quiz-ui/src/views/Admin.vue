<template>
    <div class="about">
       <h1 class="py-8 px-8 text-xl font-bold text-red-800">Admin</h1>
    </div>
    <div v-if="!adminMode">
        <div class="mt-16 grid gap-4 place-content-center">
            <form class="shadow-md border rounded px-8 py-8 mb-4">
                <div class="mb-4">
                    <label class="block text-rose-700 text-sm font-bold mb-2" for="password">
                        Password
                    </label>
                    <input class="shadow appearance-none border border-red-500 rounded w-full py-2 px-3 text-gray-700 mb-3 leading-tight focus:outline-none focus:shadow-outline" v-model="password" id="password" type="password" placeholder="******************">
                </div>
                <button @click="login" class="bg-rose-700 hover:bg-rose-900 text-white font-bold py-2 px-4 rounded focus:outline-none focus:shadow-outline" type="button">
                    Sign In
                </button>
            </form>
        </div>
    </div>
    <div v-else>
        <div class="wrapper">
            <nav class="grid gap-4 px-8">
                <i class="fa-solid fa-house"></i>
                    <RouterLink to="/admin/edit">Editer les questions</RouterLink>
                    <RouterLink to="/admin/list">Liste des questions</RouterLink>
            </nav>
        </div>
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

<template>
  <div :style="myStyle">
    <h1
      class="py-16 px-8 text-4xl font-bold text-red-800"
      :style="myTextStrokeRule"
    >
      Commencer le quiz !
    </h1>

    <div class="mt-8 grid gap-4 place-content-center">
      <form
        class="shadow-md border rounded px-8 py-8 mb-4 bg-white bg-opacity-50"
        id="username"
        action=""
        method="post"
      >
        <label
          class="block text-xl text-rose-700 font-bold mb-2"
          for="name"
          :style="myTextStrokeRule"
        >
          Saisissez votre nom :
        </label>

        <input
          class="shadow appearance-none border border-red-500 rounded w-full py-2 px-3 text-gray-700 mb-3 leading-tight focus:outline-none focus:shadow-outline"
          type="text"
          id="name"
          placeholder="Votre super pseudo"
          v-model="username"
        />

        <button
          class="bg-rose-700 hover:bg-rose-900 mt-1 text-white font-bold w-full py-2 px-3 rounded focus:outline-none focus:shadow-outline"
          type="submit"
          @click="launchNewQuiz"
        >
          GO!
        </button>
      </form>
    </div>
  </div>
</template>

<script>
import participationStorageService from "@/services/ParticipationStorageService";

export default {
  name: "NewQuizPage",
  data() {
    return {
      username: null,
      myStyle: {
        textAlign: "center",
        paddingBottom: "20em",
        backgroundSize: "1550px auto",
        backgroundAttachment: "fixed, scroll, local",
        backgroundImage:
          // "url(https://images4.alphacoders.com/146/thumb-1920-146664.jpg)",
          // "url(https://img.rawpixel.com/private/static/images/website/2022-05/upwk82583677-wikimedia-image-kows5907.jpg?w=1200&h=1200&dpr=1&fit=clip&crop=default&fm=jpg&q=75&vib=3&con=3&usm=15&cs=srgb&bg=F4F4F3&ixlib=js-2.2.1&s=94d8d8d28d58bcee9ebf690dfa3917c8)",
          "url(https://live.staticflickr.com/3579/3654034811_34ce15acac_b.jpg)",
      },
      myTextStrokeRule: {
        textShadow:
          "0 4px 3px white, 0 -4px 3px white, 4px 0 3px white, -4px 0 3px white",
        webkitTextStroke: "0.1px",
        webkitTextStrokeColor: "white",
      },
    };
  },
  methods: {
    launchNewQuiz() {
      console.log("Launch new quiz with", this.username);
      participationStorageService.savePlayerName(this.username);
      this.$router.push("/questions");
    },
  },
};
</script>

<template>
  <div class = "flex">
    <input
      tabindex="-1"
      type="file"
      name="uploadInput"
      :disabled="isSaving"
      @change="fileChange"
      accept="image/jpeg, image/png, image/gif"
      class="input-file"
      ref="fileInput"
    />
    <a class="image-upload-remove-link pt-1" 
          v-if="file" 
          @click="clickRemoveImageHandler">
          <svg class="w-6 h-6 " fill="none" stroke="DarkRed" viewBox="0 0 24 24" xmlns="http://www.w3.org/2000/svg"><path stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="M19 7l-.867 12.142A2 2 0 0116.138 21H7.862a2 2 0 01-1.995-1.858L5 7m5 4v6m4-6v6m1-10V4a1 1 0 00-1-1h-4a1 1 0 00-1 1v3M4 7h16"></path></svg>
    </a>
  </div>
</template>
<script>
  export default {
    emits: ["file-change"],
    data() {
      return {
        isSaving: false,
        fileReader: null,
        fileInput: null,
        file: null
      };
    },
    props: {
      question: {
        type: Object,
      },
    },
    mounted() {
      this.fileInput = this.$refs.fileInput;
      this.fileReader = new FileReader();
      this.fileReader.addEventListener(
        "load",
        () => {
          // fileReader holds a b64 string of the image
          this.fileDataUrl = this.fileReader?.result;
          this.isSaving = false;
          this.$emit("file-change", this.fileDataUrl);
        },
        false
      );
    },
    methods: {
      fileChange(event) {
        this.isSaving = true;
        const input = event.target;
        // pick the first file uploaded
        this.file = input.files[0];
        // feed the file to the asynchronous file reader
        // (next step is in the load eventListener defined in mounted)
        this.fileReader.readAsDataURL(this.file);
      },
      clickRemoveImageHandler() {
        this.file = null;
        this.$emit("file-change", "");
        if (this.fileInput) {
          this.fileInput.value = "";
        }
      }
    }
  };
  </script>
  
  <style>
  .image-upload-remove-link {
    display: block;
  }
  </style>
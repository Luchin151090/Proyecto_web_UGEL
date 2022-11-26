<template>
  <v-app>
    <v-main>
      <v-card height="500" width="700">
        <form class="formu" enctype="multipart/form-data" @submit.prevent="submit">
          <v-file-input required  label="archivo" v-model="file"></v-file-input>
          <v-btn :disabled="valid" type="submit" @click="submitFile">Sube</v-btn>
        </form>
      </v-card>
    </v-main>
  </v-app>
</template>
<script>
import axios from "axios";
export default {
  data: () => ({
    file: null,
    config_header: {
      "Content-Type": "multipart/form-data",
    },
    rules:[
  ],
  }),
  methods: {
    uploadFile() {
      this.file = this.$refs.file.files[0];
    },
    submitFile() {
      const formdata = new FormData();
      formdata.append("file", this.file);
      console.log(this.file.name);

      axios
        .post("http://127.0.0.1:5000/upload_file", formdata, this.config_header)
        .then((res) => {
          res.data.files;
          res.status;
          console.log(res.data.files);
        })
        .catch((error) => {
          console.log(error);
        });
    },
  },
};
</script>
<style scoped>
  .formu{
    padding-left: 10px;
    padding-right: 550px;
    padding-top: 50px;
  }
</style>

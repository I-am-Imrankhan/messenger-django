<script>
import { ref, onMounted, defineComponent } from "vue";
import apiClient from "@/api.js";
import axios from "axios";
const options = {
  method: 'GET',
  url: '',
  params: {all: 'true'},
  headers: {
    'localhost': 'http://127.0.0.1:8000/'
  }
};
const response = await apiClient.get("/messages/")
  console.log("onMounted ", response)

</script>

<template><h2>lkajlka</h2></template>

<style scoped>
.read-the-docs {
  color: #888;
}
</style>

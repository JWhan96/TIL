<template>
  <div>
    <h1>SignUp</h1>
    <form @submit.prevent="signUp">
      아이디: <input type="text" v-model.trim="username">
      <br>
      비밀번호: <input type="password" v-model.trim="password1">
      <br>
      비밀번호 확인: <input type="password" v-model.trim="password2">
      <input type="submit">
    </form>
  </div>
</template>

<script setup>
import { ref } from 'vue'
import { useCounterStore } from '@/stores/counter'

const store = useCounterStore()
const username = ref(null)
const password1 = ref(null)
const password2 = ref(null)


const signUp = function () {
  const payload = {
    username: username.value,
    password1: password1.value,
    password2: password2.value,
  }

store.signUp(payload)
}

</script>

<style>

</style>

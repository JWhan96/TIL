<template>
  <div>
    <h1>Todo PJT</h1>
    <h2>완료된 Todo : {{ store.doneTodosCount }}</h2>
    <TodoForm />
    <TodoList />
  </div>
</template>

<script setup>
import TodoForm from '@/components/TodoForm.vue'
import TodoList from '@/components/TodoList.vue'

import { useCounterStore } from '@/stores/counter'

const store = useCounterStore()
</script>

<style scoped>
</style>

<script setup lang="ts">
import FormComponent from './components/FormComponent.vue'
</script>

<template>
  <div class="content-container">
    <div>
      <h1 class="title"><strong>integral</strong>.pjbl</h1>
    </div>
    <FormComponent />
  </div>
</template>

<style scoped>
.content-container {
  min-width: 40%;
  margin-top: 150px;
  padding: 20px;
  border-radius: 8px;

  display: flex;
  align-items: center;
  justify-content: center;
  flex-direction: column;

  background: var(--surface-color);
}

.title {
  font-weight: normal;
}

</style>

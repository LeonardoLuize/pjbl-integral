<script setup lang="ts">
import { ref } from 'vue'

defineProps<{ msg: string }>()

const count = ref(0)
</script>

<template>
  <form class="form-container">
    <section>
      <label for="a-interval">Intervalo A: </label>
      <input id="a-interval" type="number" />
    </section>

    <section>
      <label for="b-interval">Intervalo B: </label>
      <input id="b-interval" type="number" />
    </section>

    <section>
      <label for="n-repetitions">Repetições N: </label>
      <input id="n-repetitions" type="number" />
    </section>

    <button>Calcular</button>
  </form>
</template>

<style scoped>
.form-container {
  width: 100%;
  max-width: 80%;

  display: flex;
  align-items: center;
  justify-content: space-around;
  flex-direction: column;
  gap: 10px;

  margin-top: 25px;
}

.form-container section {
  width: 100%;
  display: flex;
  justify-content: center;
  flex-direction: column;
}

.form-container input {
  padding: 5px;
  border-radius: 5px;
  border: 2px solid #ddd;
}

.form-container button {
  background: var(--accent-color);
  color: white;

  border: none;
  border-radius: 5px;

  padding: 10px;
  margin-top: 10px;
  
  width: 100%;
  cursor: pointer;
  transition: all .2s;
}

.form-container button:hover {
  filter: brightness(0.9);
}

</style>

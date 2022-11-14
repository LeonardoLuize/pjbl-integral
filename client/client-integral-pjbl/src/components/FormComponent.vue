<script setup lang="ts">
import { reactive, ref } from 'vue'
import axios from 'axios'

type Payload = {
  value_a: number
  value_b: number
  repeat_n: number
}
const state = reactive({ result: "", inputAError: false, inputNError: false })

const inputA = ref(0)
const inputB = ref(0)
const inputN = ref(0)

const baseUrls = [
  "http://127.0.0.1:8000",
  "http://127.0.0.1:8001",
  "http://127.0.0.1:8002",
  "http://127.0.0.1:8003",
]

function verifyValues() {
  console.log("A:" + Number(inputA.value))
  console.log("B:" + Number(inputB.value))
  if (Number(inputA.value) < Number(inputB.value)) {
    state.inputAError = true
  }

  if (inputN.value <= 0) {
    state.inputNError = true
  }

  if (state.inputNError || state.inputAError) {
    return false
  }

  return true
}

async function calculateInterval(baseURL: String, body: Payload) {
  let res = await axios.post(`${baseURL}/api/calculate`, body)

  if (res.status == 200)
    return res.data.value
  else
    alert("Houve um erro no request :/")
}

function getIntervalsArray() {
  let difference = inputA.value - inputB.value
  let decimal = difference - Math.floor(difference)
  let interval = Math.ceil(difference / 4)
  let intervals = []
  let count = 0
  let newInterval = []

  for (let i = 0; i < difference; i++) {
    newInterval.push(i)

    if (count == (interval - 1)) {
      count = 0
      intervals.push(newInterval)
      newInterval = []
      continue
    }
    count++
  }

  let lastIntervalGroup = intervals.length - 1
  let lastInterval = intervals[lastIntervalGroup].length - 1
  intervals[lastIntervalGroup][lastInterval] = Math.round((intervals[lastIntervalGroup][lastInterval] + decimal) * 10) / 10

  return intervals
}

function handleClick() {
  state.result = ""
  state.inputAError = false
  state.inputNError = false

  if (!verifyValues()) {
    alert("Dados inválidos")
    return
  }

  let intervalsArray = getIntervalsArray()
  console.log(intervalsArray)

  let promises:Array<Promise<any>> = []

  for (let interval of intervalsArray) {
    promises.push(calculateInterval(baseUrls[0] ,{
      "value_a": interval.length > 1 ? interval[0] : 0,
      "value_b": interval.length > 1 ? interval[1] : interval[0],
      "repeat_n": inputN.value
    }))    
  }

  Promise.all(promises).then(values => {
    console.log(values)
    
    let total = values.reduce((previous, current) => {
      return previous + current
    }, 0)

    state.result = String(total)
  })
}

</script>

<template>
  <form @submit.prevent="" class="form-container">
    <section>
      <label for="a-interval">Intervalo A: </label>
      <input v-model="inputA" id="a-interval" />
      <span class="error-msg" :class="{ 'd-none': !state.inputAError }">A deve ser maior ou igual a B</span>
    </section>

    <section>
      <label for="b-interval">Intervalo B: </label>
      <input v-model="inputB" id="b-interval" />
      <span class="error-msg" :class="{ 'd-none': !state.inputAError }">B deve ser menor ou igual a A</span>
    </section>

    <section>
      <label for="n-repetitions">Repetições N: </label>
      <input v-model="inputN" id="n-repetitions" type="number" />
      <span class="error-msg" :class="{ 'd-none': !state.inputNError }">N deve ser maior que 0</span>
    </section>

    <button @click="handleClick()">Calcular</button>
  </form>

  <div v-if="state.result !== ''" class="result-container">
    <p>Resultado: {{ state.result }}</p>
  </div>
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

  margin-top: 20px;
  padding-top: 10px;
  border-top: 2px solid var(--border-color)
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
  border: 2px solid var(--border-color);
}

.form-container section span {
  color: var(--error-color);
  font-size: 14px;
}

.d-none {
  opacity: 0;
}

.form-container button {
  background: var(--accent-color);
  color: white;

  border: none;
  border-radius: 5px;

  padding: 10px;
  margin-top: 5px;

  width: 100%;
  cursor: pointer;
  transition: all .2s;
}

.form-container button:hover {
  filter: brightness(0.9);
}

.result-container {
  width: 100%;
  max-width: 80%;

  margin-top: 25px;
  padding-top: 20px;
  border-top: 2px solid var(--border-color);
  display: flex;
}

.result-container p {
  font-size: 18px;
}
</style>

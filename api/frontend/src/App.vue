<template>
  <div id="app" class="container mx-auto px-4 py-8">
    <h1 class="text-3xl font-bold mb-6">Busca de Operadoras de Saúde</h1>
    <SearchComponent />
  </div>
</template>

<script>
import SearchComponent from './components/SearchComponent.vue';

export default {
  components: {
    SearchComponent
  }
};
</script>

<style>
#app {
  font-family: Avenir, Helvetica, Arial, sans-serif;
}
</style>
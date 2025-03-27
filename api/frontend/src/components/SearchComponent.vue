<template>
    <div class="search-container">
      <div class="search-input-group mb-4">
        <input 
          v-model="query" 
          @keyup.enter="search" 
          placeholder="Digite para buscar" 
          class="w-full p-2 border rounded mr-2"
        />
        <div class="flex items-center mt-2">
          <select 
            v-model="selectedModalidade" 
            class="p-2 border rounded mr-2"
          >
            <option value="">Todas Modalidades</option>
            <option>Administradora de Benefícios</option>
            <option>Medicina de Grupo</option>
            <option>Odontologia de Grupo</option>
            <option>Autogestão</option>
          </select>
          <button 
            @click="search" 
            :disabled="loading" 
            class="px-4 py-2 bg-blue-500 text-white rounded hover:bg-blue-600"
          >
            Buscar
          </button>
        </div>
      </div>

      <div v-if="loading" class="text-center py-4">
        <p>Carregando...</p>
      </div>

      <div v-if="error" class="bg-red-100 border border-red-400 text-red-700 px-4 py-3 rounded relative" role="alert">
        {{ error }}
      </div>

      <div v-if="results.length" class="results-container">
        <div 
          v-for="result in results" 
          :key="result.Registro_ANS" 
          class="border rounded p-4 mb-4 shadow-sm"
        >
          <h2 class="text-xl font-semibold">{{ result.Razao_Social }}</h2>
          <p><strong>Nome Fantasia:</strong> {{ result.Nome_Fantasia || 'Não informado' }}</p>
          <p><strong>Localização:</strong> {{ result.Cidade }}/{{ result.UF }}</p>
          <p><strong>Modalidade:</strong> {{ result.Modalidade }}</p>
          <p><strong>CNPJ:</strong> {{ result.CNPJ }}</p>
          <p><strong>Registro ANS:</strong> {{ result.Registro_ANS }}</p>
        </div>

        <div v-if="hasMoreResults" class="text-center mt-4">
          <button 
            @click="loadMore" 
            class="px-4 py-2 bg-green-500 text-white rounded hover:bg-green-600"
          >
            Carregar mais resultados
          </button>
        </div>
      </div>

      <div v-if="!loading && !results.length && query" class="text-center text-gray-500 py-4">
        Nenhum resultado encontrado
      </div>
    </div>
  </template>

  <script>
  import { ref, computed } from 'vue';
  import axios from 'axios';
  import { debounce } from 'lodash-es';

  export default {
    setup() {
      const query = ref('');
      const results = ref([]);
      const loading = ref(false);
      const error = ref(null);
      const page = ref(1);
      const selectedModalidade = ref('');

      const debouncedSearch = debounce(async () => {
        if (!query.value.trim()) return;

        loading.value = true;
        error.value = null;
        page.value = 1;

        try {
          const response = await axios.get('http://127.0.0.1:5000/busca', {
            params: { 
              q: query.value, 
              limit: 10,
              page: page.value,
              modalidade: selectedModalidade.value
            }
          });

          results.value = response.data;
        } catch (err) {
          error.value = err.response 
            ? err.response.data.message 
            : 'Erro de conexão com o servidor';

          console.error('Erro na busca:', err);
        } finally {
          loading.value = false;
        }
      }, 300);

      const search = () => {
        debouncedSearch();
      };

      const loadMore = async () => {
        page.value += 1;
        loading.value = true;

        try {
          const response = await axios.get('http://127.0.0.1:5000/busca', {
            params: { 
              q: query.value, 
              limit: 10,
              page: page.value,
              modalidade: selectedModalidade.value
            }
          });

          results.value = [...results.value, ...response.data];
        } catch (err) {
          error.value = 'Erro ao carregar mais resultados';
          console.error('Erro ao carregar mais:', err);
        } finally {
          loading.value = false;
        }
      };

      const hasMoreResults = computed(() => {
        return results.value.length > 0 && results.value.length % 10 === 0;
      });

      return { 
        query, 
        results, 
        search, 
        loading, 
        error, 
        loadMore,
        hasMoreResults,
        selectedModalidade
      };
    }
  };
  </script>

  <style scoped>
  input, select, button {
    margin-bottom: 10px;
  }
  </style>
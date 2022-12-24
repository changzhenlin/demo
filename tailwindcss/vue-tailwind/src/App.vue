<script setup>
import SiteNavigation from './components/SiteNavigation.vue';
import {RouterView} from 'vue-router';
</script>

<template>
  <div class="flex flex-col min-h-screen bg-pink-300">
    <SiteNavigation />
    <RouterView />
  </div>
</template>

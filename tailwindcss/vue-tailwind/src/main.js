import { createApp } from 'vue'
import App from './App.vue'
import './index.css'
import './assets/main.css'
import router from './router/index'

let app = createApp(App)
app.use(router)
app.mount('#app')


import './assets/main.css'
import App from './App.vue'
import router from './router'

import { createApp } from 'vue'
import { createPinia } from 'pinia'
import { library } from '@fortawesome/fontawesome-svg-core'
import { FontAwesomeIcon } from '@fortawesome/vue-fontawesome'
import {
  faXTwitter,
  faSquareGithub,
  faQq,
  faTelegram,
} from '@fortawesome/free-brands-svg-icons'

library.add(faXTwitter, faSquareGithub, faQq, faTelegram)

const app = createApp(App)

app.component('font-awesome-icon', FontAwesomeIcon)
app.use(createPinia())
app.use(router)

app.mount('#app')

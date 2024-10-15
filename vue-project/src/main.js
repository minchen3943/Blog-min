import './assets/main.css'

import { createApp } from 'vue'
import { createPinia } from 'pinia'
import { createHead } from '@vueuse/head'

import App from './App.vue'
import router from './router'

import { library } from '@fortawesome/fontawesome-svg-core'
import { FontAwesomeIcon } from '@fortawesome/vue-fontawesome'
import { faUserSecret } from '@fortawesome/free-solid-svg-icons'
import {
  faXTwitter,
  faSquareGithub,
  faQq,
} from '@fortawesome/free-brands-svg-icons'

/* add icons to the library */
library.add(faUserSecret, faXTwitter, faSquareGithub, faQq)

const app = createApp(App)
const head = createHead()

app.component('font-awesome-icon', FontAwesomeIcon)
app.use(createPinia())
app.use(router)
app.use(head)

app.mount('#app')

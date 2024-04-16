import {createApp} from 'vue'
import App from './App.vue'

import './style.css'
import {createVuetify} from "vuetify";
import * as components from "vuetify/components";
import * as directives from "vuetify/directives";
import 'vuetify/dist/vuetify.min.css'
import { aliases, mdi } from "vuetify/iconsets/mdi";
import '@mdi/font/css/materialdesignicons.css'

import 'highlight.js/styles/stackoverflow-light.css'
import 'highlight.js/lib/common'
import hljs from 'highlight.js/lib/core'
import python from 'highlight.js/lib/languages/python'

import store from './store/store'

import './demos/ipc'

const vuetify = createVuetify({
    components,
    directives,
    icons: {
        defaultSet: 'mdi',
        aliases,
        sets: {
            mdi,
        },
    },
    theme: {
        defaultTheme: 'dark'
    }
});

hljs.registerLanguage('python', python)

const app = createApp(App)
app.use(vuetify)
app.use(store)

app.mount('#app')
    .$nextTick(() => {
        postMessage({payload: 'removeLoading'}, '*')
    })

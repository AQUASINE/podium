import {createApp} from 'vue'
import App from './App.vue'

import './style.css'
import {createVuetify} from "vuetify";
import * as components from "vuetify/components";
import * as directives from "vuetify/directives";
import 'vuetify/dist/vuetify.min.css'
import { aliases, mdi } from "vuetify/iconsets/mdi";
import '@mdi/font/css/materialdesignicons.css'

import './demos/ipc'
// If you want to use Node.js, the`nodeIntegration` needs to be enabled in the Main process.
// import './demos/node'

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

const app = createApp(App)

app.use(vuetify)
app.mount('#app')
    .$nextTick(() => {
        postMessage({payload: 'removeLoading'}, '*')
    })

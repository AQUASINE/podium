# Podium Live

Twitch/YouTube ranking client intended to help streamers develop interesting apps for their viewers.

<!-- [![awesome-vite](https://awesome.re/mentioned-badge.svg)](https://github.com/vitejs/awesome-vite) -->
<!-- [![Netlify Status](https://api.netlify.com/api/v1/badges/ae3863e3-1aec-4eb1-8f9f-1890af56929d/deploy-status)](https://app.netlify.com/sites/electron-vite/deploys) -->
<!-- [![GitHub license](https://img.shields.io/github/license/caoxiemeihao/electron-vite-vue)](https://github.com/electron-vite/electron-vite-vue/blob/main/LICENSE) -->
<!-- [![GitHub stars](https://img.shields.io/github/stars/caoxiemeihao/electron-vite-vue?color=fa6470)](https://github.com/electron-vite/electron-vite-vue) -->
<!-- [![GitHub forks](https://img.shields.io/github/forks/caoxiemeihao/electron-vite-vue)](https://github.com/electron-vite/electron-vite-vue) -->
[![GitHub Build](https://github.com/AQUASINE/podium/actions/workflows/build.yml/badge.svg)](https://github.com/electron-vite/electron-vite-vue/actions/workflows/build.yml)
[![Static Badge](https://img.shields.io/badge/Documentation-blue)](https://docs.podiumlive.dev/)

## Features

- Create ruleset pipelines that will rank your chatters based on their activity in chat.
- Find the best messages and best users based on whatever criteria you want.

## TODO 
- [ ] Add items to todo list


## Quick Setup

```sh
# clone the project
git clone https://github.com/AQUASINE/podium.git

# enter the project directory
cd podium

# install dependencies
pip install -r requirements.txt
npm install
```

Note that before running the project, you need to create a `config.json` file in the root directory with the following content:
    
```json
{
  "TWITCH_OAUTH": "oauth:xxxxxxxxxxxxxxxxxx",
  "BOT_USERNAME": "your_twitch_username",
  "OPENAI_KEY": "sk-xxxxxxxxxxxxxxxxxxxxx"
}
```

Generate your Twitch OAuth token [here](https://twitchapps.com/tmi/), and use the account name you used to generate the token as `BOT_USERNAME`.

Get your OpenAI key [here](https://platform.openai.com/settings/profile?tab=api-keys).

```sh
# develop
npm run dev
```

## Directory

```diff
+ ├─┬ electron
+ │ ├─┬ main
+ │ │ └── index.ts    entry of Electron-Main
+ │ └─┬ preload
+ │   └── index.ts    entry of Preload-Scripts
  ├─┬ src
  │ └── main.ts       entry of Electron-Renderer
  ├── index.html
  ├── package.json
  └── vite.config.ts
```

<!--
## Be aware

🚨 By default, this template integrates Node.js in the Renderer process. If you don't need it, you just remove the option below. [Because it will modify the default config of Vite](https://github.com/electron-vite/vite-plugin-electron-renderer#config-presets-opinionated).

```diff
# vite.config.ts

export default {
  plugins: [
-   // Use Node.js API in the Renderer-process
-   renderer({
-     nodeIntegration: true,
-   }),
  ],
}
```
-->

## FAQ

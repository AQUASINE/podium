const configurations = {
    namespaced: true,
    state: {
        active: 'abcdsdf',
        configurations: [
            {
                id: "abcdsdf",
                name: "Default",
                lastUpdated: new Date("2024-04-11T12:00:00"),
                description: "This is the default configuration for how to use Podium to rank messages and users.",
                dataSources: [
                    {
                        id: "1234",
                        type: "ttv",
                        channelId: "Atrioc",
                        startingScore: 0.5
                    },
                    {
                        id: "5678",
                        type: "yt",
                        username: "fuslie",
                        channelId: 'UCujyjxsq5FZNVnQro51zKSQ',
                        startingScore: 0.9
                    }
                ],
                rules: [
                    {
                        id: "9991",
                        condition: {
                            type: 'contains',
                            value: 'POG'
                        },
                        action: {
                            type: 'add',
                            value: 1.0
                        }
                    }
                ],
                output: {
                    port: 8765,
                    consumeMode: false,
                }
            }
        ]
    },
    mutations: {
        setActiveConfiguration(state, payload) {
            state.active = payload;
        },
        setConfigurations(state, payload) {
            state.configurations = payload;
        },
        upsertConfiguration(state, payload) {
            const index = state.configurations.findIndex(c => c.id === payload.id);
            if (index === -1) {
                state.configurations.push(payload);
                return;
            }
            state.configurations[index] = payload;
        }
    },
}
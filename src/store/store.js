import {createStore} from "vuex";

const store = createStore({
    modules: {

    },
    state: {
        isConnected: false,
        connectionString: "localhost:8765",
        socket: null,
        users: [],
        messages: [],
    },
    mutations: {
        setConnection(state, payload) {
            state.isConnected = payload;
        },
        setSocket(state, payload) {
            state.socket = payload;
        },
        setUsers(state, payload) {
            state.users = payload;
        },
        setMessages(state, payload) {
            state.messages = payload;
        }
    },
    actions: {
        async connect({state, commit, dispatch}) {
            const socket = new WebSocket('ws://localhost:8765');
            socket.addEventListener('open', () => {
                console.log('Connected to server');
                commit('setConnection', true);
            });
            socket.addEventListener('message', event => {
                console.log('Message from server ', event.data);
                dispatch('pushMessage', event.data);
            });
            commit('setSocket', socket);
        },
        async getMessages({state, commit, dispatch}) {
            await dispatch('connect');
            setInterval(() => {
                // check if socket is in the closed state
                if (state.socket?.readyState === 3) {
                    console.log('Socket is closed, reconnecting');
                    dispatch('connect');
                }

                // fetch list of users from localhost:5000
                fetch('http://localhost:5000/get_users')
                    .then(response => response.json())
                    .then(data => {
                        console.log('Users list: ', data)
                        // sort users by user_score. data is an object of key-value pairs, convert to array
                        let users = Object.values(data);
                        users = users.sort((a, b) => b.user_score - a.user_score);
                        commit('setUsers', users);
                        console.log('Sorted users: ', this.users)
                    });
            }, 3000);
        },
        pushMessage({state}, message) {
            const decodedMessage = JSON.parse(message);
            if (state.messages.length > 500) {
                // remove 100 messages
                state.messages = this.messages.slice(100);
            }
            state.messages.push(decodedMessage);
        },
    }
})

export default store;
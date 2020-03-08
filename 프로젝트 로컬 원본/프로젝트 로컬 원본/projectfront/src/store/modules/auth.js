import jwtDecode from 'jwt-decode';

const isToken = () => {
	const storage = sessionStorage.getItem('vue-session-key');
	if (storage) {
		const isToken = JSON.parse(storage).hasOwnProperty('mmr-token');
		if (isToken) {
			return true;
		}
	}
	return false;
};

const state = {
	token: isToken()
		? JSON.parse(sessionStorage.getItem('vue-session-key'))['mmr-token']
		: null,
};

const mutations = {
	setToken(state, token) {
		state.token = token;
	},
};

const actions = {
	setTokenAction(options, token) {
		options.commit('setToken', token);
	},
	logout(options) {
		options.commit('setToken', null);
	},
};

const getters = {
	isAuthenticated(state) {
		return state.token ? true : false;
	},
	requestHeader(state) {
		return {
			headers: {
				Authorization: `JWT ${state.token}`,
			},
		};
	},
	userId(state) {
		return state.token ? jwtDecode(state.token).user_id : null
	},
	loggedInUser(state) {
		return state.token ? jwtDecode(state.token) : null;
	},
};

export default {
	state,
	mutations,
	actions,
	getters,
};
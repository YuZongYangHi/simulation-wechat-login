import Qs from 'qs'
import axios from 'axios';
import {withRouter } from 'react-router-dom';


axios.interceptors.request.use(
	config => {
		config.headers.Authorization = `${window.localStorage.getItem('token')}`;
	    //config.headers['Content-Type'] = 'application/json'
        config.headers['Content-Type'] = 'application/x-www-form-urlencoded'
		return config;
	},
	err => {
		return Promise.reject(err);
	});
axios.interceptors.response.use(
	response => {
		if (window.location.pathname.split('/')[1] != 'login' && response.data.code == 401 || response.data.code == 405)  {
			window.localStorage.removeItem('username')
			window.localStorage.removeItem('token')
			window.location.href = '/login'
		}
		return response
	},
	error => {
        let res = error.response;
       
		switch (res.status) {
			case 401:
				window.localStorage.removeItem('username')
				window.localStorage.removeItem('token')
				break
			case 403:
				break
			case 500:
				break
		}
		return Promise.reject(error.response.data)
    });

const host = 'http://127.0.0.1:8000'
const login_log_uri = `${host}/api/v1/common/login`
const check_login_uri = `${host}/api/v1/common/check_login`
const index_uri = `${host}/api/v1/assets`

export const index_request = (body) => {
	return axios.get(`${index_uri}/`,Qs.stringify(body))
}
export const login_request = (body) => {
    return axios.get(`${login_log_uri}/`,Qs.stringify(body))
}



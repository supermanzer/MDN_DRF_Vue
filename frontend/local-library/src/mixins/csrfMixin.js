/**
 * Define a mixin to provide getting CSRF Token 
 */
import axios from 'axios';
export const csrfMixin = {
    methods: {
        getToken(url) {
            const fullUrl = `${url}/get-token/`
            axios.get(fullUrl)
                .then(response => response.data)
                .then(data => {
                    document.cookie = `csrftoken=${data.token}; SameSite=None;Secure`
                })
                .catch(error => console.log(error))
        }
    }
}
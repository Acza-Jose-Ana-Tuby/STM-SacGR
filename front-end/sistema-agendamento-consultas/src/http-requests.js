import axios from "axios"

let baseURLRequest = axios.create({
    baseURL: "http://localhost:5000/api",
    headers: {
        'Content-Type':  'application/json',
        'Access-Control-Allow-Credentials' : 'true',
        'Access-Control-Allow-Origin': '*',
        'Access-Control-Allow-Methods': 'GET, POST, PATCH, DELETE, PUT, OPTIONS',
        'Access-Control-Allow-Headers': 'Content-Type, Access-Control-Allow-Headers, Authorization, X-Requested-With',
    }
})

class httpRequests {
    create(object, data) {
        console.log(baseURLRequest.post(`/${object}`, data))
    }
}

export default new httpRequests();
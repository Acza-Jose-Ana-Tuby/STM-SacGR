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
        return baseURLRequest.post(`/${object}`, data)
    }

    read(object, id) {
        return baseURLRequest.get(`/${object}/${id}`)
    }

    readAll(object) {
        return baseURLRequest.get(`/${object}`)
    }

    update(object, id, data) {
        return baseURLRequest.put(`/${object}/${id}`, data)
    }

    delete(object, id) {
        return baseURLRequest.delete(`/${object}/${id}`)
    }

}

export default new httpRequests();
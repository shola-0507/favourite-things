<template>
    <div class="container">
        <Header />
        <div v-if="alert">
            <Alert />
        </div>
        <table class="table">
            <thead class="thead-dark">
                <tr>
                    <th scope="col">Action</th>
                    <th scope="col">Date</th>
                </tr>
            </thead>
            <tbody>
                <tr v-bind:key="log.id" v-for="log in logs">
                    <td>{{ log.action }}</td>
                    <td>{{ new Date(log.date).toString() }}</td>
                </tr>
            </tbody>
        </table>
    </div>
</template>

<script>
    import axios from 'axios';
    import Header from '../components/layout/Header';
    import Alert from '../components/layout/Alert';

    export default {
        name: "Logs",
        components: { Header, Alert },
        data() {
            return {
                logs: [],
                alert: null
            }
        },
        created() {
            axios.get('https://britecore-backend-flask.herokuapp.com/logs/get', { withCredentials: true })
            .then(res => this.logs = res.data)
            .catch(err => console.log(err))
        }
    }
</script>
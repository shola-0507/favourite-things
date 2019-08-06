<template>
    <div>
        <div class="container">
            <Header />
            <div v-if="alert">
                <Alert />
            </div>
            <form>
                <div class="form-row">
                    <div class="col padding">
                        <input type="text" class="form-control" id="name" name="name" placeholder="Please Enter a title">
                    </div>
                    <div class="col padding">
                        <input type="button" class="btn btn-success" value="Create Category" @click="AddCategory"/>
                    </div>
                </div>
            </form>
            <Categories v-bind:categories="categories"/>
        </div>
    </div>
</template>

<script>
    import Header from '../components/layout/Header';
    import Alert from '../components/layout/Alert';
    import Categories from '../components/Categories';
    import axios from 'axios';

    export default {
        name: "CreateCategory",
        components: { Header, Alert, Categories },
        data() {
            return {
                alert: null,
                categories: []
            }
        },
        methods: {
            AddCategory() {
                const name = document.getElementById('name').value;
                axios.post('https://britecore-backend-flask.herokuapp.com/category/create', { name }, { withCredentials: true })
                .then(res => this.categories.push(res.data))
                .catch(err => console.log(err))
            }
        },
        mounted() {
            axios.get('https://britecore-backend-flask.herokuapp.com/category/all', { withCredentials: true })
            .then(res => this.categories = res.data)
            .catch(err => console.log(err))
        }
    }
</script>

<style scoped>
    .form-row {
        padding: 10px;
    }
    .btn {
        width: 100%;
    }
</style>

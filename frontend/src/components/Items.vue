<template>
    <div class="container">
        <table class="table">
            <thead class="thead-dark">
                <tr>
                    <th scope="col">Rank</th>
                    <th scope="col">Name</th>
                    <th scope="col">Description</th>
                    <th scope="col">Created At</th>
                    <th scope="col">Modified At</th>
                    <th scope="col">Meta Information</th>
                </tr>
            </thead>
            
            <draggable v-model="sortedItems" draggable=".item" tag="tbody">
                <tr v-bind:key="item.id" v-for="item in sortedItems" class="item" @dragend="dragged()">
                    <td>{{ item.rank }}</td>
                    <td>{{ item.title }}</td>
                    <td>{{ item.description }}</td>
                    <td>{{ new Date(item.created_date).toString() }}</td>
                    <td>{{ new Date(item.modified_date).toString() }}</td>
                    <td> 
                        <div class="nav-item dropdown">
                            <a class="nav-link dropdown-toggle" data-toggle="dropdown" href="#" role="button" aria-haspopup="true" aria-expanded="false">MetaData</a>
                            <div class="dropdown-menu">
                                <a class="dropdown-item" href="#">
                                    <p v-bind:key="index" v-for="(data, index) in item.meta">
                                        <strong>{{ data.name }}</strong>: {{ data.data }}
                                    </p>
                                </a>
                            </div>
                        </div>
                    </td>
                </tr>
            </draggable>
        </table>
        <div v-if="sorted">
            <input type="button" class="btn btn-success" value="Update Rank" @click="updateRank"/>
        </div>
    </div>
</template>

<script>
    import draggable from 'vuedraggable';
    import axios from 'axios';

    export default {
        name: "Items",
        props: {
            items: Array
        },
        data() {
            return {
                sortedItems: this.items,
                sorted: false
            }
        },
        components: { draggable },
        methods: {
            dragged() {
                this.sorted = true
            },
            updateRank() {
                const items = this.sortedItems.map((item) => { return item.id });
                const category_id = this.sortedItems[0].category_id;

                axios.put(`https://britecore-backend-flask.herokuapp.com/item/${category_id}/rank`, { items }, { withCredentials: true })
                .then((res) => {
                    this.sortedItems = res.data;
                    this.sorted = false
                })
                .catch((err) => console.log(err))
            }
        }
    }
</script>

<style scoped>
    tbody {
        cursor: all-scroll;
    }
    .btn {
        width: 100%;
    }
</style>

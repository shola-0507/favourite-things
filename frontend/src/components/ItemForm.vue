<template>
    <div class="container">
        <div v-if="alert">
            <Alert v-bind:message="alert"/>
        </div>
        <form>
            <div class="form-row">
                <div class="col padding">
                    <input type="text" class="form-control" id="title" name="title" placeholder="Please Enter a title">
                </div>
                <div class="col padding">
                    <select class="form-control" id="category" v-model="category_id">
                        <option selected="selected" v-bind:value="null">Please Select a Category</option>
                        <option v-bind:key="category.id" v-for="category in categories" v-bind:value="category.id">{{ category.name }}</option>
                    </select>
                </div>
                <div class="col-md-12 padding">
                    <textarea class="form-control" id="description" rows="3" placeholder="Please Enter a Description"></textarea>
                </div>
                
                <div class="col-md-12">
                    <p>
                        Optional Meta Information
                        <span class="btn btn-link" @click="addMeta">+</span>
                    </p>
                </div>
            </div>

            <div id="meta" ref="container"></div>
            <input type="button" class="btn btn-success full-width" value="Create Item" @click="addItem"/>
        </form>
    </div>
</template>

<script>
    import Vue from 'vue';
    import axios from 'axios';
    import metaData from './metaData';
    import Alert from './layout/Alert';

    export default {
        name: 'ItemForm',
        components: { metaData, Alert },
        data() {
            return {
                categories: [],
                category_id: null,
                meta_counter: 0,
                alert: null
            }
        },
        methods: {
            addMeta() {
                this.meta_counter++;
                const metaComponent = Vue.extend(metaData);
                const instance = new metaComponent({
                    propsData: { id: this.meta_counter }
                });

                instance.$mount();
                this.$refs.container.appendChild(instance.$el);
            },
            addItem() {
                const title = document.getElementById('title').value;
                const category_id = parseInt(document.getElementById('category').value);
                const description = document.getElementById('description').value;
                const meta = this.getMetaData();
                const body = {
                    title, category_id, description, meta
                }

                axios.post('https://britecore-backend-flask.herokuapp.com/item/create', body, {withCredentials: true})
                .then((res) => {
                    console.log(res.data)
                    this.alert = {
                        class: "alert-success",
                        data: "Favourite thing created"
                    } 
                })
                .catch(err => console.log(err))
            },
            getMetaData() {
                const response = [];
                for (let index = 1; index <= this.meta_counter; index++) {
                    const type = document.getElementById("type-" + index).value.toString();
                    const name = document.getElementById("key-" + index).value.toString();
                    const data = document.getElementById("value-" + index).value.toString();
                    
                    response.push({
                        name,
                        data,
                        type
                    });
                }

                return response;
            }
        },
        mounted() {
            axios.get('https://britecore-backend-flask.herokuapp.com/category/all', {withCredentials: true})
            .then(res => this.categories = res.data)
            .catch(err => console.log(err))
        }
    }
</script>

<style>
    .full-width {
        width: 100%
    }
    .padding {
        padding: 10px;
    }
</style>

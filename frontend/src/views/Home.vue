<template>
    <div id="app" class="container">
      <Header />
      <div v-if="error">
        <Alert v-bind:message="error"/>
      </div>
      <div class="form-group row">
          <label for="exampleFormControlSelect1" class="col-sm-4">Please select a category</label>
          <div class="col-sm-8">
              <select class="form-control" id="categories" @change="getItems(category_id)" v-model="category_id">
                <option v-bind:key="category.id" v-for="category in categories" v-bind:value="category.id">{{ category.name }}</option>
              </select>
          </div>
      </div>
      <div v-if="items.length">
        <Items v-bind:items="items" class="item"/>
      </div>
    </div>
</template>

<script>
  import Header from '../components/layout/Header';
  import Alert from '../components/layout/Alert';
  import Items from '../components/Items';
  import axios from 'axios';

  export default {
      name: 'Home',
      components: {
        Header,
        Alert,
        Items
      },
      data() {
        return {
          category_id: "",
          categories: [],
          items: [],
          error: null
        }
      },
      methods: {
        getItems(category_id) {
          this.error = null
          this.items = []
          
          axios.get(`https://britecore-backend-flask.herokuapp.com/item/${category_id}/all`, { withCredentials: true })
          .then(res => this.items = res.data)
          .catch((err) => { 
            this.error = {
              class: 'alert-warning',
              data: err.response.data.error }
          });
        }
      },
      mounted() {
        axios.get('https://britecore-backend-flask.herokuapp.com/category/all', { withCredentials: true })
        .then(res => this.categories = res.data)
        .catch(err => console.log(err))
      }
  }
</script>

<style>
  #app {
    font-family: 'Avenir', Helvetica, Arial, sans-serif;
    -webkit-font-smoothing: antialiased;
    -moz-osx-font-smoothing: grayscale;
    text-align: center;
    color: #2c3e50;
    margin-top: 60px;
  }
</style>
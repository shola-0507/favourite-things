<template>
    <div>
        <ul class="nav justify-content-center">
            <router-link class="nav-link active" to="/">Favourite Things</router-link>
            <router-link class="nav-link" to="/createCategory">Add Category</router-link>
            <router-link class="nav-link" to="/createItem">Add Favourite Thing</router-link>
            <router-link class="nav-link" to="/logs">Audit Logs</router-link>
        </ul>
    </div>
</template>

<script>
export default {
    name: 'Header'
}
</script>

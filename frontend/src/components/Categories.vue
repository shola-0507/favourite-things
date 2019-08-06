<template>
    <div>
        <table class="table">
            <thead class="thead-dark">
                <tr>
                    <th scope="col">Name</th>
                    <th scope="col">Created At</th>
                </tr>
            </thead>
            <tbody>
                <tr v-bind:key="category.id" v-for="category in categories">
                    <td>{{ category.name }}</td>
                    <td>{{ new Date(category.created_date).toString() }}</td>
                </tr>
            </tbody>
        </table>
    </div>
</template>

<script>
    export default {
        name: "CategoryForm",
        props: ["categories"]
    }
</script>
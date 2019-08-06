<template>
    <div id="app" class="container">
        <Header />
        <p>Hi there, you can create items here.</p>
        <ItemForm />
    </div>
</template>

<script>
    import Header from '../components/layout/Header';
    import Alert from '../components/layout/Alert';
    import ItemForm from '../components/ItemForm'

    export default {
        name: 'CreateItem',
        components: {
            Header,
            Alert,
            ItemForm
        }
    }
</script>


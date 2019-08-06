<template>
    <div class="alert alert-dismissible fade show" v-bind:class="message.class" role="alert">
        {{ message.data }}
        <button type="button" class="close" data-dismiss="alert" aria-label="Close">
            <span aria-hidden="true">&times;</span>
        </button>
    </div>
</template>

<script>
export default {
    name: 'Alert',
    props: ['message']
}
</script>

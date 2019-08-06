<template>
    <div>
        <div class="form-row padding" id="metadata">
            <div class="col">
                <select class="form-control" v-bind:id="'type-' + id" @change="changeKeyField(id)">
                    <option value="String">Text</option>
                    <option value="Date">Date</option>
                </select>
            </div>
            <div class="col">
                <input type="text" class="form-control" v-bind:id="'key-' + id" placeholder="Please Enter a Key">
            </div>
            <div class="col">
                <input type="text" class="form-control" v-bind:id="'value-' + id" placeholder="Please Enter a Value">
            </div>                        
        </div>
    </div>
</template>

<script>
    export default {
        name: "metaData",
        props: ["id"],
        methods: {
            changeKeyField(id) {
                const name = "value-" + id;
                const inputField = document.getElementById(name);

                if (inputField.getAttribute("type") === "text") {
                    inputField.setAttribute("type", "datetime-local");
                } else {
                    inputField.setAttribute("type", "text");
                }
            }
        }
    }
</script>
<template>
    <div class="my-3 mx-4">
        <h2 class="my-2 ml-3">Current Habits</h2>
        <v-sheet class="w-100">
            <div>
                <HabitCreate/>
            </div>
            <div class="d-flex justify-center">
                <v-data-table :headers="habitHeaders" :items="habitList" class="t-spacing">
                    <template v-slot:item.actions="{ item }">
                        <div class="d-flex ga-2 justify-start">
                            <v-icon color="medium-emphasis" icon="mdi-pencil" size="small" @click="edit(item.id)"></v-icon>
                            <v-icon color="medium-emphasis" icon="mdi-delete" size="small" @click="remove(item.id)"></v-icon>
                        </div>
                    </template>
                </v-data-table>
            </div>
           
        </v-sheet>
    </div>
</template>

<script setup>
import axios from 'axios'
import { useUserStore } from '@/stores/user'

const userStore = useUserStore()
const {userId, username} = storeToRefs(userStore)
const habitHeaders = [
    { title: 'Created Date', key: 'created_date' },
    { title: 'Name', key: 'name' },
    { title: 'Description', key: 'description', sortable: false },
    { title: 'Classification', key: 'classification' },
    { title: 'Actions', key: 'actions', sortable: false}
]
const habitList = ref([])

onMounted(() => {
    getHabits()
})

async function getHabits()
{
    let url = 'http://127.0.0.1:5000/habit'
    if(userId.value == '')
    {
        userId.value = '1'
    }

    let data = {
        user_id: userId.value
    }
    let headers = {
        headers: {
            "Content-Type": "application/json"
        }
    }
    await axios
    .post(url, data, headers)
    .then(response => {
        habitList.value = response.data
        console.log(habitList.value)
    })
    .catch(err => console.error("Network or parsing error:", err))
}
</script>

<style>
    .t-spacing{
        margin-top: 10px;
        margin-bottom: 15px;
        width: 95%
    }
</style>
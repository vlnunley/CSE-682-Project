<template>
    <div class="my-3 mx-4">
        <h2 class="my-2 ml-3">{{ habitName }} - Entries</h2>
        <v-sheet class="w-100">
            <div>
                <HabitEntryCreate @closed="getHabitEntries()"/>
            </div>
            <div class="d-flex justify-center">
                <v-data-table :headers="habitEntryHeaders" :items="habitEntryList" class="t-spacing">
                    <template v-slot:item.actions="{ item }">
                        <div class="d-flex ga-2 justify-start">
                            <v-icon color="medium-emphasis" icon="mdi-pencil" size="small" @click="editHabit(item.id)"></v-icon>
                            <v-icon color="medium-emphasis" icon="mdi-delete" size="small" @click="removeHabit(item.id)"></v-icon>
                        </div>
                    </template>
                </v-data-table>
            </div>
           
        </v-sheet>
    </div>
</template>

<script setup>
import axios from 'axios'
import { useHabitStore } from '@/stores/habit'

const habitStore = useHabitStore()
const {habitId, habitName, habitDescription, habitClassification, habitCreatedDate} = storeToRefs(habitStore)
const habitEntryHeaders = [
    { title: 'Created Date', key: 'created_date', width:'20%'},
    { title: 'Note', key: 'note', sortable: false, width:'35%'},
    { title: 'Status', key: 'status'},
    { title: 'Actions', key: 'actions', sortable: false, width:'10%'}
]
const habitEntryList = ref([])

onMounted(() => {
    getHabitEntries()
})

async function getHabitEntries()
{
    let url = 'http://127.0.0.1:5000/habit_entry'

    if(habitId.value == '')
    {
        habitId.value = '1'
    }

    let data = {
        habit_id: habitId.value
    }
    let headers = {
        headers: {
            "Content-Type": "application/json"
        }
    }
    await axios
    .post(url, data, headers)
    .then(response => {
        habitEntryList.value = response.data
        console.log(habitEntryList.value)
    })
    .catch(err => console.error("Network or parsing error:", err))
}

async function editHabitEntry(habit_id)
{
   
}

async function removeHabitEntry(habit_id)
{
    
}
</script>

<style>
    .t-spacing{
        margin-top: 10px;
        margin-bottom: 15px;
        width: 95%
    }
</style>
<template>
    <v-dialog max-width="500">
        <template v-slot:activator="{ props: activatorProps }">
            <v-btn 
                v-bind="activatorProps"
                class="mt-3 ml-3" 
                color="teal-darken-3"
                text="Create Habit Entry"
            ></v-btn>
        </template>

        <template v-slot:default="{ isActive }">
            <v-card title="Create Habit Entry" class="bg-teal-darken-3">
                <v-card-text class="bg-grey-darken-4">
                    <div class="mt-4 text-subtitle-1 text-medium-emphasis d-flex align-center justify-space-between">
                        Status
                    </div>
                    <v-select
                        v-model="selectedStatus"
                        clearable
                        density="compact"
                        label="Status"
                        :items="['Completed', 'Missed']"
                    ></v-select>
                    <div class="text-subtitle-1 text-medium-emphasis d-flex align-center justify-space-between">
                        Notes
                    </div>
                    <v-textarea
                        clear-icon="mdi-close-circle"
                        label="Entry Notes"
                        v-model="entryNote"
                        clearable
                    ></v-textarea>
                </v-card-text>
                <v-card-actions class="bg-grey-darken-4">
                    <v-spacer></v-spacer>
                    <v-btn
                        color="teal-lighten-1"
                        text="Create"
                        @click="createHabitEntry(isActive)"
                    ></v-btn>
                    <v-btn
                        color="amber-lighten-2"
                        text="Cancel"
                        @click="isActive.value = false"
                    ></v-btn>
                </v-card-actions>
            </v-card>
        </template>
    </v-dialog>
</template>

<script setup>
import axios from 'axios'
import { useHabitStore } from '@/stores/habit'

const emit = defineEmits(['closed'])
const habitStore = useHabitStore()
const {habitId, habitName, habitDescription, habitClassification, habitCreatedDate} = storeToRefs(habitStore)

const entryNote = ref('')
const selectedStatus = ref()

async function createHabitEntry(isActive)
{
    let url = 'http://127.0.0.1:5000/habit_entry/create'
    if(habitId.value == '')
    {
        habitId.value = '1'
    }

    let data = {
        habit_id: habitId.value,
        status: selectedStatus.value,
        note: entryNote.value,
        created_date: new Date()
    }
    let headers = {
        headers: {
            "Content-Type": "application/json"
        }
    }
    await axios
    .post(url, data, headers)
    .then(response => {
        console.log(response)
    })
    .catch(err => console.error("Network or parsing error:", err))
    isActive.value = false
    close()
}

function close() {
    emit('closed')
}
</script>
<template>
    <v-dialog max-width="500">
        <template v-slot:activator="{ props: activatorProps }">
            <v-btn 
                v-bind="activatorProps"
                class="mt-3 ml-3" 
                color="teal-darken-3"
                text="Create Habit"
            ></v-btn>
        </template>

        <template v-slot:default="{ isActive }">
            <v-card title="Create Habit" class="bg-teal-darken-3">
                <v-card-text class="bg-grey-darken-4">
                    <div class="mt-4 text-subtitle-1 text-medium-emphasis d-flex align-center justify-space-between">
                        Name
                    </div>
                    <v-text-field
                        density="compact"
                        v-model="habitName"
                        placeholder="Habit Name"
                        variant="outlined"
                    ></v-text-field>
                    <div class="text-subtitle-1 text-medium-emphasis d-flex align-center justify-space-between">
                        Description
                    </div>
                    <v-text-field
                        density="compact"
                        v-model="habitDescription"
                        placeholder="Habit Description"
                        variant="outlined"
                    ></v-text-field>
                    <div class="text-subtitle-1 text-medium-emphasis d-flex align-center justify-space-between">
                        Classification
                    </div>
                    <v-select
                        v-model="selectedClassification"
                        clearable
                        density="compact"
                        label="Classification"
                        :items="['Positive', 'Negative', 'Neutral']"
                    ></v-select>
                </v-card-text>
                <v-card-actions class="bg-grey-darken-4">
                    <v-spacer></v-spacer>
                    <v-btn
                        color="teal-lighten-1"
                        text="Create"
                        @click="createHabit"
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
import { useUserStore } from '@/stores/user'

const userStore = useUserStore()
const {userId, username} = storeToRefs(userStore)

const habitName= ref('')
const habitDescription = ref('')
const selectedClassification = ref()
const isActive = ref(false)

async function createHabit()
{
    let url = 'http://127.0.0.1:5000/habit/create'
    if(userId.value == '')
    {
        userId.value = '1'
    }

    let data = {
        user_id: userId.value,
        name: habitName.value,
        description: habitDescription.value,
        classification: selectedClassification.value,
        created_date: new Date().toLocaleString()
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
}
</script>
<template>
    <v-dialog max-width="500">
        <template v-slot:activator="{ props: activatorProps }">
            <v-btn 
                v-bind="activatorProps"
                class="mt-3 ml-3" 
                color="teal-darken-3"
                text="Log Mood"
            ></v-btn>
        </template>

        <template v-slot:default="{ isActive }">
            <v-card title="Log Mood" class="bg-teal-darken-3">
                <v-card-text class="bg-grey-darken-4">
                    <div class="mt-4 text-subtitle-1 text-medium-emphasis d-flex align-center justify-space-between">
                        Mood:
                    </div>
                    <v-select
                        v-model="selectedMood"
                        clearable
                        density="compact"
                        label="Status"
                        :items="moodItems"
                        item-title="name"
                        item-value="id"
                    >
                    </v-select>
                    <div class="text-subtitle-1 text-medium-emphasis d-flex align-center justify-space-between">
                        Note:
                    </div>
                    <v-textarea
                        clear-icon="mdi-close-circle"
                        label="Log Notes"
                        v-model="moodNote"
                        clearable
                    ></v-textarea>
                </v-card-text>
                <v-card-actions class="bg-grey-darken-4">
                    <v-spacer></v-spacer>
                    <v-btn
                        color="teal-lighten-1"
                        text="Create"
                        @click="createMood(isActive)"
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

const emit = defineEmits(['closed'])
const moodNote= ref('')
const selectedMood = ref()
const moodItems = ref([])

onMounted(() => {
    getMoodList()
})

async function getMoodList()
{
    let url = 'http://127.0.0.1:5000/mood/emojis'

    const response = await axios.get(url)
    console.log(response.data)
    moodItems.value = response.data

    console.log(moodItems.value)
}

async function createMood(isActive)
{
    let url = 'http://127.0.0.1:5000/mood/create'
    if(userId.value == '')
    {
        userId.value = '1'
    }

    let data = {
        user_id: userId.value,
        note: moodNote.value,
        mood_id: selectedMood.value,
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
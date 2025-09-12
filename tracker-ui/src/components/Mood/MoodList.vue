<template>
    <div class="my-3 mx-4">
        <h2 class="my-2 ml-3">Past Moods</h2>
        <v-sheet class="w-100">
            <div>
                <MoodCreate @closed="getMoodEntries()"/>
            </div>
            <div class="d-flex justify-center">
                <v-data-table :headers="moodHeaders" :items="moodList" class="t-spacing">
                    <template v-slot:item.actions="{ item }">
                        <div class="d-flex ga-2 justify-start">
                            <v-icon color="medium-emphasis" icon="mdi-delete" size="small" @click="removeMood(item.id)"></v-icon>
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
import { useRouter } from 'vue-router';

const router = useRouter()
const userStore = useUserStore()
const {userId, username} = storeToRefs(userStore)
const moodHeaders = [
    { title: 'Created Date', key: 'created_date', width:'20%'},
    { title: 'Mood', key: 'mood', width:'15%' },
    { title: 'Note', key: 'note', sortable: false }
]
const moodList = ref([])

onMounted(() => {
    getMoodEntries()
})


async function getMoodEntries()
{
    let url = 'http://127.0.0.1:5000/mood'
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
    const response = await axios.post(url, data, headers)
    moodList.value = response.data
    console.log(moodList.value)
}

async function removeMood(mood)
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
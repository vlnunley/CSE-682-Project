<template>
    <div>
        <v-img
        class="mx-auto"
        :width="350"
        aspect-ratio="16/9"
        cover
        src="../../assets/habitlogo.png"
        ></v-img>
        <v-form class="mb-3" v-model="valid">
           <v-card
            class="w-25 my-auto mx-auto pa-12 pb-8"
            elevation="8"
            rounded="lg"
            >
                <v-card-title class="text-center mb-3">Account Login</v-card-title>

                <div class="text-subtitle-1 text-medium-emphasis">Username</div>

                <v-text-field
                    density="compact"
                    placeholder="Username"
                    v-model="username"
                    prepend-inner-icon="mdi-account-outline"
                    variant="outlined"
                ></v-text-field>

                <div class="text-subtitle-1 text-medium-emphasis d-flex align-center justify-space-between">
                    Password
                    <a
                    class="text-caption text-decoration-none text-blue"
                    href="#"
                    rel="noopener noreferrer"
                    target="_blank"
                    >
                    Forgot login password?</a>
                </div>

                <v-text-field
                    :append-inner-icon="visible ? 'mdi-eye-off' : 'mdi-eye'"
                    :type="visible ? 'text' : 'password'"
                    density="compact"
                    v-model="password"
                    placeholder="Enter your password"
                    prepend-inner-icon="mdi-lock-outline"
                    variant="outlined"
                    @click:append-inner="visible = !visible"
                ></v-text-field>

                <v-btn
                    class="mb-8"
                    color="blue"
                    size="large"
                    variant="tonal"
                    block
                    @click="login"
                >
                    Log In
                </v-btn>

                <v-card-text class="text-center">
                    <div>Don't have an Account?</div>
                    <a
                    class="text-blue text-decoration-none"
                    href="/register"
                    rel="noopener noreferrer"
                    >
                        Sign up
                    </a>
                </v-card-text>
            </v-card>
        </v-form>
        <v-snackbar
            v-model="snackbar"
            timeout="3000"
            color="error"
        >
            {{ message }}
            <template v-slot:actions>
                <v-btn
                variant="text"
                @click="snackbar = false"
                >
                X
                </v-btn>
            </template>
        </v-snackbar>
    </div>
</template>


<script setup>
import { useRouter } from 'vue-router';
import axios from 'axios'
import { useUserStore } from '@/stores/user'

const userStore = useUserStore()
const valid = ref(false)
const username = ref('')
const password = ref('')
const router = useRouter()
const message = ref('')
const snackbar = ref(false)
const visible = ref(false)

async function login()
{
    let url = 'http://127.0.0.1:5000/user/'+username.value
    await axios
    .get(url)
    .then(response => {
        console.log(response)
        if(response.data.data["password"] == password.value)
        {
            router.push("/home")
            userStore.$patch({
                userId: response.data.data["id"],
                username: response.data.data["username"]
            })
        }
        else{
            message.value = "Incorrect Username or Password."
            snackbar.value = true
        }
    })
    .catch(err => console.error("Network or parsing error:", err))
}

</script>
<template>
        <div>
        <v-img
        class="mx-auto"
        :width="350"
        aspect-ratio="16/9"
        cover
        src="../../assets/habitlogo.png"
        ></v-img>
        
        <v-form class="mb-4" v-model="valid">
           <v-card
            class="w-25 my-auto mx-auto pa-12 pb-8"
            elevation="8"
            rounded="lg"
            >
                <v-card-title class="text-center mb-3">Account Registration</v-card-title>
                <div class="text-subtitle-1 text-medium-emphasis">
                    Username
                </div>

                <v-text-field
                    density="compact"
                    placeholder="Username"
                    v-model="username"
                    prepend-inner-icon="mdi-account-outline"
                    variant="outlined"
                    :rules="usenameRules"
                    required
                ></v-text-field>

                <div class="text-subtitle-1 text-medium-emphasis">
                    Email
                </div>

                <v-text-field
                    density="compact"
                    placeholder="Email"
                    v-model="email"
                    prepend-inner-icon="mdi-email-outline"
                    variant="outlined"
                    :rules="emailRules"
                    required
                ></v-text-field>

                <div class="text-subtitle-1 text-medium-emphasis d-flex align-center justify-space-between">
                    Password
                </div>

                <v-text-field
                    :append-inner-icon="visible ? 'mdi-eye-off' : 'mdi-eye'"
                    :type="visible ? 'text' : 'password'"
                    density="compact"
                    placeholder="Enter password"
                    v-model="password"
                    prepend-inner-icon="mdi-lock-outline"
                    variant="outlined"
                    @click:append-inner="visible = !visible"
                    :rules="passwordRules"
                    required
                ></v-text-field>

                <div class="text-subtitle-1 text-medium-emphasis d-flex align-center justify-space-between">
                    Confirm Password
                </div>

                <v-text-field
                    :append-inner-icon="revisible ? 'mdi-eye-off' : 'mdi-eye'"
                    :type="revisible ? 'text' : 'password'"
                    density="compact"
                    placeholder="Re-enter password"
                    v-model="confirmPassword"
                    prepend-inner-icon="mdi-lock-outline"
                    variant="outlined"
                    @click:append-inner="revisible = !revisible"
                    :rules="confirmPasswordRules"
                    required
                ></v-text-field>

                <v-btn
                    class="mb-8"
                    color="blue"
                    size="large"
                    variant="tonal"
                    block
                    @click="createAccount"
                >
                    Sign Up
                </v-btn>

                <v-card-text class="text-center">
                    <div>Have an Account?</div>
                    <a
                    class="text-blue text-decoration-none"
                    href="/"
                    rel="noopener noreferrer"
                    >
                        Login
                    </a>
                </v-card-text>
            </v-card>
        </v-form>
        <v-snackbar
        v-model="snackbar"
        timeout="3000"
        :color="snackError ? 'error': 'success'"
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
import axios from 'axios'

const valid = ref(false)
const username = ref('')
const password = ref('')
const email = ref('')
const confirmPassword = ref('')
const isRegister = ref(false)
const visible = ref(false)
const revisible = ref(false)
const snackbar = ref(false)
const snackError = ref(false)
const message = ref('')

const usenameRules = [
    value => {
        if (value) return true
        return 'Username is required.'
    }
]
const emailRules = [
    value => {
        if (value) return true
        return 'Email is required.'
    },
    value => {
        if (/.+@.+\..+/.test(value)) return true
        return 'Email must be valid.'
    }
]
const passwordRules = [
    value => {
        if (value) return true
        return 'Password is required.'
    },
    value => {
        if (/[A-Z]/.test(value)) return true
        return 'Password requires uppercase.'
    },
    value => {
        if (/[a-z]/.test(value)) return true
        return 'Password requires lowercase.'
    },
    value => {
        if (/[0-9]/.test(value)) return true
        return 'Password requires a number.'
    }
]
const confirmPasswordRules = [
    value => {
        if (value == password.value) return true
        return 'Passwords do not match'
    }
]

async function createAccount(e) {
    console.log(e)
    message.value = "Account Successfully Created."
    let newUser = {
        "username": username.value,
        "password": password.value,
        "email": email.value
    }

    await axios
        .post('http://127.0.0.1:5000/user/create', newUser, {
            headers: {
                "Content-Type": "application/json"
            }}
        )
        .then(response => {
            console.log(response)
            if(response.data.success)
            {
                console.log("User Data:", response.data.data)
                snackError.value = false
                snackbar.value = true
            }
            else {
                console.error("Error: ", response.data.error)
                message.value = "Username already in use."
                snackError.value = true
                snackbar.value = true
            }
        })
        .catch(err => console.error("Network or parsing error:", err))

}

</script>
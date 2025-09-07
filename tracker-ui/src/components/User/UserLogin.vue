<template>
    <div>
        <v-img
        class="mx-auto my-6"
        :width="350"
        aspect-ratio="16/9"
        cover
        src="../../assets/habitlogo.png"
        ></v-img>
        <v-form class="" v-model="valid">
           <v-card
            class="w-25 my-auto mx-auto pa-12 pb-8"
            elevation="8"
            rounded="lg"
            >
                <div class="text-subtitle-1 text-medium-emphasis">Account</div>

                <v-text-field
                    density="compact"
                    placeholder="Username"
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
                >
                    Log In
                </v-btn>

                <v-card-text class="text-center">
                    <a
                    class="text-blue text-decoration-none"
                    href="#"
                    rel="noopener noreferrer"
                    target="_blank"
                    >
                    Sign up now <v-icon icon="mdi-chevron-right"></v-icon>
                    </a>
                </v-card-text>
            </v-card>
        </v-form>
    </div>
</template>

<script setup>
</script>
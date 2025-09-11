<template>
  <v-container class="fill-height">
    <div class="d-flex w-100 justify-space-around">
        <v-card title="Habit Tracker" class="text-center w-33 bg-teal-darken-3">
            <v-card-text class="d-flex bg-surface-light pt-4 ga-3 justify-center">
                <!-- <v-btn prepend-icon="mdi-notebook-plus" href="/habit/create">Create Habit</v-btn> -->
                <v-btn prepend-icon="mdi-notebook-multiple" href="/habit/list">View Habits</v-btn>
            </v-card-text>
        </v-card>
        <v-card title="Mood Tracker" class="text-center w-33 bg-teal-darken-3">
            <v-card-text class="d-flex bg-surface-light pt-4 ga-3 justify-center">
                <!-- <v-btn prepend-icon="mdi-heart-plus">Log Mood</v-btn> -->
                <v-btn prepend-icon="mdi-heart-multiple">View Mood Entries</v-btn>
            </v-card-text>
        </v-card>
    </div>
  </v-container>
</template>

<script setup>
</script>

<style>

</style>
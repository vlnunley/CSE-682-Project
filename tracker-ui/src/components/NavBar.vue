<template>
    <v-app-bar
        color="dark"
      >
        <template v-slot:prepend>
            <v-app-bar-nav-icon class="mr-3"  @click.stop="drawer = !drawer"></v-app-bar-nav-icon>
            <v-img
                :width="75"
                aspect-ratio="16/9"
                cover
                src="../assets/trackericon.png"
            ></v-img>
        </template>

        <v-app-bar-title>Habit & Mood Tracker</v-app-bar-title>

        <template v-slot:append>
          <v-btn icon="mdi-cog" class="mr-2" ></v-btn>
        </template>
    </v-app-bar>
    <v-navigation-drawer
        v-model="drawer"
        temporary
      >
        <v-list density="compact" nav>
            <v-list-item prepend-icon="mdi-home" title="Home" value="home" href="/home"></v-list-item>
            <v-divider class="mb-3"></v-divider>
            <span>Habit Tracker</span>
            <!-- <v-list-item prepend-icon="mdi-notebook-plus" title="Create Habit" value="create_habit" href="/habit/create"></v-list-item> -->
            <v-list-item prepend-icon="mdi-notebook-multiple" title="View Habits" value="list_habit" href="/habit/list"></v-list-item>
            <v-divider class="mb-3"></v-divider>
            <span>Mood Tracker</span>
            <!-- <v-list-item prepend-icon="mdi-heart-plus" title="Log Mood" value="log_mood" href="/mood/create"></v-list-item> -->
            <v-list-item prepend-icon="mdi-heart-multiple" title="View Mood Entries" value="list_mood" href="/mood/list"></v-list-item>
        </v-list>
      </v-navigation-drawer>
</template>

<script setup>
  const drawer = ref(null)


</script>
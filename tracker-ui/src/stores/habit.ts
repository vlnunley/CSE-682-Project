// Utilities
import { defineStore } from 'pinia'

export const useHabitStore = defineStore('habit', {
  state: () => ({
    habitId: '',
    habitName: '',
    habitDescription: '',
    habitClassification: '',
    habitCreatedDate: ''
  }),
})

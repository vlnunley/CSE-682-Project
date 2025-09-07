new_user = """
    INSERT INTO user (username, password, email, phoneNumber)
    VALUES (?, ?, ?, ?)
"""

new_habit = """
    INSERT INTO habit (name, isActive, classification, userId)
    VALUES (?, ?, ?, ?)
"""

new_habit_entry = """
    INSERT INTO habitEntry (note, status, habitId, goalId)
    VALUES (?, ?, ?, ?)
"""

new_goal = """
    INSERT INTO goal (name, frequencyNum, frequencyType, habitId)
    VALUES (?, ?, ?, ?)
"""

new_mood_entry = """
    INSERT INTO moodEntry (mood, note, userId)
    VALUES (?, ?, ?)
"""

new_correlation = """
    INSERT INTO correlation (moodEntryId, habitId)
    VALUES (?, ?)
"""

get_all_habits = """

"""
get_all_habit_entries = """
    SELECT * FROM habitEntry 
    WHERE habitId = ?
"""
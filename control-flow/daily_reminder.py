# daily_reminder.py

# Prompt user for task description
task = input("Enter your task: ")

# Prompt user for task priority
priority = input("Priority (high/medium/low): ").lower()

# Prompt user to check if task is time-bound 
time_bound = input("Is it time-bound? (yes/no): ").lower()

# Initialise a reminder variable
reminder = f"'{task}' has an undefined priority level."

# Process the task based on priority and time sensitivity
match priority:
    case "high":
        reminder = f"'{task}' is a high priority task"
    case "medium":
        reminder = f"'{task}' is a medium priority task"
    case "low":
        reminder = f"'{task}' is a low priority task."
    case _:
        print("Invalid priority level entered.")
        reminder = None

if reminder:
    # Check if the task is time-bound
    if time_bound == "yes":
        reminder += " that requires immediate attention today!"
    else:
        reminder += " Consider completing it when you have free time."

    # Provide a customized reminder
    print("\nReminder:", reminder)

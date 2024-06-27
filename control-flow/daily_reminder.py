# daily_reminder.py

# Prompt user for task description
task = input("Enter your task: ")

# Prompt user for task priority
priority = input("Priority (high/medium/low): ").lower()

# Prompt user to check if task is time-bound 
time_bound = input("Is it time-bound? (yes/no): ").lower()

# Initialise a reminder variable
reminder = f"'{task}' has an undefined priority level."

# Initialise a reminder variable
reminder = f"'{task}' has an undefined priority level."

# Process the task based on priority and time sensitivity
match priority:
    case "high":
        print(f"\nReminder: '{task}' is a high priority task", end="")
    case "medium":
        print(f"\nReminder: '{task}' is a medium priority task", end="")
    case "low":
        print(f"\nNote: '{task}' is a low priority task.", end="")
    case _:
        print("Invalid priority level entered.")

# Check if the task is time-bound
if time_bound == "yes":
    print(" that requires immediate attention today!")
else:
    print(" Consider completing it when you have free time.")

# Provide a customised reminder
print("\nReminder:", reminder)
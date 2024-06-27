# daily_reminder.py

# Prompt user for input for a single task

task = input("Enter your task: ")
priority = input("Priority (high/medium/low): ")
time_bound = input("Is it time-bound? (yes/no): ")

# Process the task based on priority and time sensitivity

match priority:
    case "high":
        print("\nReminder: ")
        print(f"'{task}' is a high priority task ", end="")
    case "medium":
        print("\nReminder: ")
        print(f"'{task}' is a medium priority task ", end="")
    case "low":
        print("\nNote: ")
        print(f"'{task}' is a low priority task. ", end="")
    case _:
        print("Invalid priority level entered.")

# Check if the task is time-bound
if time_bound_variable == "yes":
    print("that requires immediate attention today!")
else:
    print("Consider completing it when you have free time.")
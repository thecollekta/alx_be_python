# daily_reminder.py

# Prompt user for input for a single task

task_variable = input("Enter your task: ")
priority_variable = input("Priority (high/medium/low): ")
time_bound_variable = input("Is it time-bound? (yes/no): ")

# Process the task based on priority and time sensitivity

match priority_variable:
    case "high":
        print("\nReminder: ")
        print(f"'{task_variable}' is a high priority task ", end="")
    case "medium":
        print("\nReminder: ")
        print(f"'{task_variable}' is a medium priority task ", end="")
    case "low":
        print("\nNote: ")
        print(f"'{task_variable}' is a low priority task. ", end="")
    case _:
        print("Invalid priority level entered.")

# Check if the task is time-bound
if time_bound_variable == "yes":
    print("that requires immediate attention today!")
else:
    print("Consider completing it when you have free time.")
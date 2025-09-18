task = input("Enter your task: ")

while True:
    priority = input("Priority (high/medium/low): ").strip().lower()
    if priority not in ["high", "medium", "low"]:
        print("Invalid priority level. Please enter high, medium, or low.")
        continue
    break

while True:
    time_bound = input("Is it time-bound? (yes/no): ").strip().lower()
    if time_bound not in ["yes", "no"]:
        print("Invalid input. Please enter 'yes' or 'no'.")
        continue
    break

match priority:
    case "high":
        message = f"'{task}' is a high priority task"
        if time_bound == 'yes':
            print(f"Reminder:  '{task}' is a high priority task that requires immediate attention today!")
        else:
            print(f"Note:  '{task}' is a high priority task. But, consider completing it when you have free time.")
    case "medium":
        if time_bound == 'yes':
            print(f"Reminder:  '{task}' is a medium priority task that requires immediate attention today!")
        else:
            print(f"Note:  '{task}' is a medium priority task. Consider completing it when you have free time.")
    case "low":
        if time_bound == 'yes':
            print(f"Reminder:  '{task}' is a low priority task that requires immediate attention today!")
        else:
            print(f"Note:  '{task}' is a low priority task. Consider completing it when you have free time.")
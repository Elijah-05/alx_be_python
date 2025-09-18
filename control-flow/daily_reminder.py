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
    case "medium":
        message = f"'{task}' is a medium priority task"
    case "low":
        message = f"'{task}' is a low priority task"

match time_bound:
    case "yes":
        message += " that requires immediate attention today!"
    case "no":
        message +=  ". Consider completing it when you have free time."

print(message)

task = input("Enter your task: ")
priority = input("Priority (high, medium, low): ").strip().lower()
time_bound = input("Is it time-bound? (yes or no): ").strip().lower()

match priority:
    case "high":
        reminder = f"{task} is a high-priority task."
        if time_bound == "yes":
            reminder += " It requires immediate attention today!"
    case "medium":
        reminder = f"{task} is a medium-priority task."
        if time_bound == "yes":
            reminder += " Consider scheduling it for today."
    case "low":
        reminder = f"{task} is a low-priority task."
        if time_bound == "yes":
            reminder += " You might want to address it soon."
    case _:
        reminder = "Invalid priority level. Please specify high, medium, or low."

print(reminder)

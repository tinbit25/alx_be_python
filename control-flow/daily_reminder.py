def get_user_input():
    task = input("Enter your task: ").strip()
    
    # Ensure the task is not empty
    if not task:
        print("Task cannot be empty.")
        return None, None, None

    priority = input("Priority (high, medium, low): ").strip().lower()
    
    # Ensure the priority is valid
    if priority not in ["high", "medium", "low"]:
        print("Invalid priority level. Please specify high, medium, or low.")
        return None, None, None

    time_bound = input("Is it time-bound? (yes or no): ").strip().lower()

    # Ensure time_bound is valid
    if time_bound not in ["yes", "no"]:
        print("Invalid response for time-bound. Please answer with 'yes' or 'no'.")
        return None, None, None

    return task, priority, time_bound

def generate_reminder(task, priority, time_bound):
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
    
    return reminder

def main():
    task, priority, time_bound = get_user_input()
    
    if task and priority and time_bound:
        reminder = generate_reminder(task, priority, time_bound)
        print(reminder)

if __name__ == "__main__":
    main()

def get_user_input():
    # Get task description from the user
    task = input("Enter your task: ").strip()
    
    # Get the priority level (high, medium, low)
    priority = input("Priority (high/medium/low): ").strip().lower()
    if priority not in ["high", "medium", "low"]:
        print("Invalid priority level. Please enter 'high', 'medium', or 'low'.")
        return None, None, None
    
    # Ask if the task is time-bound
    time_bound = input("Is it time-bound? (yes/no): ").strip().lower()
    if time_bound not in ["yes", "no"]:
        print("Invalid response. Please answer 'yes' or 'no'.")
        return None, None, None

    return task, priority, time_bound

def generate_reminder(task, priority, time_bound):
    # Use match case to handle different priority levels
    match priority:
        case "high":
            reminder = f"'{task}' is a high priority task"
            if time_bound == "yes":
                reminder += " that requires immediate attention today!"
            else:
                reminder += ". You should try to complete it soon."
        case "medium":
            reminder = f"'{task}' is a medium priority task"
            if time_bound == "yes":
                reminder += " that should be completed soon."
            else:
                reminder += ". Consider completing it when you have time."
        case "low":
            reminder = f"'{task}' is a low priority task"
            if time_bound == "yes":
                reminder += " but you can handle it later."
            else:
                reminder += ". Consider completing it when you have free time."
        case _:
            reminder = "Invalid priority level."
    
    return reminder

def main():
    task, priority, time_bound = get_user_input()

    if task and priority and time_bound:
        reminder = generate_reminder(task, priority, time_bound)
        print("Reminder:", reminder)

if __name__ == "__main__":
    main()

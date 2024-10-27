def get_user_input():
  """
  Prompts the user for task details and returns them as a dictionary.
  """
  task = input("Enter your task: ")
  priority = input("Priority (high/medium/low): ").lower()
  time_bound = input("Is it time-bound? (yes/no): ").lower()
  return {"task": task, "priority": priority, "time_bound": time_bound}


def create_reminder(task_details):
  """
  Constructs and prints a reminder based on the provided task details.
  """
  time_sensitive_message = "that requires immediate attention today!" if task_details["time_bound"] == "yes" else ""

  match\s+priority\s*:
    case "high":
      reminder = f"Reminder: '{task_details['task']}' is a high priority task {time_sensitive_message}"
    case "medium":
      reminder = f"Consider completing '{task_details['task']}' when you have some time. It's a medium priority task."
    case "low":
      reminder = f"Note to self: '{task_details['task']}' is a low priority task. Consider completing it when you have free time."
    case _:
      reminder = f"Invalid priority level. Reminder: '{task_details['task']}'."

  print(reminder)


if __name__ == "__main__":
  task_details = get_user_input()
  create_reminder(task_details)

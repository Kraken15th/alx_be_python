# Get user input for task
task = input("Enter your task: ")
# Get user input for priority
while True:
    priority = input("Priority (high/medium/low): ").lower()
    if priority in ("high", "medium", "low"):
        break
    else:
        print("Invalid priority. Please enter high, medium, or low.")
        # Get user input for time sensitivity
        while True:
            time_bound = input("Is it time-bound? (yes/no): ").lower()
            if time_bound in ("yes", "no"):
             break
            else:
               print("Invalid input. Please enter yes or no.")
               # Generate reminder message
               message = f"'{task}' is a {priority} priority task."
               # Add time sensitivity information
               if time_bound == "yes":
                  message += " It requires immediate attention today!"
else:
   message += " Consider completing it when you have free time."
   # Print the reminder
   print(message)
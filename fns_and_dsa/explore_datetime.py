from datetime import datetime, timedelta


def display_current_datetime():
  """
  Gets the current date and time and prints it in a readable format.
  """
  current_date = datetime.now()
  formatted_date = current_date.strftime("%Y-%m-%d %H:%M:%S")
  print(f"Current date and time: {formatted_date}")


def calculate_future_date(days):
  """
  Calculates the future date by adding the specified number of days to the current date.
  """
  current_date = datetime.now()
  future_date = current_date + timedelta(days=days)
  formatted_date = future_date.strftime("%Y-%m-%d")
  print(f"Future date: {formatted_date}")


if __name__ == "__main__":
  display_current_datetime()

  while True:
    try:
      days = int(input("Enter the number of days to add to the current date (or 'q' to quit): "))
      if days == 'q':
        break
      calculate_future_date(days)
    except ValueError:
      print("Invalid input. Please enter an integer or 'q' to quit.")


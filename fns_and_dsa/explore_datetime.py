import datetime
def display_current_datetime():
    current_date = datetime.now()
    formatted_date = current_date.strftime("%Y-%m-%d %H:%M:%S")
    print(f"Current date and time: {formatted_date}")
def calculate_future_date(days):
 current_date = datetime.now()
 future_date = current_date + datetime.timedelta(days=days)
 formatted_date = future_date.strftime("%Y-%m-%d")
 print(f"Future date: {formatted_date}")
 if __name__ == "__main__":
    display_current_datetime()
    num_days = int(input("Enter the number of days to add to the current date: "))
    calculate_future_date(num_days)
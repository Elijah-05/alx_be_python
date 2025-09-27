import datetime
from datetime import timedelta

def display_current_datetime():
    current_date = datetime.datetime.now()
    print(f"Current date and time: {current_date.strftime("%Y-%m-%d %H:%M:%S")}")

def calculate_future_date():
    display_current_datetime()
    number_of_days = int(input("Enter the number of days to add to the current date: "))
    current_time = datetime.datetime.now()

    future_date = current_time + timedelta(days=number_of_days)
    formatted_future_date = future_date.strftime("%Y-%m-%d")

    print(f"Future date: {formatted_future_date}")
    return formatted_future_date


if __name__ == "__main__":
    calculate_future_date()
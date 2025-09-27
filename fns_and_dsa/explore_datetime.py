import datetime
from datetime import timedelta

def display_current_datetime():
    current_date = datetime.datetime.now()
    print(f"Current date and time: {current_date.strftime("%Y-%m-%d %H:%M:%S")}")

def calculate_future_date():
    display_current_datetime()
    number_of_days = int(input("Enter number of days: "))
    current_time = datetime.datetime.now()
    future_date = current_time + timedelta(days=number_of_days)
    print(f"Future date: {future_date.strftime("%Y-%m-%d")}")

if __name__ == "__main__":
    calculate_future_date()
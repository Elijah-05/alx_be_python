# Future age calculator. The code calculates what the age will be on the future (2025)

age = int(input("How old are you? "))
current_year = 2023
future_year = 2050

age_in_future_year = age + (future_year - current_year)

print("In", future_year, "you will be", age_in_future_year, "years old")
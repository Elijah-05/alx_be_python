# Personal Finance Calculator
# Objective: Calculate monthly savings and project annual savings with interest

monthly_income = int(input("Enter your monthly income: "))
monthly_expenses = int(input("Enter your total monthly expenses: "))
annual_interest_rate = 0.05

monthly_savings = monthly_income - monthly_expenses
projected_saving = monthly_savings * 12 + (monthly_savings * 12 * annual_interest_rate)

print("Your monthly savings are", monthly_savings)
print("Projected savings after one year, with interest, is:", projected_saving)
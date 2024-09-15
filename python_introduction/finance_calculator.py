# finance_calculator.py
# User input for income and expenses
monthly_income = float(input("Enter your monthly income: "))
monthly_expenses = float(input("Enter your total monthly expenses: "))
# Calculate monthly savings
monthly_savings = monthly_income - monthly_expenses
# Print monthly savings result
print(f"Your monthly savings are ${monthly_savings:.2f}")  # Format to two decimal places
# Annual interest rate (as a decimal)
annual_interest_rate = 0.05  # 5%
# Projected annual savings with interest
projected_savings = (monthly_savings * 12) + (monthly_savings * 12 * annual_interest_rate)
# Print projected annual savings result
print(f"Projected savings after one year, with interest, is: ${projected_savings:.2f}")
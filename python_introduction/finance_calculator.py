# finance_calculator.py

# Prompt user to input their financial details
monthly_income = int (input("Enter your monthly income: "))
monthly_expenses = int (input("Enter your monthly expenses: "))

# Calculate monthly savings
monthly_savings = monthly_income - monthly_expenses

# Projected annual savings
simple_interest = 0.05 # Representing 5% annual interest rate

# Calculate the projected savings
projected_savings_after_one_year = int (monthly_savings * 12 + (monthly_savings * 12 * 0.05))

# Print results
print(f"Your monthly savings are ${monthly_savings}.")
print(f"Projected savings after one year, with interest, is: ${projected_savings_after_one_year}.")
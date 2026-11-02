
# Multi-Currency Travel Budget Analysis

# Exchange rates (1 unit of currency = INR)
exchange_rates = {
    "INR": 1.0,
    "USD": 84.0,
    "EUR": 91.0,
    "GBP": 108.0,
    "AED": 23.0,
    "JPY": 0.56
}

# Currency conversion fee
conversion_fee_rate = 2.0

print("===== MULTI-CURRENCY TRAVEL BUDGET ANALYSIS =====")

# Input travel budget
budget = float(input("Enter travel budget (INR): "))

# Input number of expenses
n = int(input("Enter number of expense categories: "))

expenses = {}
total_expense = 0

# Process multiple expenses
for i in range(n):

    print("\nExpense", i + 1)

    category = input("Enter expense category: ").title()

    amount = float(input("Enter expense amount: "))

    currency = input(
        "Enter currency (INR/USD/EUR/GBP/AED/JPY): "
    ).upper()

    # Validate currency
    if currency not in exchange_rates:
        print("Invalid currency. Expense skipped.")
        continue

    if amount < 0:
        print("Invalid amount. Expense skipped.")
        continue

    # Convert to INR
    rate = exchange_rates[currency]

    converted_amount = amount * rate

    # Calculate conversion fee
    conversion_fee = (
        converted_amount * conversion_fee_rate / 100
    )

    # Calculate total expense
    final_amount = converted_amount + conversion_fee

    # Store category-wise expense
    expenses[category] = (
        expenses.get(category, 0) + final_amount
    )

    total_expense += final_amount

    # Display individual expense
    print("\nConverted Amount : Rs.",
          round(converted_amount, 2))

    print("Conversion Fee   : Rs.",
          round(conversion_fee, 2))

    print("Total Expense    : Rs.",
          round(final_amount, 2))


# Calculate budget difference
budget_difference = budget - total_expense

# Identify largest expense category
if expenses:
    largest_category = max(
        expenses,
        key=expenses.get
    )
    largest_amount = expenses[largest_category]
else:
    largest_category = "None"
    largest_amount = 0


# Display final travel report
print("\n========== TRAVEL EXPENSE REPORT ==========")

print("\nCategory-wise Expenses:")

for category, amount in expenses.items():
    print(category, ": Rs.", round(amount, 2))

print("-------------------------------------------")

print("Travel Budget       : Rs.", round(budget, 2))

print("Total Expenditure   : Rs.",
      round(total_expense, 2))

print("Largest Category    :", largest_category)

print("Largest Expense     : Rs.",
      round(largest_amount, 2))

print("-------------------------------------------")

# Check budget status
if budget_difference >= 0:

    print("Budget Status       : WITHIN BUDGET")

    print("Remaining Budget    : Rs.",
          round(budget_difference, 2))

else:

    print("Budget Status       : BUDGET EXCEEDED")

    print("Excess Amount       : Rs.",
          round(abs(budget_difference), 2))

print("===========================================")


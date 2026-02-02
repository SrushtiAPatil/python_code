expenses = []

days = int(input("Enter number of days: "))

for i in range(days):
    amount = float(input(f"Enter expense for day {i+1}: ₹"))
    expenses.append(amount)

print("\n📊 Expense Report")
print("All Expenses:", expenses)
print("Total Expense: ₹", sum(expenses))
print("Highest Expense: ₹", max(expenses))
print("Lowest Expense: ₹", min(expenses))
print("Average Expense: ₹", sum(expenses)/len(expenses))

expenses.sort()
print("Sorted Expenses:", expenses)

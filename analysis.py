# analysis.py

from datetime import datetime
import data


# CALCULATE TOTAL
def calculate_total():
    total = 0
    for expense in data.expenses:
        total = total + expense["amount"]
    return total


# COUNT EXPENSES
def count_expenses():
    return len(data.expenses)


# AVERAGE EXPENSE
def calculate_average():
    if len(data.expenses) == 0:
        return 0
    total = calculate_total()
    average = total / len(data.expenses)
    return average


# EXPENSE SUMMARY
def expense_summary():
    print(" EXPENSE SUMMARY ")
    total = calculate_total()
    average = calculate_average()
    count = count_expenses()
    print("Number of expenses:", count)
    print(f"Total spent: ${total:.2f}")
    print(f"Average expense: ${average:.2f}")


# HIGHEST EXPENSE
def highest_expense():
    if len(data.expenses) == 0:
        print("No expenses to look at yet.")
        return
    highest = data.expenses[0]
    for expense in data.expenses:
        if expense["amount"] > highest["amount"]:
            highest = expense

    print("HIGHEST EXPENSE ")
    print("Item:", highest["item"])
    print(f"Amount: ${highest['amount']:.2f}")
    print("Category:", highest["category"])
    print("Date:", highest["date"])


# LOWEST EXPENSE
def lowest_expense():
    if len(data.expenses) == 0:
        print("No expenses to look at yet.")
        return
    lowest = data.expenses[0]
    for expense in data.expenses:
        if expense["amount"] < lowest["amount"]:
            lowest = expense

    print(" LOWEST EXPENSE ")
    print("Item:", lowest["item"])
    print(f"Amount: ${lowest['amount']:.2f}")
    print("Category:", lowest["category"])
    print("Date:", lowest["date"])


# CATEGORY SEARCH
def category_search():
    if len(data.expenses) == 0:
        print("No expenses to search yet.")
        return
    category = input("What category? ").lower().strip()
    found = False

    for expense in data.expenses:
        if expense["category"].lower() == category:
            print(f"{expense['item']} - ${expense['amount']:.2f}")
            found = True
    if not found:
        print("Nothing found in that category.")


# ITEM SEARCH
def item_search():
    if len(data.expenses) == 0:
        print("No expenses to search.")
        return

    keyword = input("Type part of the expense name: ").lower().strip()
    found = False

    for expense in data.expenses:
        if keyword in expense["item"].lower():
            print(f"{expense['item']} - ${expense['amount']:.2f}")
            found = True
    if not found:
        print("No matching expense found.")


# AMOUNT FILTER
def amount_filter():
    if len(data.expenses) == 0:
        print("No expenses to filter.")
        return
    try:
        minimum = float(input("Minimum amount: "))
        maximum = float(input("Maximum amount: "))
    except ValueError:
        print("Enter valid numbers.")
        return
    found = False

    for expense in data.expenses:
        if minimum <= expense["amount"] <= maximum:
            print(f"{expense['item']} - ${expense['amount']:.2f}")
            found = True
    if not found:
        print("No expenses in that range.")


# BUDGET STATUS
def budget_status():
    if data.monthly_budget == 0:
        print("Budget not set.")
        return
    total = calculate_total()
    remaining = data.monthly_budget - total
    print(" BUDGET STATUS ")
    print(f"Monthly budget: ${data.monthly_budget:.2f}")
    print(f"Total spent: ${total:.2f}")
    if remaining > 0:
        print(f"Remaining: ${remaining:.2f}")
    elif remaining == 0:
        print("You have used your entire budget.")
    else:
        print(f"Over budget by ${abs(remaining):.2f}")


# BUDGET PERCENTAGE
def budget_percentage():
    if data.monthly_budget == 0:
        print("budget not set")
        return
    total = calculate_total()
    percentage = (total / data.monthly_budget) * 100
    print(f"You have used {percentage:.2f}% of your budget.")

    if percentage >= 100:
        print("Gone over budget.")
    elif percentage >= 80:
        print("Close to budget limit.")
    else:
        print("Spending is within a safe range.")


# CATEGORY REPORT
def category_report():
    if len(data.expenses) == 0:
        print("No expenses to report.")
        return
    categories = []
    for expense in data.expenses:
        category = expense["category"]
        if category not in categories:
            categories.append(category)

    print("CATEGORY REPORT ")
    for category in categories:
        total = 0
        for expense in data.expenses:
            if expense["category"] == category:
                total = total + expense["amount"]
        print(f"{category:<20}${total:.2f}")


# PAYMENT REPORT
def payment_report():
    if len(data.expenses) == 0:
        print("No expenses to report.")
        return
    payments = {}
    for expense in data.expenses:
        method = expense["payment"]
        if method not in payments:
            payments[method] = 0
        payments[method] += expense["amount"]
    print(" PAYMENT REPORT ")

    for method in payments:
        print(f"{method:<20}${payments[method]:.2f}")


# SORT BY AMOUNT
def sort_by_amount():
    if len(data.expenses) == 0:
        print("No expenses to sort.")
        return

    sorted_list = sorted(data.expenses, key=lambda x: x["amount"])
    print(" SORTED BY AMOUNT")
    for expense in sorted_list:
        print(f"{expense['item']:<20}${expense['amount']:.2f}")


# SORT BY DATE
def sort_by_date():
    if len(data.expenses) == 0:
        print("No expenses to sort.")
        return
    sorted_list = sorted(
        data.expenses,
        key=lambda x: datetime.strptime(x["date"], "%d-%m-%Y"))
    print("SORTED BY DATE")
    for expense in sorted_list:
        print(f"{expense['date']:<15}{expense['item']:<20}${expense['amount']:.2f}")


# LARGE EXPENSE DETECTOR
def large_expense_detector():
    if len(data.expenses) == 0:
        print("No expenses to check.")
        return
    try:
        limit = float(input("Show expenses above what amount ($)? "))
    except ValueError:
        print("Enter a valid number.")
        return
    print(f"Expenses above ${limit:.2f}:")
    found = False
    for expense in data.expenses:
        if expense["amount"] > limit:
            print(f"{expense['item']} - ${expense['amount']:.2f}")
            found = True
    if not found:
        print("No large expenses found.")


# SPENDING LEVEL
def spending_level():
    total = calculate_total()
    print(" SPENDING LEVEL")

    if total == 0:
        print("No spending recorded.")
    elif total < 100:
        print("Low spending.")
    elif total < 500:
        print("Moderate spending.")
    elif total < 1000:
        print("High spending.")
    else:
        print("Very high spending.")
# data.py

from datetime import datetime

expenses = []
backups = []

# User information
user_name = ""
user_email = ""

# Monthly budget
monthly_budget = 0


# USER PROFILE
def create_profile():
    global user_name
    global user_email
    print("CREATE PROFILE ")
    user_name = input("What's your name? ").strip()
    user_email = input("What's your email? ").strip()
    print("All set!")
    print("Nice to meet you,", user_name + "!")


def ask_date(prompt):
    while True:
        text = input(prompt).strip()
        try:
            datetime.strptime(text, "%d-%m-%Y")
            return text
        except ValueError:
            print("That doesn't look right.Use DD-MM-YYYY")


# ADD EXPENSE
def add_expenses():
    print(" ADD EXPENSE")
    item = input("What did you spend on? ").strip()
    while True:
        try:
            amount = float(input("How much was it ($)? "))
            if amount <= 0:
                print("The amount has to be more than 0.")
            else:
                break
        except ValueError:
            print("Please type a number")
    category = input("Category (food, travel, bills,shopping): ").strip()
    date = ask_date("Date (DD-MM-YYYY): ")
    payment = input("Payment method (cash, card, UPI): ").strip()

    expense = {
        "item": item,
        "amount": amount,
        "category": category,
        "date": date,
        "payment": payment
    }

    expenses.append(expense)
    print("Your expense has been saved.")


# ADD MULTIPLE EXPENSES
def add_multiple_expenses():
    print(" ADD MULTIPLE EXPENSES ")
    while True:
        add_expenses()
        again = input("Add another one? (y/n): ").lower().strip()
        if again != "y":
            break


# DISPLAY EXPENSES
def display_expenses():
    if len(expenses) == 0:
        print("You haven't added any expenses yet.")
        return
    print("-" * 80)
    print(f"{'No.':<5}{'Item':<20}{'Amount':<12}{'Category':<15}{'Date':<15}")
    print("-" * 80)
    for i in range(len(expenses)):
        expense = expenses[i]
        print(f"{i + 1:<5}"
              f"{expense['item']:<20}"
              f"${expense['amount']:<11.2f}"
              f"{expense['category']:<15}"
              f"{expense['date']:<15}")
    print("-" * 80)


# VIEW ALL EXPENSES
def view_expenses():
    print(" ALL EXPENSES ")
    display_expenses()


# EDIT EXPENSE
def edit_expense():
    if len(expenses) == 0:
        print("There's nothing to edit yet.")
        return

    display_expenses()
    try:
        number = int(input("Enter the number of the expense to edit: "))
        if number < 1 or number > len(expenses):
            print("That number isn't on the list.")
            return
    except ValueError:
        print("Please enter a valid number.")
        return
    expense = expenses[number - 1]
    print("Enter new details (press Enter to keep the current value).")

    new_item = input(f"Item [{expense['item']}]: ").strip()
    if new_item != "":
        expense["item"] = new_item

    new_amount = input(f"Amount [{expense['amount']:.2f}]: ").strip()
    if new_amount != "":
        try:
            value = float(new_amount)
            if value > 0:
                expense["amount"] = value
            else:
                print("Amount must be more than 0, keeping the old one.")
        except ValueError:
            print("That wasn't a number, keeping the old amount.")

    new_category = input(f"Category [{expense['category']}]: ").strip()
    if new_category != "":
        expense["category"] = new_category

    new_date = input(f"Date [{expense['date']}]: ").strip()
    if new_date != "":
        try:
            datetime.strptime(new_date, "%d-%m-%Y")
            expense["date"] = new_date
        except ValueError:
            print("Invalid date format, keeping old date.")

    new_payment = input(f"Payment [{expense['payment']}]: ").strip()
    if new_payment != "":
        expense["payment"] = new_payment

    print("Expense updated.")


# DELETE EXPENSE
def delete_expense():
    if len(expenses) == 0:
        print("There's nothing to delete yet.")
        return

    display_expenses()

    try:
        number = int(input("Enter the number of the expense to delete: "))
        if number < 1 or number > len(expenses):
            print("That number isn't on the list.")
            return
        removed = expenses.pop(number - 1)
        print(f"Deleted: {removed['item']}")
    except ValueError:
        print("Please enter a valid number.")


# SET BUDGET
def set_budget():
    global monthly_budget
    print(" SET MONTHLY BUDGET ")
    while True:
        try:
            amount = float(input("What's your monthly budget ($)? "))
            if amount <= 0:
                print("Your budget has to be more than 0.")
            else:
                monthly_budget = amount
                print(f"Budget set to ${monthly_budget:.2f}")
                break
        except ValueError:
            print("Please enter a valid number.")


# BACKUP
def backup_expenses():
    global backups
    backups = []
    for expense in expenses:
        backups.append(expense.copy())
    print(f"Backup created for {len(backups)} expenses.")
    return backups
# menus.py
# What the user sees.

import data
import analysis


# WELCOME FUNCTION
def welcome():
    print()
    print("=" * 60)
    print("PERSONAL EXPENSE TRACKER")
    print("=" * 60)
    print("Keep an eye on where your money goes.")
    print("Track spending, categories and your monthly budget.")
    print("=" * 60)


# ANALYSIS MENU
def analysis_menu():
    while True:
        print(" ANALYSIS MENU ")
        print("1. Expense Summary")
        print("2. Highest Expense")
        print("3. Lowest Expense")
        print("4. Category Report")
        print("5. Payment Report")
        print("6. Spending Level")
        print("7. Back")

        choice = input("Enter your choice: ").strip()

        if choice == "1":
            analysis.expense_summary()
        elif choice == "2":
            analysis.highest_expense()
        elif choice == "3":
            analysis.lowest_expense()
        elif choice == "4":
            analysis.category_report()
        elif choice == "5":
            analysis.payment_report()
        elif choice == "6":
            analysis.spending_level()
        elif choice == "7":
            break
        else:
            print("Oops, that's not a valid choice. Try 1-7.")


# SEARCH MENU
def search_menu():
    while True:
        print(" SEARCH MENU ")
        print("1. Search by Item")
        print("2. Search by Category")
        print("3. Filter by Amount")
        print("4. Sort by Amount")
        print("5. Sort by Date")
        print("6. Back")
        choice = input("Enter your choice: ").strip()

        if choice == "1":
            analysis.item_search()
        elif choice == "2":
            analysis.category_search()
        elif choice == "3":
            analysis.amount_filter()
        elif choice == "4":
            analysis.sort_by_amount()
        elif choice == "5":
            analysis.sort_by_date()
        elif choice == "6":
            break
        else:
            print("Not a valid choice. Try 1-6.")


# MAIN MENU
def main_menu():
    while True:
        print()
        print("=" * 60)
        print("MAIN MENU")
        print("=" * 60)
        print("User:", data.user_name)
        print()

        print("1. Add Expense")
        print("2. Add Multiple Expenses")
        print("3. View Expenses")
        print("4. Analysis")
        print("5. Search and Sort")
        print("6. Set Monthly Budget")
        print("7. Budget Status")
        print("8. Budget Percentage")
        print("9. Detect Large Expenses")
        print("10. Edit Expense")
        print("11. Delete Expense")
        print("12. Create Backup")
        print("13. Exit")

        choice = input("Enter your choice: ").strip()

        if choice == "1":
            data.add_expenses()
        elif choice == "2":
            data.add_multiple_expenses()
        elif choice == "3":
            data.view_expenses()
        elif choice == "4":
            analysis_menu()
        elif choice == "5":
            search_menu()
        elif choice == "6":
            data.set_budget()
        elif choice == "7":
            analysis.budget_status()
        elif choice == "8":
            analysis.budget_percentage()
        elif choice == "9":
            analysis.large_expense_detector()
        elif choice == "10":
            data.edit_expense()
        elif choice == "11":
            data.delete_expense()
        elif choice == "12":
            data.backup_expenses()
        elif choice == "13":
            print("Thanks for using ")
            print("Personal Expense Tracker. See you soon!")
            break
        else:
            print("Not a valid choice. Please pick 1-13.")
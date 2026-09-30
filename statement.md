### Personal Expense Tracker
### Project Statement
The Personal Expense Tracker is a Python-based console application designed to help users record, manage, search, analyze, and monitor their daily expenses. It also allows users to create a monthly budget and check their spending status.
### Objectives
- Record individual expenses with item, amount, category, date, and payment method.
- Add multiple expenses easily.
- View, edit, and delete saved expenses.
- Calculate total, average, highest, and lowest expenses.
- Search expenses by item or category.
- Filter expenses by amount.
- Sort expenses by amount and date.
- Set and monitor a monthly budget.
- Calculate the percentage of the budget used.
- Detect large expenses.
- Generate category and payment reports.
- Create a backup of the current expenses.
### Technologies Used
- Programming Language: Python
- Modules Used: datetime
- Data Structure: Lists and dictionaries
- Interface: Command-line / console based
### Project File Structure
Personal_Expense_Tracker/
│
├── data.py
├── analysis.py
├── menus.py
├── main.py
└── statement.md
1. data.py
This file handles the main expense data and user information. It contains functions for:
- Creating a user profile
- Adding expenses
- Adding multiple expenses
- Viewing expenses
- Editing expenses
- Deleting expenses
- Setting the monthly budget
- Creating backups
- Validating dates
2. analysis.py
This file performs calculations and analysis on the stored expenses. It contains functions for:
- Calculating total expenses
- Counting expenses
- Calculating average expense
- Finding highest and lowest expenses
- Searching by category and item
- Filtering by amount
- Checking budget status
- Calculating budget percentage
- Generating category and payment reports
- Sorting expenses
- Detecting large expenses
- Determining spending level
3. menus.py
This file manages the user interface and menus. It contains:
- Welcome screen
- Main menu
- Analysis menu
- Search and sort menu
4. main.py
This is the main entry point of the project. It starts the application by displaying the welcome message, creating the user profile, and opening the main menu.
### How to Run
1. Make sure Python is installed on the computer.
2. Keep all project files in the same folder.
3. Open the project folder in VS Code, IDLE, or another Python editor.
4. Run:
main.py
5. Enter the requested profile information.
6. Use the main menu to manage and analyze expenses.
Conclusion
The Personal Expense Tracker provides a simple and user-friendly way to manage personal spending through a Python console application. The project demonstrates the use of functions, lists, dictionaries, loops, conditional statements, input validation, modules, and basic data analysis in Python.
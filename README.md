# Personal Expense Tracker

I made this command-line app in Python because I wanted a simple way to see where my money actually goes. You add your expenses, set a monthly budget, and the app tells you how you're doing.

## What it can do

- Save your name and email at the start
- Add one expense, or keep adding a bunch back to back
- View, edit and delete expenses whenever you make a mistake
- Set a monthly budget and check how much is left (or how far over you went)
- Show a summary, your biggest and smallest expense, and totals by category and by payment method
- Search by item name or category, and filter by an amount range
- Sort your expenses by amount or by date
- report any expense above a limit you choose
- Make a quick backup copy of your expenses

## Files

```
expense_tracker/
├── main.py       # start here, this is the file you run
├── menus.py      # all the menus you see on screen
├── data.py       # adding, editing, deleting, budget and backup
├── analysis.py   # totals, reports, search, sort and budget checks
└── README.md
```

## What you need

Python 3.6 or newer.

## Running it

Open a terminal, go into the project folder and run:
`python3 main.py`.

## Using it

When the project starts, it asks for your name and email. After that you'll be redirected to the main menu, where you just type the number of what you want to do.

When you add an expense, it asks for the item, the amount, a category (like food, travel, bills or shopping), the date in `DD-MM-YYYY` format, and how you paid (cash, card or UPI). If you type something wrong, like a letter instead of an amount, it'll just ask again.

To leave, pick option 13.

### Main menu

|No. What it does 
 1. Add an expense 
 2. Add several expenses in a row 
 3. See all your expenses 
 4. Analysis (reports and summaries) 
 5. Search and sort 
 6. Set your monthly budget 
 7. Check budget status 
 8. See what % of your budget is used
 9. Find large expenses
 10. Edit an expense 
 11. Delete an expense 
 12. Make a backup 
 13. Exit 

## Things to know

This is a first version, so a few things aren't perfect yet:

- Nothing is saved after you close the file. Your expenses live in memory only, so they're gone once you exit.
- The budget check adds up every expense you've entered, not just this months'.
- "Food" and "food" show up as two separate categories in the category report, so try to type them the same way each time.
- You can make a backup, but there's no way to restore it yet. A new backup also replaces the old one.
- Amounts are shown in dollars ($) for now.

## What I'd like to add next

- Saving to a file so your data stays after you close the interface.
- Checking the budget against the current month only.
- Restoring from a backup.
- Cleaning up categories automatically.
- Choosing your own currency, like ₹, Pound ,etc.
- Some tests.

![Main](/Screenshot%202026-09-30%20203812.png)
![Main](/ss2.png)
![Main](/ss3.png)
![Main](/ss4.png)
![Main](/ss5.png)
![Main](/Screenshot%202026-09-30%20220314.png)
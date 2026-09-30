# main.py
# Run this file to start the Personal Expense Tracker.

import data
import menus


def main():
    menus.welcome()
    data.create_profile()
    menus.main_menu()


main()
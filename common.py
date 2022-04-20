
# Return the selected value
import sqlite3

import account


def select_from_options(minimum, maximum):
    while True:
        try:
            input_val = int(input("Select from menu above : "))
            if minimum <= input_val <= maximum:
                return input_val
                break
            else:
                print("Invalid input! Please enter a number from {} to {}.", minimum, maximum)
        except ValueError:
            print("Invalid input! Please enter a numeric!")
            continue


def chose_operation():
    print("************************************************")
    print("************************************************\n")
    print("(1) Create New User \n"
          "(2) Login Existing User \n"
          "(3) Quit Application \n")

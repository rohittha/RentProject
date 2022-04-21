# Return the selected value
import sqlite3
import pyodbc


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


def chose_report():
    print("************************************************\n")
    print("(1) Report 1 \n"
          "(2) Report 2  \n"
          "(3) Report 3  \n")


def get_connection():
    connection = pyodbc.connect('Driver={SQL Server};'
                                'Server = DESKTOP-KSAT5NM\\RTSQL;'
                                'Database = Rent1;'
                                'Trusted_Connection=yes;')
    return connection

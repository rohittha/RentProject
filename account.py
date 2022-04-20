import csv
import sqlite3
import common
import encryption
import account
import dbbackup
import sys

# This function is used to take decision based on user input
import home


def users_input():

    # Encrypt Pwd
    while True:
        common.chose_operation()
        input_val = common.select_from_options(1, 3)
        new_user_email = input("Please enter email: ")
        new_user_password = input("Please enter password: ")
        encrypted_pwd = encryption.encrypt_password(new_user_password)

        if input_val == 1:
            print("You have selected - Create new user")
            is_Admin = select_user_type()
            account.create_user(new_user_email, encrypted_pwd, is_Admin)
        elif input_val == 2:
            print("You have selected - Login existing user")
            account.login_user(new_user_email, encrypted_pwd)
        elif input_val == 3:
            print("You have selected to Quit Application.")
            input("Press any key to continue..")
            sys.exit()
    # Take backup of the DB
    dbbackup.take_backup()


def select_user_type():
    print("(0) Create Regular User \n"
          "(1) Create Admin User  \n")
    selected_value = common.select_from_options(0, 1)
    return selected_value


# This function creates a new user in the database
def create_user(username, password, is_admin):
    print("Creating New User..")
    connection = sqlite3.connect("User.db")
    cursor = connection.cursor()
    sql_query = "Insert into TB_USER (Login, Cryptographic_Password, ACCESS_COUNT, IsAdmin) " \
                "VALUES('" + username + "','" + password + "',0," + str(is_admin) + ")"
    cursor.execute(sql_query)
    connection.commit()
    cursor.close()
    connection.close()


def login_user(username, password):
    try:
        print("Searching user account..")
        connection = sqlite3.connect("User.db")

        cursor = connection.cursor()
        sql_query = "select * from TB_USER where Login = '" + username + \
                    "' and Cryptographic_Password = '" + password + "'"
        cursor.execute(sql_query)
        results = cursor.fetchall()
        if not results:
            print("Result not found")
        else:
            if len(list(results)) > 0:
                print("****** User found *******")
                print(" User Login   : {}".format(results[0][1]))
                print(" Access Count : {}".format(results[0][3]))
                print("****** User found *******")
                account.update_user_access_count(username, int(format(results[0][3])))
                home.load_home_page()
            else:
                print("No record found")
        cursor.close()
        connection.close()
    except Exception as e:
        print("Encountered error in logging in the user! Please read message below:")
        print(str(e))


def update_user_access_count(username, access_count):
    try:
        print("Updating user access count..")
        connection = sqlite3.connect("User.db")
        access_count += 1
        cursor = connection.cursor()
        sql_query = "update TB_USER set ACCESS_COUNT=" + str(access_count) + " where Login = '" + username + "'"
        cursor.execute(sql_query)
        connection.commit()
        cursor.close()
        connection.close()
    except Exception as e:
        print("Encountered error while updating access count! Please read message below:")
        print(str(e))
        pass


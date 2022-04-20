import sqlite3

import account
import common
import reports


def load_home_page():
    print("************************************************")
    print("************************************************\n")
    print("(1) Add New Building \n"
          "(2) Add New Tenant \n"
          "(3) Record Rent Information \n"
          "(4) Record Monthly Payment\n"
          "(5) Access Reports \n"
          "(6) Log Out\n")
    input_val = common.select_from_options(1, 5)

    if input_val == 1:
        print("You have selected - Add New Building")
        add_new_building()
    elif input_val == 2:
        print("You have selected - Add New Tenant")
        add_new_tenant()
    elif input_val == 3:
        print("You have selected - Add New Rent Profile")
        add_new_rent_profile()
    elif input_val == 4:
        print("You have selected - Add New Tenant")
        add_new_payments()
    elif input_val == 5:
        print("You have selected to Access report.")
        input("Press any key to continue..")
        reports.view_reports()
    elif input_val == 6:
        print("You have selected to Log Out.")
        input("Press any key to continue..")
        account.users_input()


# This function creates a new building in the database
def add_new_building():
    print("Creating New Building..")
    building_number = input("Please enter building number: ")
    building_street = input("Please enter street: ")
    building_city = input("Please enter city: ")
    building_province = input("Please enter province: ")
    building_country = input("Please enter country: ")

    connection = sqlite3.connect("User.db")
    cursor = connection.cursor()
    sql_query_master = "Insert into Buildings (BuildingNumber, Street, City, Province, Country)" + "VALUES(" + str(
        building_number) + ",'" + building_street + "','" + building_city + "','" + building_province + "','" + building_country + "')"
    cursor.execute(sql_query_master)
    last_inserted_id = cursor.lastrowid
    add_new_apartment(last_inserted_id, connection)
    connection.commit()
    cursor.close()
    connection.close()


def add_new_apartment(building_id, connection):
    print("Creating New Apartment..")

    apartment_number = input("Please enter apartment number: ")
    # connection = sqlite3.connect("User.db")
    cursor = connection.cursor()
    sql_query = "Insert into Apartments (BuildingId, ApartmentNumber)" + \
                "VALUES(" + str(building_id) + "," + apartment_number + ")"
    cursor.execute(sql_query)


def add_new_tenant():
    tenant_firstname = input("Please enter Tenant First Name: ")
    tenant_lastname = input("Please enter Tenant Last Name: ")
    tenant_govtidtype = input("Please enter Govt Id Type: ")
    tenant_govtidnumber = input("Please enter Govt Id Number: ")

    connection = sqlite3.connect("User.db")
    cursor = connection.cursor()
    sql_query_master = "Insert into Tenants (FirstName, LastName, GovtId_Type, GovtId_Number) VALUES(\'{0}\',\'{1}\',\'{2}\',\'{3}\')".format(
        tenant_firstname, tenant_lastname, tenant_govtidtype, tenant_govtidnumber)
    cursor.execute(sql_query_master)
    connection.commit()
    cursor.close()
    connection.close()


def add_new_rent_profile():
    rent_tenant_id = input("Please enter Tenant Id: ")
    rent_apart_id = input("Please enter Tenant's Apartment Id: ")
    rent_rent_period = input("Please enter Rent Period: ")
    rent_price = input("Please enter Price: ")

    connection = sqlite3.connect("User.db")
    cursor = connection.cursor()
    sql_query_master = "Insert into RentProfiles (TenantId, ApartmentId, RentPeriod, Price) VALUES(\'{0}\',\'{1}\',\'{2}\',\'{3}\')".format(
        rent_tenant_id, rent_apart_id, rent_rent_period, rent_price)
    cursor.execute(sql_query_master)
    connection.commit()
    cursor.close()
    connection.close()


def add_new_payments():
    rent_tenant_id = input("Please enter tenant id: ")
    rent_rent_id = input("Please enter rent profile id: ")
    rent_paid_amount = input("Please enter paid amount: ")
    rent_paid_date = input("Please enter paid date: ")

    connection = sqlite3.connect("User.db")
    cursor = connection.cursor()
    sql_query_master = "Insert into Payments (TenantId, RentId, PaidAmount, PaidDate) VALUES(\'{0}\',\'{1}\',\'{2}\',\'{3}\')".format(
        rent_tenant_id, rent_rent_id, rent_paid_amount, rent_paid_date)
    cursor.execute(sql_query_master)
    connection.commit()
    cursor.close()
    connection.close()


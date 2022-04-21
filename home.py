import sqlite3

import account
import common
import reports
import pyodbc


def load_home_page():
    print("************************************************")
    print("************************************************\n")
    print("(1) Add New Building \n"
          "(2) Update Building \n"
          "(3) Add New Apartment \n"
          "(4) Update Apartment \n"
          "(5) Add New Tenant \n"
          "(6) Update Tenant \n"
          "(7) Add new Rent Information \n"
          "(8) Update Rent Information \n"
          "(9) Add new Monthly Payment\n"
          "(10) Update Monthly Payment\n"
          "(11) Delete Building \n"
          "(12) Delete Tenant \n"
          "(13) Delete Rent Information \n"
          "(14) Delete Monthly Payment\n"
          "(15) Access Reports \n"
          "(16) Log Out\n")
    input_val = common.select_from_options(1, 16)

    if input_val == 1:
        print("You have selected - Add New Building")
        add_new_building()
    elif input_val == 2:
        print("You have selected - Update Building")
        update_building()
    elif input_val == 3:
        print("You have selected - Add New Tenant")
        add_new_apartment()
    elif input_val == 4:
        print("You have selected - Update Tenant")
        update_apartment()
    elif input_val == 5:
        print("You have selected - Add New Tenant")
        add_new_tenant()
    elif input_val == 6:
        print("You have selected - Update Tenant")
        update_tenant()
    elif input_val == 7:
        print("You have selected - Add New Rent Profile")
        add_new_rent_profile()
    elif input_val == 8:
        print("You have selected - Update Rent Profile")
        update_rent_profile()
    elif input_val == 9:
        print("You have selected - Add New Payments")
        add_new_payments()
    elif input_val == 10:
        print("You have selected - Update Payments")
        update_payments()
    elif input_val == 11:
        print("You have selected - Delete Building")
        delete_building()
    elif input_val == 12:
        print("You have selected - Delete Tenant")
        delete_tenant()
    elif input_val == 13:
        print("You have selected - Delete Rent Profile")
        delete_rent_profile()
    elif input_val == 14:
        print("You have selected - Delete Payments")
        delete_payments()
    elif input_val == 15:
        print("You have selected to Access report.")
        input("Press any key to continue..")
        reports.view_reports()
    elif input_val == 16:
        print("You have selected to Log Out.")
        input("Press any key to continue..")
        account.users_input()
    load_home_page()

    # This function delete the building for which the ID has been passed
def delete_tenant():
    id = input("Please enter tenant Id : ")
    connection = pyodbc.connect('Driver={SQL Server};'
                                'Server=DESKTOP-KSAT5NM\RTSQL;'
                                'Database=Rent1;'
                                'Trusted_Connection=yes;')
    cursor = connection.cursor()
    sql_query_master = "Delete from tenants where Id = " + str(id) + ""
    cursor.execute(sql_query_master)
    connection.commit()
    input("Deleted successfully! Press any key to continue..")
    cursor.close()
    connection.close()



def delete_rent_profile():
    id = input("Please enter rent profile Id : ")
    connection = pyodbc.connect('Driver={SQL Server};'
                                'Server=DESKTOP-KSAT5NM\RTSQL;'
                                'Database=Rent1;'
                                'Trusted_Connection=yes;')
    cursor = connection.cursor()
    sql_query_master = "Delete from rent_profiles where Id = " + str(id) + ""
    cursor.execute(sql_query_master)
    connection.commit()
    input("Deleted successfully! Press any key to continue..")
    cursor.close()
    connection.close()


def delete_payments():
    id = input("Please enter payments Id : ")
    connection = pyodbc.connect('Driver={SQL Server};'
                                'Server=DESKTOP-KSAT5NM\RTSQL;'
                                'Database=Rent1;'
                                'Trusted_Connection=yes;')
    cursor = connection.cursor()
    sql_query_master = "Delete from payments where Id = " + str(id) + ""
    cursor.execute(sql_query_master)
    connection.commit()
    input("Deleted succesfully! Press any key to continue..")
    cursor.close()
    connection.close()


def delete_apartments():
    id = input("Please enter apartment Id : ")
    connection = pyodbc.connect('Driver={SQL Server};'
                                'Server=DESKTOP-KSAT5NM\RTSQL;'
                                'Database=Rent1;'
                                'Trusted_Connection=yes;')
    cursor = connection.cursor()
    sql_query_master = "Delete from apartments where Id = " + str(id) + ""
    cursor.execute(sql_query_master)
    connection.commit()
    input("Deleted succesfully! Press any key to continue..")
    cursor.close()
    connection.close()


# This function creates a new building in the database
def add_new_building():
    print("Creating New Building..")
    building_number = input("Please enter building number: ")
    building_street = input("Please enter street: ")
    building_city = input("Please enter city: ")
    building_province = input("Please enter province: ")
    building_country = input("Please enter country: ")
    connection = pyodbc.connect('Driver={SQL Server};'
                                'Server=DESKTOP-KSAT5NM\RTSQL;'
                                'Database=Rent1;'
                                'Trusted_Connection=yes;')
    cursor = connection.cursor()
    sql_query_master = "Insert into Buildings (BuildingNumber, Street, City, Province, Country)" + "VALUES(" + str(
        building_number) + ",'" + building_street + "','" + building_city + "','" + building_province + "','" + building_country + "')"
    cursor.execute(sql_query_master)
    connection.commit()
    cursor.execute("SELECT @@IDENTITY AS ID;")
    last_inserted_id = cursor.fetchone()[0]
    print("New record added successfully! Last insert building id = " + str(last_inserted_id))
    # add_new_apartment(last_inserted_id, connection)
    input("Press any key to continue..")
    cursor.close()
    connection.close()


# This function updates an existing building in the database
def update_building():
    print("Update Building..")
    building_id = input("Please enter building Id : ")
    building_number = input("Please enter building number: ")
    building_street = input("Please enter street: ")
    building_city = input("Please enter city: ")
    building_province = input("Please enter province: ")
    building_country = input("Please enter country: ")
    connection = pyodbc.connect('Driver={SQL Server};'
                                'Server=DESKTOP-KSAT5NM\RTSQL;'
                                'Database=Rent1;'
                                'Trusted_Connection=yes;')
    cursor = connection.cursor()
    sql_query_master = "Update Buildings set BuildingNumber = " + str(building_number) + \
                       ", Street = '" + building_street + "', City ='" + building_city + \
                       "', Province='" + building_province + "', Country='" + building_country + \
                       "' where Id = " + str(building_id)
    cursor.execute(sql_query_master)
    connection.commit()
    print("Record updated successfully!")
    input("Press any key to continue..")
    cursor.close()
    connection.close()


# This function delete the building for which the ID has been passed
def delete_building():
    print("Delete Building..")
    building_id = input("Please enter building Id : ")
    connection = pyodbc.connect('Driver={SQL Server};'
                                'Server=DESKTOP-KSAT5NM\RTSQL;'
                                'Database=Rent1;'
                                'Trusted_Connection=yes;')
    cursor = connection.cursor()
    sql_query_master = "Delete from Buildings where Id = " + str(building_id) + ""
    cursor.execute(sql_query_master)
    connection.commit()
    input("Press any key to continue..")
    cursor.close()
    connection.close()


def add_new_apartment():
    print("Creating New Apartment..")
    building_id = input("Please enter building id: ")

    apartment_number = input("Please enter apartment number: ")
    connection = pyodbc.connect('Driver={SQL Server};'
                                'Server=DESKTOP-KSAT5NM\RTSQL;'
                                'Database=Rent1;'
                                'Trusted_Connection=yes;')
    cursor = connection.cursor()
    sql_query = "Insert into Apartments (BuildingId, ApartmentNumber)" + \
                " VALUES(" + str(building_id) + "," + apartment_number + ")"
    cursor.execute(sql_query)
    connection.commit()
    cursor.execute("SELECT @@IDENTITY AS ID;")
    last_inserted_id = cursor.fetchone()[0]
    print("New record added successfully! Last insert apartment id = " + str(last_inserted_id))
    input("Press any key to continue..")
    cursor.close()
    connection.close()


def update_apartment():
    print("Update Apartment..")
    apartment_id = input("Please enter apartment Id : ")
    building_id = input("Please enter building Id : ")
    apartment_number = input("Please enter apartment number: ")
    connection = pyodbc.connect('Driver={SQL Server};'
                                'Server=DESKTOP-KSAT5NM\RTSQL;'
                                'Database=Rent1;'
                                'Trusted_Connection=yes;')
    cursor = connection.cursor()
    sql_query = "Update Apartments set BuildingId = " + str(building_id) + \
                ", ApartmentNumber = " + apartment_number + " where Id = " + str(apartment_id)
    cursor.execute(sql_query)
    connection.commit()
    print("Record updated successfully!")
    input("Press any key to continue..")
    cursor.close()
    connection.close()


def add_new_tenant():
    tenant_firstname = input("Please enter Tenant First Name: ")
    tenant_lastname = input("Please enter Tenant Last Name: ")
    tenant_govtidtype = input("Please enter Govt Id Type: ")
    tenant_govtidnumber = input("Please enter Govt Id Number: ")

    connection = pyodbc.connect('Driver={SQL Server};'
                                'Server=DESKTOP-KSAT5NM\RTSQL;'
                                'Database=Rent1;'
                                'Trusted_Connection=yes;')
    cursor = connection.cursor()
    sql_query_master = "Insert into Tenants (FirstName, LastName, GovtId_Type, GovtId_Number) VALUES(\'{0}\',\'{1}\',\'{2}\',\'{3}\')".format(
        tenant_firstname, tenant_lastname, tenant_govtidtype, tenant_govtidnumber)
    cursor.execute(sql_query_master)
    connection.commit()
    cursor.execute("SELECT @@IDENTITY AS ID;")
    last_inserted_id = cursor.fetchone()[0]
    print("New record added successfully! Last insert tenant id = " + str(last_inserted_id))
    input("Press any key to continue..")
    cursor.close()
    connection.close()


def update_tenant():
    tenant_id = input("Please enter Tenant Id : ")
    tenant_firstname = input("Please enter Tenant First Name: ")
    tenant_lastname = input("Please enter Tenant Last Name: ")
    tenant_govtidtype = input("Please enter Govt Id Type: ")
    tenant_govtidnumber = input("Please enter Govt Id Number: ")
    connection = pyodbc.connect('Driver={SQL Server};'
                                'Server=DESKTOP-KSAT5NM\RTSQL;'
                                'Database=Rent1;'
                                'Trusted_Connection=yes;')
    cursor = connection.cursor()
    sql_query_master = "Update Tenants set FirstName = \'{0}\', LastName = \'{1}\', GovtId_Type = \'{2}\', GovtId_Number = \'{3}\' " \
                       " where Id = \'{4}\'".format(tenant_firstname, tenant_lastname, tenant_govtidtype,
                                                    tenant_govtidnumber, tenant_id)
    cursor.execute(sql_query_master)
    connection.commit()
    print("Record updated successfully!")
    input("Press any key to continue..")
    cursor.close()
    connection.close()


def add_new_rent_profile():
    rent_tenant_id = input("Please enter Tenant Id: ")
    rent_apart_id = input("Please enter Tenant's Apartment Id: ")
    rent_rent_period = input("Please enter Rent Period: ")
    rent_price = input("Please enter Price: ")
    connection = pyodbc.connect('Driver={SQL Server};'
                                'Server=DESKTOP-KSAT5NM\RTSQL;'
                                'Database=Rent1;'
                                'Trusted_Connection=yes;')
    cursor = connection.cursor()
    sql_query_master = "Insert into Rent_Profiles (TenantId, ApartmentId, RentPeriod, Price) VALUES(\'{0}\',\'{1}\',\'{2}\',\'{3}\')".format(
        rent_tenant_id, rent_apart_id, rent_rent_period, rent_price)
    cursor.execute(sql_query_master)
    connection.commit()
    cursor.execute("SELECT @@IDENTITY AS ID;")
    last_inserted_id = cursor.fetchone()[0]
    print("New record added successfully! Last inserted rent profile id = " + str(last_inserted_id))
    input("Press any key to continue..")
    cursor.close()
    connection.close()


def update_rent_profile():
    rent_id = input("Please enter rent profile Id: ")
    rent_tenant_id = input("Please enter Tenant Id: ")
    rent_apart_id = input("Please enter Tenant's Apartment Id: ")
    rent_rent_period = input("Please enter Rent Period: ")
    rent_price = input("Please enter Price: ")
    connection = pyodbc.connect('Driver={SQL Server};'
                                'Server=DESKTOP-KSAT5NM\RTSQL;'
                                'Database=Rent1;'
                                'Trusted_Connection=yes;')
    cursor = connection.cursor()
    sql_query_master = "Update Rent_Profiles set TenantId = \'{0}\', ApartmentId =\'{1}\', RentPeriod = \'{2}\', Price = \'{3}\'" \
                       " where Id = \'{4}\'".format(rent_tenant_id, rent_apart_id, rent_rent_period, rent_price,
                                                    rent_id)
    cursor.execute(sql_query_master)
    connection.commit()
    print("Record updated successfully!")
    input("Press any key to continue..")
    cursor.close()
    connection.close()


def add_new_payments():
    rent_tenant_id = input("Please enter tenant id: ")
    rent_rent_id = input("Please enter rent profile id: ")
    rent_paid_amount = input("Please enter paid amount: ")
    rent_paid_date = input("Please enter paid date: ")
    connection = pyodbc.connect('Driver={SQL Server};'
                                'Server=DESKTOP-KSAT5NM\RTSQL;'
                                'Database=Rent1;'
                                'Trusted_Connection=yes;')
    cursor = connection.cursor()
    sql_query_master = "Insert into Payments (TenantId, RentId, PaidAmount, PaidDate) " \
                       "VALUES(\'{0}\',\'{1}\',\'{2}\',\'{3}\'" \
                       ")".format(rent_tenant_id, rent_rent_id, rent_paid_amount, rent_paid_date)
    cursor.execute(sql_query_master)
    connection.commit()
    input("Press any key to continue..")
    cursor.close()
    connection.close()


def update_payments():
    payments_id = input("Please enter payments Id: ")
    rent_tenant_id = input("Please enter tenant id: ")
    rent_rent_id = input("Please enter rent profile id: ")
    rent_paid_amount = input("Please enter paid amount: ")
    rent_paid_date = input("Please enter paid date: ")
    connection = pyodbc.connect('Driver={SQL Server};'
                                'Server=DESKTOP-KSAT5NM\RTSQL;'
                                'Database=Rent1;'
                                'Trusted_Connection=yes;')
    cursor = connection.cursor()
    sql_query_master = "Update Payments set TenantId= \'{0}\', RentId=\'{1}\', PaidAmount=\'{2}\', PaidDate=\'{3}\' " \
                       " where Id = \'{4}\'".format(rent_tenant_id, rent_rent_id, rent_paid_amount, rent_paid_date,
                                                    payments_id)
    cursor.execute(sql_query_master)
    connection.commit()
    print("Record updated successfully!")
    input("Press any key to continue..")
    cursor.close()
    connection.close()

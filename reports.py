
import pyodbc
import pandas
import common
import csv


def view_reports():
    print("************************************************")
    print("************************************************\n")
    print("(1) Rental Unit Status Report \n"
          "(2) Rental Payments Report \n"
          "(3) Report 3 \n")
    input_val = common.select_from_options(1, 3)

    if input_val == 1:
        print("You have selected - Rental Unit Status Report")
        get_rental_unit_status()
    elif input_val == 2:
        print("You have selected - Rental Payments Report")
        GetRentalPayments()
    elif input_val == 3:
        print("You have selected - Report")
        Report3()


def get_rental_unit_status():
    connection = pyodbc.connect('Driver={SQL Server};'
                                'Server=DESKTOP-KSAT5NM\RTSQL;'
                                'Database=Rent1;'
                                'Trusted_Connection=yes;')
    cursor = connection.cursor()
    sqlquery = "EXEC USP_GetRentalUnitStatus"
    dataframe_results = pandas.read_sql_query(sqlquery, connection)
    pandas.set_option("display.max_rows", None, "display.max_columns", None)
    print(dataframe_results)
    dataframe_results.to_csv("RentalUnitStatusReport.csv")
    # cursor.execute(sql_query_master)
    # connection.commit()
    input("Press any key to continue..")
    cursor.close()
    connection.close()


def GetRentalPayments():
    connection = pyodbc.connect('Driver={SQL Server};'
                                'Server=DESKTOP-KSAT5NM\RTSQL;'
                                'Database=Rent1;'
                                'Trusted_Connection=yes;')
    cursor = connection.cursor()
    sqlquery = "EXEC USP_GetRentalPayments"
    dataframe_results = pandas.read_sql_query(sqlquery, connection)
    pandas.set_option("display.max_rows", None, "display.max_columns", None)
    print(dataframe_results)
    dataframe_results.to_csv("Report2_RentalPayments.csv")
    # cursor.execute(sql_query_master)
    # connection.commit()
    input("Press any key to continue..")
    cursor.close()
    connection.close()


def Report3():
    connection = pyodbc.connect('Driver={SQL Server};'
                                'Server=DESKTOP-KSAT5NM\RTSQL;'
                                'Database=Rent1;'
                                'Trusted_Connection=yes;')
    cursor = connection.cursor()
    sqlquery = "EXEC USP_GetReport3"
    dataframe_results = pandas.read_sql_query(sqlquery, connection)
    pandas.set_option("display.max_rows", None, "display.max_columns", None)
    print(dataframe_results)
    dataframe_results.to_csv("Report3.csv")
    # cursor.execute(sql_query_master)
    # connection.commit()
    input("Press any key to continue..")
    cursor.close()
    connection.close()
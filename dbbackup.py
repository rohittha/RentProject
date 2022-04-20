import csv
import sqlite3


def take_backup():
    print("Creating Backup..")
    connection = sqlite3.connect("User.db")
    cursor = connection.cursor()
    sql_query = "SELECT User_id, Login, Cryptographic_Password, Access_count FROM TB_USER"
    cursor.execute(sql_query)
    results = cursor.fetchall()

    with open('usersdb-backup.csv', 'w') as out:
        header = ['User_id', 'Login', 'Cryptographic_Password', 'Access_count']
        file = csv.writer(out)
        file.writerow(header)
        for row in results:
            file.writerow(row)
    cursor.close()
    connection.close()

#Function to load data from csv to a postgres db table

import psycopg2
import pandas as pd
import sys

def pg_load_table(filepath, tblname, dbname, host, port, username, password):
    try:
        connection = psycopg2.connect(dbname=dbname, host=host, port=port, user=username, password=password)
        print("Making connection with database...")
        cur = connection.curoser()
        file = open(filepath, "r")
        #Load data from the csv file with header into the table
        cur.copy_expert("copy {} from STDIN CSV HEADER QUOTE '\"'".format(tblname), file)
        cur.execute("commit;")
        print("Data loaded into {}".format(tblname))
        connection.close()
        print("Database connection closed.")

    except Exception as err:
        print("Error:{}".format(str(err)))
        sys.exit(1)

#function execution
filepath='C:/Users/Divya/AppData/Local/Programs/Python/Python38-32/patients.csv'
tblname='patients'
dbname='medical_data'
host='host_url'
port='8880'
username='dshukla'
password='pswrd'
pg_load_table(filepath, tblname, dbname, host, port, username, password)

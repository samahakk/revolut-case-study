import sqlite3, csv 

connection = sqlite3.connect('revoult')
cursor = connection.cursor()

tables = ['countries.csv', 'currency_details.csv','fraudsters.csv','fx_rates.csv', 'transactions.csv', 'users.csv']

for table in tables:
        with open(table, 'r'):
                no_records = 0
                for row in file:
                        cursor.execute()

import sqlite3, csv 

connection = sqlite3.connect('revoult')
cursor = connection.cursor()

tables = ['countries.csv', 'currency_details.csv','fraudsters.csv','fx_rates', 'transactions.csv', 'users.csv']

for table in tables:

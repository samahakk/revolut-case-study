import sqlite3, csv 

connection = sqlite3.connect('revoult.db')
cursor = connection.cursor()

tables = ['countries.csv', 'currency_details.csv','fraudsters.csv','fx_rates.csv', 'transactions.csv', 'users.csv']

with open('hc_data/countries.csv', 'r') as file:
        no_records = 0
        for row in file:
                cursor.execute("INSERT INTO countries (?,?,?,?,?)", row.split(","))
                connection.commit()
                no_records += 1
connection.close()
print('\n{} Datenbak Eintrag Erfolgreich abgeschlossen')

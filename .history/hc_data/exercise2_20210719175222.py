import sqlite3, csv 

connection = sqlite3.connect('revoult')
cursor = connection.cursor()

tables = ['countries.csv', ]

for table in tables:

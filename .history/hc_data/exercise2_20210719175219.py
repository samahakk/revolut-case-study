import sqlite3, csv 

connection = sqlite3.connect('revoult')
cursor = connection.cursor()

tables = ['countries.c']

for table in tables:
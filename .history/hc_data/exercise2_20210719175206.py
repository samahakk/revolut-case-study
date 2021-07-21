import sqlite3, csv 

connection = sqlite3.connect('revoult')
cursor = connection.cursor()

for table in tables:
        
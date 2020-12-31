import sqlite3
import os

connection = sqlite3.connect('database/temperature_humidity.db')

FOLDER = 'database/ddl'

for file in os.listdir(FOLDER):
    if file.endswith('sql'):
        with open(f'{FOLDER}/{file}') as f:
            connection.executescript(f.read())

connection.close()
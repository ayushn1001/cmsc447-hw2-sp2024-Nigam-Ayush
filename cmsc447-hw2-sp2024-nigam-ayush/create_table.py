#Author: Ayush Nigam
#Class: CMSC447
import sqlite3

conn = sqlite3.connect('database.db')
print("Connected to database successfully")

conn.execute('CREATE TABLE students (name TEXT, idnum TEXT, points TEXT)')
print("Created table successfully!")

conn.close()


Title: Homework 2 
Class: CMSC447
Author: Ayush Nigam

This is a simple Flask web application for managing student records using SQLite3 to perform CRUD (Create, Read, Update, Delete) operations.

Features:
-Add new student records
-List all student records
-Edit existing student records
-Delete student records
-Search for student records

Requirements
-Python 3.x
-Flask
-SQLite3
-virtual environment

To run:
-go into the virtual environment using "myenv\Scripts\activate" with the appropriate name for your venv (if you're on command prompt)
-run "python create_table.py"
-run "python -m flask run"
-Start the LocalHost:5000 on your browser

Usage:
-Navigate to the "Add Student" page to add new student records.
-Navigate to the "Edit Students" page to view all existing student records and edit/delete them.
-Use the "Search" feature to search for specific student records.

Configs:
-Database connection settings can be configured in the app.py file.
-Templates for the HTML views are located in the templates directory.
-CSS file is located in the static directory.
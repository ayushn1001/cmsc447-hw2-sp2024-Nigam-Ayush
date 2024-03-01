#Author: Ayush Nigam
#Class : CMSC447
from flask import Flask
from flask import render_template
from flask import request
import sqlite3

app = Flask(__name__)

# Home Page
@app.route("/")
def home():
    return render_template("home.html")

# to add a new student to the database
@app.route("/enternew")
def enternew():
    return render_template("student.html")

# to add a new record (INSERT) student data to the database
@app.route("/addrec", methods = ['POST', 'GET'])
def addrec():
    
    if request.method == 'POST':
        try:
            nm = request.form['nm']
            idnum = request.form['idnum']
            points = request.form['points']
            with sqlite3.connect('database.db') as con:
                cur = con.cursor()
                cur.execute("INSERT INTO students (name, idnum, points) VALUES (?,?,?)",(nm, idnum, points))

                con.commit()
                msg = "Record successfully added to database"
        except:
            con.rollback()
            msg = "Error in the INSERT"

        finally:
            con.close()
            # Send the transaction message to result.html
            return render_template('result.html',msg=msg)

# select all data from the database and display in a table      
@app.route('/list')
def list():
    con = sqlite3.connect("database.db")
    con.row_factory = sqlite3.Row

    cur = con.cursor()
    cur.execute("SELECT rowid, * FROM students")

    rows = cur.fetchall()
    con.close()
    return render_template("list.html",rows=rows)

# select a specific row in the database then load an Edit form 
@app.route("/edit", methods=['POST','GET'])
def edit():
    if request.method == 'POST':
        try:            
            id = request.form['id']
            con = sqlite3.connect("database.db")
            con.row_factory = sqlite3.Row

            cur = con.cursor()
            cur.execute("SELECT rowid, * FROM students WHERE rowid = " + id)

            rows = cur.fetchall()
        except:
            id=None
        finally:
            con.close()
            return render_template("edit.html",rows=rows)

@app.route("/search", methods=['GET'])
def search():
    query = request.args.get('query')

    try:
        con = sqlite3.connect("database.db")
        con.row_factory = sqlite3.Row
        cur = con.cursor()
        cur.execute("SELECT rowid, * FROM students WHERE name LIKE ? OR idnum LIKE ? OR points LIKE ?", ('%' + query + '%', '%' + query + '%', '%' + query + '%'))
        rows = cur.fetchall()
        return render_template("search.html", query=query, results=rows)

    except Exception as e:
        msg = "An error occurred during search:" + str(e)
        
    finally:
        con.close()
        return render_template('result.html',msg=msg)

    

# to execute the UPDATE statement on a specific record in the database
@app.route("/editrec", methods=['POST','GET'])
def editrec():
 
    if request.method == 'POST':
        try:
            rowid = request.form['rowid']
            nm = request.form['nm']
            idnum = request.form['idnum']
            points = request.form['points']
            with sqlite3.connect('database.db') as con:
                cur = con.cursor()
                cur.execute("UPDATE students SET name='"+nm+"', idnum='"+idnum+"', points='"+points+"' WHERE rowid="+rowid)

                con.commit()
                msg = "Record successfully edited in the database"
        except:
            con.rollback()
            msg = "Error in the Edit: UPDATE students SET name="+nm+", idnum="+idnum+", points="+points+" WHERE rowid="+rowid

        finally:
            con.close()
            return render_template('result.html',msg=msg)

# delete a specific record in the database    
@app.route("/delete", methods=['POST','GET'])
def delete():
    if request.method == 'POST':
        try:
            rowid = request.form['id']
            with sqlite3.connect('database.db') as con:
                    cur = con.cursor()
                    cur.execute("DELETE FROM students WHERE rowid="+rowid)

                    con.commit()
                    msg = "Record successfully deleted from the database"
        except:
            con.rollback()
            msg = "Error in the DELETE"

        finally:
            con.close()
            return render_template('result.html',msg=msg)
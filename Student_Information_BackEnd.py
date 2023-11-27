import sqlite3

def connect():
       conn = sqlite3.connect("student.db")
       cur = conn.cursor()

       cur.execute("CREATE TABLE IF NOT EXISTS student (id INTEGER PRIMARY KEY, name text, fname text, mname text, \
                     address text, mobno integer,email text, dob integer, gender text)")

       conn.commit()
       conn.close()

def insert(name = " ", fname = " ", mname = " ", address = " ", mobno = " ", email = " ", dob = " ", gender = " "):
       conn = sqlite3.connect("student.db")
       cur = conn.cursor()

       cur.execute("INSERT INTO student VALUES (NULL,?,?,?,?,?,?,?,?)", (name, fname, mname, address , mobno, email, dob, gender))

       conn.commit()
       conn.close()
                                                                        

def view():
       conn = sqlite3.connect("student.db")
       cur = conn.cursor()

       cur.execute("SELECT * FROM student")
       rows = cur.fetchall()
       return rows

       conn.close()

def delete(id):
       conn = sqlite3.connect("student.db")
       cur = conn.cursor()

       cur.execute("DELETE FROM student WHERE id = ?", (id,))

       conn.commit()
       conn.close()

def update(id,name = " ", fname = " ", mname = " ", address = " ", mobno = " ", email = " ", dob = " ", gender = " "):
       conn = sqlite3.connect("student.db")
       cur = conn.cursor()

       cur.execute("UPDATE student SET name = ? OR fname = ? OR mname = ? OR address = ? OR mobno = ? OR email = ? OR dob = ? OR gender = ?", \
                   (name, fname, mname, address , mobno, email, dob, gender))

       conn.commit()
       conn.close()

def search(name="", fname="", mname="", address="", mobno="", email="", dob="", gender=""):
       con = sqlite3.connect("student.db")
       cur = con.cursor()

       query = "SELECT * FROM student WHERE"
       params = []
       if name:
              query += ' name LIKE ? AND'
              params.append('%' + name + '%')
       if fname:
              query += ' fname LIKE ? AND'
              params.append('%' + fname + '%')
       if mname:
              query += ' mname LIKE ? AND'
              params.append('%' + mname + '%')
       if address:
              query += ' address LIKE ? AND'
              params.append('%' + address + '%')
       if mobno:
              query += ' mobno LIKE ? AND'
              params.append('%' + mobno + '%')
       if email:
              query += ' email LIKE ? AND'
              params.append('%' + email + '%')
       if dob:
              query += ' dob LIKE ? AND'
              params.append('%' + dob + '%')
       if gender:
              query += ' gender = ? AND'
              params.append(gender)

       # Remove the trailing ' AND'
       if params:
              query = query[:-4]
       else:
              query = 'SELECT * FROM fee'

       cur.execute(query, params)
       rows = cur.fetchall()
       con.close()
       return rows
                                                               
connect()
       

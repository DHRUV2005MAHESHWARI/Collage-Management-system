import sqlite3

def connect():
       con = sqlite3.connect('library.db')
       cur = con.cursor()

       cur.execute('CREATE TABLE IF NOT EXISTS library(x INTEGER PRIMARY KEY, ID text, title text, author text, edsn text, yop text, borrow integer, due integer, issued_days integer, overdue_status text)')

       con.commit()
       con.close()

def insert(ID = ' ', title = ' ', author = ' ', edsn = ' ', yop = ' ', borrow = ' ', due = ' ', issued_days = ' ', overdue_status = ' '):
       con = sqlite3.connect('library.db')
       cur = con.cursor()

       cur.execute('INSERT INTO library VALUES (NULL,?,?,?,?,?,?,?,?,?)',(ID,title,author,edsn,yop,borrow,due,issued_days,overdue_status))

       con.commit()
       con.close()

def view():
      try:
         con = sqlite3.connect('library.db')
         cur = con.cursor()

         cur.execute('SELECT * FROM library')
         rows = cur.fetchall()
         return rows
      except sqlite3.Error as e:
         print(f"An error occurred: {e}")
         return None
      finally:
         if con:
            con.close()

def get_all_books():
   conn = sqlite3.connect('library.db')
   cursor = conn.cursor()

   try:
      cursor.execute("SELECT title FROM library")
      books = cursor.fetchall()
      return [book[0] for book in books]  # Extracting the titles from the query result
   except sqlite3.Error as e:
      print(f"An error occurred: {e}")
      return []
   finally:
      conn.close()

def get_book_details(title):
    conn = sqlite3.connect('library.db')
    cursor = conn.cursor()
    try:
        cursor.execute("SELECT * FROM library WHERE title = ?", (title,))
        book_details = cursor.fetchone()
        return book_details
    except sqlite3.Error as e:
        print(f"An error occurred: {e}")
        return None
    finally:
        conn.close()

def get_book_id(title):
    conn = sqlite3.connect('library.db')
    cursor = conn.cursor()
    try:
        cursor.execute("SELECT x FROM library WHERE title = ?", (title,))
        result = cursor.fetchone()
        return result[0] if result else None
    except sqlite3.Error as e:
        print(f"An error occurred: {e}")
        return None
    finally:
        conn.close()


def delete(x):
       con = sqlite3.connect('library.db')
       cur = con.cursor()
       cur.execute('DELETE FROM library WHERE x = ?',(x,))
       
       con.commit()
       con.close()
       
def update(x, ID, title, author, edsn, yop, borrow, due, issued_days, overdue_status):
    conn = sqlite3.connect('library.db')
    cursor = conn.cursor()
    try:
        cursor.execute("UPDATE library SET ID = ?, title = ?, author = ?, edsn = ?, yop = ?, borrow = ?, due = ?, issued_days = ?, overdue_status = ? WHERE x = ?", (ID, title, author, edsn, yop, borrow, due, issued_days, overdue_status, x))
        conn.commit()
    except sqlite3.Error as e:
        print(f"An error occurred: {e}")
    finally:
        conn.close()



def search(ID='', title='', author='', edsn='', yop='', borrow=''):
    con = sqlite3.connect('library.db')
    cur = con.cursor()

    query = 'SELECT * FROM library WHERE'
    params = []
    if ID:
       query += ' ID LIKE ? AND'
       params.append('%' + ID + '%')
    if title:
       query += ' title LIKE ? AND'
       params.append('%' + title + '%')
    if author:
       query += ' author LIKE ? AND'
       params.append('%' + author + '%')
    if edsn:
       query += ' edsn LIKE ? AND'
       params.append('%' + edsn + '%')
    if yop:
       query += ' yop LIKE ? AND'
       params.append('%' + yop + '%')
    if borrow:
       query += ' borrow LIKE ? AND'
       params.append('%' + borrow + '%')

    # Remove the trailing ' AND'
    if params:
       query = query[:-4]
    else:
       query = 'SELECT * FROM library'

    cur.execute(query, params)
    rows = cur.fetchall()
    con.close()
    return rows

connect()
       
       
       
                   
       

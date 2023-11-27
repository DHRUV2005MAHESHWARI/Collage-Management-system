import sqlite3

def connect():
       con = sqlite3.connect('fee.db')
       cur = con.cursor()

       cur.execute('CREATE TABLE IF NOT EXISTS fee(id INTEGER PRIMARY KEY, recpt integer, name text, admsn text, date integer, branch text, sem text, total integer, paid integer, due integer)')

       con.commit()
       con.close()

def insert(recpt = ' ', name = ' ', admsn = ' ', date = ' ', branch = ' ', sem = ' ', total = ' ', paid = ' ', due = ' '):
       con = sqlite3.connect('fee.db')
       cur = con.cursor()

       cur.execute('INSERT INTO fee VALUES (NULL,?,?,?,?,?,?,?,?,?)',(recpt,name,admsn,date,branch,sem,total,paid,due))

       con.commit()
       con.close()

def view():
       con = sqlite3.connect('fee.db')
       cur = con.cursor()
       cur.execute('SELECT * FROM fee')
       rows = cur.fetchall()

       con.close()
       return rows
       

def delete(id):
       con = sqlite3.connect('fee.db')
       cur = con.cursor()
       cur.execute('DELETE FROM fee WHERE id = ?',(id,))

       con.commit()
       con.close()

def update(id,recpt = ' ', name = ' ', admsn = ' ', date = ' ', branch = ' ', sem = ' ', total = ' ', paid = ' ', due = ' '):
       con = sqlite3.connect('fee.db')
       cur = con.cursor()
       #cur.execute('UPDATE fee SET recpt = ? OR name = ? OR admsn = ? OR date = ? OR branch = ? OR sem = ? OR total = ? OR paid = ? OR due = ?',(recpt,name,admsn,date,branch,sem,total,paid,due))
       cur.execute('UPDATE fee SET recpt = ?, name = ?, admsn = ?, date = ?, branch = ?, sem = ?, total = ?, paid = ?, due = ? WHERE id = ?', (recpt, name, admsn, date, branch, sem, total, paid, due, id))

       con.commit()
       con.close()

def search(recpt='', name='', admsn='', date='', branch='', sem='', total='', paid='', due=''):
    con = sqlite3.connect('fee.db')
    cur = con.cursor()

    query = 'SELECT * FROM fee WHERE'
    params = []
    if recpt:
       query += ' recpt LIKE ? AND'
       params.append('%' + recpt + '%')
    if name:
       query += ' name LIKE ? AND'
       params.append('%' + name + '%')
    if admsn:
       query += ' admsn LIKE ? AND'
       params.append('%' + admsn + '%')
    if date:
       query += ' date LIKE ? AND'
       params.append('%' + date + '%')
    if branch:
       query += ' branch LIKE ? AND'
       params.append('%' + branch + '%')
    if sem:
       query += ' sem LIKE ? AND'
       params.append('%' + sem + '%')
    if total:
       query += ' total = ? AND'
       params.append(total)
    if paid:
       query += ' paid = ? AND'
       params.append(paid)
    if due:
       query += ' due = ? AND'
       params.append(due)

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
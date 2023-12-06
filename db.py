import sqlite3

def create_table():
    conn = sqlite3.connect('todo.db')
    c = conn.cursor()
    c.execute('''
        CREATE TABLE IF NOT EXISTS Todos (
            id INTEGER PRIMARY KEY, 
            task text, 
            status text)''')
    conn.commit()
    conn.close()

def fetch_todos():
    conn = sqlite3.connect('todo.db')
    c = conn.cursor()
    c.execute('SELECT * FROM Todos')
    todos = c.fetchall()
    conn.close()
    return todos

def add_todo(id, task, status):
    conn = sqlite3.connect('todo.db')
    c = conn.cursor()
    c.execute('INSERT INTO Todos (id, task, status) VALUES (?, ?, ?)', (id, task, status))
    conn.commit()
    conn.close()

def update_todo(id, new_task, new_status):
    conn = sqlite3.connect('todo.db')
    c = conn.cursor()
    c.execute('UPDATE Todos SET task = ?, status = ? WHERE id = ?', (new_task, new_status, id))
    conn.commit()
    conn.close()

def delete_todo(id):
    conn = sqlite3.connect('todo.db')
    c = conn.cursor()
    c.execute('DELETE FROM Todos WHERE id = ?', (id,))
    conn.commit()
    conn.close()

def id_exists(id):
    conn = sqlite3.connect('todo.db')
    c = conn.cursor()
    c.execute('SELECT COUNT (*) FROM Todos WHERE id = ?', (id,))
    todo = c.fetchone()
    conn.close()
    return todo[0] > 0

create_table()
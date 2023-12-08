import sqlite3

def create_db():
    conn = sqlite3.connect('todo.db')
    c = conn.cursor()
    c.execute('''
        CREATE TABLE IF NOT EXISTS Todos (
            id INTEGER PRIMARY KEY,
            title TEXT,
            description TEXT,
            status TEXT
        )
    ''')
    conn.commit()
    conn.close()

def fetch_todos():
    try:
        conn = sqlite3.connect("todo.db")
        c = conn.cursor()
        c.execute('SELECT * FROM Todos')
        todos = c.fetchall()
        conn.close()
        return todos
    except Exception as e:
        print(f"Error fetching todos: {e}")
        return []    

def add_todo(title, description, status):
    conn = None
    try:
        conn = sqlite3.connect('todo.db')
        c = conn.cursor()
        c.execute("INSERT INTO Todos (title, description, status) VALUES (?, ?, ?)", (title, description, status))
        conn.commit()
        return True
    except Exception as e:
        print(f"Error adding todo: {e}")
        return False
    finally:
        if conn:
            conn.close()

def update_todo(new_title, new_description, new_status, id):
    conn = None
    try:
        conn = sqlite3.connect('todo.db')
        c = conn.cursor()
        c.execute("UPDATE Todos SET title = ?, description = ?, status = ? WHERE id = ?", (new_title, new_description, new_status, id))
        conn.commit()
        return True
    except Exception as e:
        print(f"Error updating todo: {e}")
        return False
    finally:
        if conn:
            conn.close()

def delete_todo(id):
    conn = sqlite3.connect('todo.db')
    c = conn.cursor()
    c.execute("DELETE FROM Todos WHERE id = ?", (id,))
    conn.commit()
    conn.close()

def id_exists(id):
    conn = sqlite3.connect('todo.db')
    c = conn.cursor()
    c.execute("SELECT COUNT (*) FROM Todos WHERE id = ?", (id,))
    todo = c.fetchone()
    conn.close()
    return todo[0] > 0

def search_todos(keyword):
    conn = sqlite3.connect('todo.db')
    c = conn.cursor()
    c.execute("SELECT * FROM Todos WHERE title LIKE ?", ('%' + keyword + '%'))
    todos = c.fetchall()
    conn.close()
    return todos

create_db()
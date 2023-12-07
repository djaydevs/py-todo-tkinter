import db
from customtkinter import *
from tkinter import messagebox

# Function to display tasks in the Treeview widget
def show_treeview():
    task = db.fetch_todos()
    tree.delete(*tree.get_children)
    for todo in task:
        tree.insert('', END, values=todo)

# Function to add a new task
def add_task():
    title_value = title_entry.get()
    description_value = description_entry.get()
    status_value = status_entry.get()

    if not (title_value and description_value and status_value):
        messagebox.showerror('Error', "Enter all fields")
    else:
        db.add_todo(title_value, description_value, status_value)
        show_treeview()
        clear_task()
        messagebox.showerror("Success", "To do have been added")

    print("Add Task button clicked")

# Function to update an existing task
def update_task():
    selected_task = tree.focus()
    if not selected_task:
        messagebox.showerror('Error', "Please select a task to update.")
    else:
        id_value = id_entry.get()
        title_value = title_entry.get()
        description_value = description_entry.get()
        status_value = status_entry.get()
        db.update_todo(title_value, description_value, status_value, id_value)
        show_treeview()
        clear_task()
        messagebox.showinfo("Success", "Task updated successfully.")
    print("Update Task button clicked")

# Function to delete an existing task
def delete_task():
    selected_task = tree.focus()
    if not selected_task:
        messagebox.showerror('Error', "Please select a task to delete.")
    else:
        id_value = id_entry.get()
        db.delete_todo(id_value)
        show_treeview()
        clear_task()
        messagebox.showinfo("Success", "Task deleted successfully.")
    print("Delete Task button clicked")

# Function to clear the input fields and selection in the Treeview
def clear_task(*clicked):
    if clicked:
        tree.selection_remove(tree.focus())
        tree.focus("")
    title_entry.delete(0, END)
    description_entry.delete(0, END)
    status_entry.delete(0, END)

# Function to display the details of a selected task
def show_task():
    selected_task = tree.focus()
    if selected_task: 
        row = tree.item(selected_task)['values']
        clear_task()
        title_entry.insert(0, row[0])
        description_entry.insert(0, row[1])
        status_entry.insert(0, row[2])
    else:
        pass

def search_task():
    keyword = search_entry.get()
    if not keyword:
        messagebox.showerror('Error', "Enter a keyword to search.")
        return
    results = db.search_todos(keyword)
    tree.delete(*tree.get_children())
    if not results:
        messagebox.showinfo("Search Results", "No matching tasks found.")
    else:
        for todo in results:
            tree.insert('', END, values=todo)

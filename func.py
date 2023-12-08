import db
from customtkinter import *
from tkinter import messagebox

# Function to add a new task
def add_task(title, description, status, tree):
    title_value = title.get()
    description_value = description.get("1.0", 'end-1c')  # Get text from the textbox
    status_value = status.get()

    if not (title_value and description_value and status_value):
        messagebox.showerror('Error', "Enter all fields")
    else:
        db.add_todo(title_value, description_value, status_value)
        show_treeview(tree)
        clear_task(title, description, status, tree)
        messagebox.showinfo("Success", "To do have been added")

    print("Add Task button clicked")

# Function to clear the input fields and selection in the Treeview
def clear_task(title, description, status, tree):
    title.delete(0, 'end')
    description.delete("1.0", 'end')  
    status.set('')
    show_treeview(tree)

def update_task(tree, titleEntry, descriptionTextBox, statusCombobox):
    selected_item = tree.selection()

    if not selected_item:
        messagebox.showerror('Error', "Please select a task to update.")
    else:
        values = tree.item(selected_item)['values']
        id = values[0]  

        new_title = titleEntry.get()
        new_description = descriptionTextBox.get("1.0", 'end-1c')
        new_status = statusCombobox.get()

        db.update_todo(new_title, new_description, new_status, id)
        clear_task(titleEntry, descriptionTextBox, statusCombobox, tree)
        show_treeview(tree)
        messagebox.showinfo("Success", "Task updated successfully.")

# Function to delete an existing task
def delete_task(title, description, status, tree):
    selected_item = tree.selection()

    if not selected_item:
        messagebox.showerror('Error', "Please select a task to delete.")
    else:
        values = tree.item(selected_item)['values']
        id = values[0]  # Get the ID from the tuple
        db.delete_todo(id)
        show_treeview(tree)
        clear_task(title, description, status, tree)
        messagebox.showinfo("Success", "Task deleted successfully.")

# Function to display the details of a selected task
def on_treeview_select(event, titleEntry, descriptionTextBox, statusCombobox):
    treeview = event.widget
    selected_item = treeview.selection()

    if selected_item:
        values = treeview.item(selected_item)['values']

        titleEntry.delete(0, 'end')
        descriptionTextBox.delete('1.0', 'end')
        statusCombobox.set('')

        titleEntry.insert('end', values[1])  
        descriptionTextBox.insert('end', values[2])  
        statusCombobox.set(values[3])  

# Function to search for a task
def search_task(tree, searchEntry):
    keyword = searchEntry.get()
    if not keyword:
        messagebox.showerror('Error', "Enter a keyword to search.")
        return

    all_items = tree.get_children()
    matching_items = [item for item in all_items if keyword.lower() in tree.item(item)['values'][1].lower()]
    non_matching_items = [item for item in all_items if item not in matching_items]

    tree.delete(*non_matching_items)

def on_search_entry_key_release(event, tree, searchEntry):
    keyword = searchEntry.get()
    if not keyword:  # If the search entry is empty
        show_treeview(tree)  # Display all tasks

# Function to display tasks in the Treeview widget
def show_treeview(treeview):
    todos = db.fetch_todos()
    for i in treeview.get_children():
        treeview.delete(i)
    for todo in todos:
        treeview.insert('', 'end', values=(todo[0], todo[1], todo[2], todo[3]))

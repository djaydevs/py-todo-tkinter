import db
from customtkinter import *
from tkinter import messagebox

# Function to add a new task
def add_task(title, description, status, taskList):
    title_value = title.get()
    description_value = description.get("1.0", 'end-1c')  # Get text from the textbox
    status_value = status.get()

    if not (title_value and description_value and status_value):
        messagebox.showerror('Error', "Enter all fields")
    else:
        db.add_todo(title_value, description_value, status_value)
        show_listbox(taskList)
        clear_task(title, description, status, taskList)
        messagebox.showinfo("Success", "To do have been added")

        todos = db.fetch_todos()
        for todo in todos:
            print(todo)
    print("Add Task button clicked")

# Function to clear the input fields and selection in the Treeview
def clear_task(title, description, status, taskList):
    title.delete(0, 'end')
    description.delete("1.0", 'end')  
    status.set('')
    show_listbox(taskList)

def update_task(taskList, titleEntry, descriptionTextBox, statusCombobox):
    selected_index = taskList.curselection()
    
    if not selected_index:
        messagebox.showerror('Error', "Please select a task to update.")
    else:
        selected_item = taskList.get(selected_index)
        id = selected_item[0]  

        new_title = titleEntry.get()
        new_description = descriptionTextBox.get("1.0", 'end-1c')
        new_status = statusCombobox.get()

        db.update_todo(new_title, new_description, new_status, id)
        clear_task(titleEntry, descriptionTextBox, statusCombobox, taskList)
        show_listbox(taskList)
        messagebox.showinfo("Success", "Task updated successfully.")

# Function to delete an existing task
def delete_task(title, description, status, taskList):
    selected_index = taskList.curselection()
    if not selected_index:
        messagebox.showerror('Error', "Please select a task to delete.")
    else:
        selected_item = taskList.get(selected_index)
        id = selected_item[0]  # Get the ID from the tuple
        print(f"Selected id: {id}") 
        db.delete_todo(id)
        show_listbox(taskList)
        clear_task(title, description, status, taskList)
        messagebox.showinfo("Success", "Task deleted successfully.")
    print("Delete Task button clicked")

# Function to display the details of a selected task
def on_listbox_select(event, titleEntry, descriptionTextBox, statusCombobox):
    listbox = event.widget
    selected_index = listbox.curselection()

    if selected_index:
        selected_item = listbox.get(selected_index)

        titleEntry.delete(0, END)
        descriptionTextBox.delete('1.0', END)
        statusCombobox.set('')

        titleEntry.insert(END, selected_item[1])  
        descriptionTextBox.insert(END, selected_item[2])  
        statusCombobox.set(selected_item[3])  

# Function to search for a task
def search_task(taskList, searchEntry):
    keyword = searchEntry.get()
    if not keyword:
        messagebox.showerror('Error', "Enter a keyword to search.")
        return

    all_items = taskList.get(0, 'end')
    taskList.delete(0, 'end')

    for item in all_items:
        item_str = item[1]  # Consider the title, not the id
        if keyword.lower() in item_str.lower():
            taskList.insert('end', item)

# Function to display tasks in the Listbox widget
def show_listbox(listbox):
    todos = db.fetch_todos()
    listbox.delete(0, END) 
    for todo in todos:
        listbox.insert(END, (todo)) 

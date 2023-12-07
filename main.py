from customtkinter import *
from PIL import Image as PILImage
from CTkTable import *
from tkinter import *
from tkinter import ttk
import tkinter as tk
from tkinter import messagebox
from tkinter import Listbox
import db
import func

light = '#f8fdf7'
light2 = '#e0e0e0'
dark = '#030802'
dark2 = '#020d0a'
primary = '#2bdeae'
secondary = '#83c2ec'
accent = '#608de6'
destructive = '#e15b5b'

app = CTk()
app.title('Todo App')
app.geometry('900x600')
set_appearance_mode('dark')
app.resizable(False, False)

font20 = ('Arial', 20)
font20_bold = ('Arial', 20, 'bold')
font14 = ('Arial', 14)
font14_bold = ('Arial', 14, 'bold')
font12 = ('Arial', 12)
font12_bold = ('Arial', 12, 'bold')

plus_icon = PILImage.open('assets/plus-circle.png')

titleLabel = CTkLabel(app, text="Todo Application", font=font20_bold)
titleLabel.pack(anchor='c', pady=5, padx=10, fill='x')

mainFrame = CTkFrame(app, fg_color='transparent', corner_radius=20)
mainFrame.pack(anchor='nw', expand=True, fill='both')

addFrame = CTkFrame(mainFrame, fg_color=dark2, corner_radius=20)
addFrame.grid(row=0, column=0, sticky='nsew', padx=(10, 0), pady=10)

addLabel = CTkLabel(addFrame, text="Add or Update Task", font=font14_bold, text_color=light)

addTitleLabel = CTkLabel(addFrame, text="Title", font=font12_bold, text_color=light)
titleEntry = CTkEntry(
    addFrame, 
    font=font12, 
    fg_color=light, 
    text_color=dark, 
    border_width=0,
    corner_radius=15
)

addStatusLabel = CTkLabel(addFrame, text="Status", font=font12_bold, text_color=light)
statusCombobox = CTkComboBox(
    addFrame, 
    font=font12,
    hover=True,
    border_width=0,
    button_color=primary,
    fg_color=light, 
    dropdown_fg_color=light,
    dropdown_hover_color=secondary,
    dropdown_text_color=dark,
    text_color=dark, 
    corner_radius=15, 
    state='readonly',
    values=['Todo', 'In Progress', 'Done']
)

descriptionLabel = CTkLabel(addFrame, text="Description", font=font12_bold, text_color=light)
descriptionTextBox = CTkTextbox(
    addFrame, 
    width=250, 
    border_color=dark, 
    font=font12, 
    fg_color=light, 
    text_color=dark, 
    corner_radius=15
)

saveTaskBtn = CTkButton(
    addFrame,
    height=40,
    font=font14_bold,
    text_color=light,
    text="Save Task",
    fg_color=primary,
    hover_color=accent,
    cursor='hand2',
    corner_radius=32,
    image=CTkImage(dark_image=plus_icon, light_image=plus_icon),
    command=func.add_task,
)

addLabel.pack(anchor='w', padx=15, pady=(10, 5))
addTitleLabel.pack(anchor='w', padx=15)
titleEntry.pack(anchor='w', padx=15, pady=(0, 10), fill='x')
addStatusLabel.pack(anchor='w', padx=15)
statusCombobox.pack(anchor='w', padx=15, pady=(0, 10), fill='x')
descriptionLabel.pack(anchor='w', padx=15)
descriptionTextBox.pack(anchor='w', padx=15, pady=(0, 10), fill='both', expand=True)
saveTaskBtn.pack(anchor='e', pady=10, padx=15)

listFrame = CTkFrame(mainFrame, fg_color=dark2, corner_radius=20)
listFrame.grid(row=0, column=1, sticky='nsew', padx=10, pady=10)

listLabel = CTkLabel(listFrame, text="List of Tasks", font=font14_bold, text_color=light)
searchEntry = CTkEntry(
    listFrame, 
    placeholder_text="Search",
    font=font12, 
    fg_color=light, 
    text_color=dark, 
    border_width=0,
    corner_radius=15,
)
taskList = Listbox(
    listFrame,
    font=font12, 
    fg=light, 
    borderwidth=0, 
    highlightthickness=0, 
    selectbackground=primary, 
    selectforeground=light, 
    activestyle='none', 
    cursor='hand2',
)

listLabel.pack(anchor='w', padx=15, pady=(10, 5))
searchEntry.pack(anchor='w', padx=15, pady=(0, 10), fill='x')
taskList.pack(anchor='w', padx=15, pady=(0, 10), fill='both', expand=True)

mainFrame.grid_columnconfigure(0, weight=1)
mainFrame.grid_columnconfigure(1, weight=6)
mainFrame.grid_rowconfigure(0, weight=1)

#uncomment the following line of code if the treeview is created
#tree.bind('ButtonRelease', func.show_task)
# func.show_treeview()

app.mainloop()

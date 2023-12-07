from customtkinter import *
from PIL import Image as PILImage
from tkinter import *
from tkinter import ttk
import tkinter as tk
from tkinter import messagebox
import db
import func

light = '#f8fdf7'
dark = '#030802'
primary = '#52d930'
secondary = '#869dea'
accent = '#955be1'
destructive = '#e15b5b'

app = CTk()
app.title('Todo App')
app.geometry('600x700')
set_appearance_mode('dark')
app.resizable(False, False)

font20 = ('Arial', 20)
font20_bold = ('Arial', 20, 'bold')
font14 = ('Arial', 14)
font14_bold = ('Arial', 14, 'bold')
font12 = ('Arial', 12)
font12_bold = ('Arial', 12, 'bold')

plus_icon = PILImage.open('assets/plus-circle.png')

addTaskBtn = CTkButton(
    app,
    height=40,
    font=font14_bold,
    text_color=light,
    text="New Task",
    fg_color=primary,
    hover_color=secondary,
    cursor='hand2',
    corner_radius=32,
    image=CTkImage(dark_image=plus_icon, light_image=plus_icon),
    command=func.add_task,
)
addTaskBtn.place(x=10, y=10)

#uncomment the following line of code if the treeview is created
#tree.bind('ButtonRelease', func.show_task)
func.show_treeview()

app.mainloop()

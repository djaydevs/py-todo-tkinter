import customtkinter
from tkinter import *
from tkinter import ttk
import tkinter as tk
from tkinter import messagebox
import db

app = customtkinter.CTk()
app.title('Todo App')
app.geometry('500x500')
app.configure(bg='#fff')
app.resizable(False, False)

font1 = ('Arial', 20)
font2 = ('Arial', 12)

app.mainloop()
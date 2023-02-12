# import tkinter
# import customtkinter

# customtkinter.set_appearance_mode("System")
# customtkinter.set_default_color_theme("blue")

# app = customtkinter.CTk()
# app.geometry("720x480")
# app.title("Intelsat Asset Collector")

# app.mainloop()

# -----------------------------------------------------------------------------------------------------------
# ------------------------------------------IMPORT FUNCTIONS-------------------------------------------------
# -----------------------------------------------------------------------------------------------------------

from tkinter import *
import ttkbootstrap as tb
from ttkbootstrap.tableview import Tableview
from ttkbootstrap.constants import *
from PIL import ImageTk, Image

import mysql.connector


# ------------------------------------------------------------------------------------------------------------------
# ------------------------------------------INITIALIZATION OF APP / MYSQL-------------------------------------------
# ------------------------------------------------------------------------------------------------------------------

mydb = mysql.connector.connect(
  host="localhost",
  user="root",
  password="",
  database="vrdb"
)


root = tb.Window(themename="cerculean")
root.geometry("1920x1080")
colors = root.style.colors


# -------------------------------------------------------------------------------------------------------------------
# ------------------------------------------GETTING ALL THE TABLES FROM DB-------------------------------------------
# -------------------------------------------------------------------------------------------------------------------


mycursor = mydb.cursor()
mycursor.execute(f"SHOW tables;")
myresult = mycursor.fetchall()
tables = []
for i in myresult:
    tables.append(i[0])
print("Tables : ",tables)


# -----------------------------------------------------------------------------------------------------------
# ------------------------------------------SAMPLE FUNCTION-------------------------------------------------
# -----------------------------------------------------------------------------------------------------------

def insert_func():
    insertWindow = Toplevel(root)
    insertWindow.title("Insert")
    insertWindow.geometry("200x200")
    new_Label = tb.Label(insertWindow,text="You Just clicked Insert")
    new_Label.pack(pady=25)


# ------------------------------------------------------------------------------------------------------------
# ------------------------------------------GET ALL TABLES FUNCTION-------------------------------------------
# ------------------------------------------------------------------------------------------------------------
    
def get_all_tables():
    global nice
    nice = table_selector.get()
    print("FROM FUNCTION : ",nice)
    
# -----------------------------------------------------------------------------------------------------------
# ------------------------------------------DISPLAY TABLE FUNCTION-------------------------------------------
# -----------------------------------------------------------------------------------------------------------

def display_func():
    displayWindow = Toplevel(root)
    displayWindow.title("Display")
    displayWindow.geometry("1024x720")
    dv = tb.tableview.Tableview(
        master=displayWindow,
        paginated=True,
        searchable=True,
        bootstyle=SUCCESS,
        pagesize=10,
        height=10,
        stripecolor=(colors.light, None),
    )
    dv.grid(row=0, column=0, padx=5, pady=5)

    table_name = nice

    # Collect Headers 1st
    mycursor = mydb.cursor()
    mycursor.execute(f"SHOW columns FROM {table_name}")
    myresult = mycursor.fetchall()
    # print(type(myresult))
    l1 = [] #l1 => Column Names
    for i in myresult:
        l1.append(i[0])

    # Collect Data
    mycursor.execute(f"SELECT * FROM {table_name}")
    myresult = mycursor.fetchall()
    r_set = [] #r_set => Table Data
    for i in myresult:
        r_set.append(i)

    # l1 = [r for r in r_set.keys()]
    # r_set = [list(r) for r in r_set]
    dv.build_table_data(l1, r_set)  # adding column and row data
    dv.load_table_data()  # refresh the table view with data
    dv.autofit_columns()  # Adjust with available space
    dv.autoalign_columns()  # String left and Numbers to right



# -----------------------------------------------------------------------------------------------------------
# ------------------------------------------DISPLAY WELCOME PICTURE-------------------------------------------
# ------------------------------------------------------------------------------------------------------------

open_image = Image.open("F:/Coding Projects/Python Projects/superman.png")
resized_image = open_image.resize((500,130))
img = ImageTk.PhotoImage(resized_image)
panel = Label(root, image = img)
panel.pack(side = "top", fill = "both",padx=20,pady=50)
# panel.place(relx=0.6,rely=0.1)


# ---------------------------------------------------------------------------------------------------
# ------------------------------------------WELCOME LABEL-------------------------------------------
# ---------------------------------------------------------------------------------------------------

# Welcome Screen
welcome_label = tb.Label(text='Welcome',font=("Montserrat", 20), bootstyle='info',borderwidth=1,relief="solid")
# welcome_label.config(anchor=CENTER)
welcome_label.pack(padx=150,pady=50)
# welcome_label.place(relx=0.7,rely=0.3)

# Password Input
# password_label = tb.Label(text='Enter the Username',font=("Montserrat", 13), bootstyle='warning')
# password_label.pack(pady=0)
# password_label.place(relx=0.68,rely=0.4)

# insert_button = tb.Button(text="Insert",width=35,bootstyle='warning',command=insert_func)

# ---------------------------------------------------------------------------------------------------
# ------------------------------------------TABLE SELECTOR-------------------------------------------
# ---------------------------------------------------------------------------------------------------

table_label = tb.Label(text='Select the Table',font=("Montserrat", 13), bootstyle='warning')
table_label.pack(padx=50,pady=2)

sel=tb.StringVar()
table_selector = tb.Combobox(values=tables,textvariable=sel)
table_selector.pack(padx=80,pady=10)
table_selector.current()

set_table_button = tb.Button(text='Set the table',width=3,bootstyle='danger',command=get_all_tables)
set_table_button.pack(padx=80,pady=10)

# ---------------------------------------------------------------------------------------------------
# ------------------------------------------DISPLAY BUTTON-------------------------------------------
# ---------------------------------------------------------------------------------------------------

# Display Button 
display_button = tb.Button(text='Display',width=35,bootstyle='primary',command=display_func)
display_button.pack(padx=80,pady=20)
# login.place(relx=0.62,rely=0.55)

root.mainloop()

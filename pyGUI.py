# import tkinter
# import customtkinter

# customtkinter.set_appearance_mode("System")
# customtkinter.set_default_color_theme("blue")

# app = customtkinter.CTk()
# app.geometry("720x480")
# app.title("Intelsat Asset Collector")

# app.mainloop()

from tkinter import *
import ttkbootstrap as tb
from ttkbootstrap.tableview import Tableview
from ttkbootstrap.constants import *
from PIL import ImageTk, Image



import mysql.connector

mydb = mysql.connector.connect(
  host="localhost",
  user="root",
  password="",
  database="vrdb"
)


root = tb.Window(themename="cerculean")
root.geometry("1920x1080")
colors = root.style.colors


mycursor = mydb.cursor()
mycursor.execute(f"SHOW tables;")
myresult = mycursor.fetchall()
tables = []
for i in myresult:
    tables.append(i[0])
print("Tables : ",tables)

def insert_func():
    insertWindow = Toplevel(root)
    insertWindow.title("Insert")
    insertWindow.geometry("200x200")
    new_Label = tb.Label(insertWindow,text="You Just clicked Insert")
    new_Label.pack(pady=25)


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

    table_name = 'profilepicture'

    # Collect Headers 1st
    mycursor = mydb.cursor()
    mycursor.execute(f"SHOW columns FROM {table_name}")
    myresult = mycursor.fetchall()
    print(type(myresult))
    l1 = []
    for i in myresult:
        l1.append(i[0])

    # Collect Data
    mycursor.execute(f"SELECT * FROM {table_name}")
    myresult = mycursor.fetchall()
    r_set = []
    for i in myresult:
        r_set.append(i)

    # l1 = [r for r in r_set.keys()]
    # r_set = [list(r) for r in r_set]
    dv.build_table_data(l1, r_set)  # adding column and row data
    dv.load_table_data()  # refresh the table view with data
    dv.autofit_columns()  # Adjust with available space
    dv.autoalign_columns()  # String left and Numbers to right



# Intelsat Logo
# intelsat_label = tb.Label(text='Intelsat',font=("Montserrat", 30), bootstyle='warning')
# intelsat_label.pack(padx=50,pady=25)
open_image = Image.open("F:/Coding Projects/Python Projects/intesat.png")
resized_image = open_image.resize((500,130))
img = ImageTk.PhotoImage(resized_image)
panel = Label(root, image = img)
panel.pack(side = "top", fill = "both",padx=20,pady=50)
# panel.place(relx=0.6,rely=0.1)

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



sel=tb.StringVar()
table_selector = tb.Combobox(values=tables,textvariable=sel)
table_selector.pack(padx=80,pady=10)
table_selector.current()

# def setter():
#     global sel
#     sel = sel.get()


# set_table = tb.Button(text='Set the table',width=3,bootstyle='danger',command=setter)
# set_table.pack(padx=80,pady=10)

print("ATLAST GOT IT : ",str(sel.get()))


# password = tb.Entry(bootstyle='info',width=50)
# password.pack(padx=50,pady=10)
# password.place(relx=0.62,rely=0.47)

# Login Button 
login = tb.Button(text='Display',width=35,bootstyle='primary',command=display_func)
login.pack(padx=80,pady=20)
# login.place(relx=0.62,rely=0.55)

root.mainloop()

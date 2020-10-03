from tkinter import *
import sqlite3
from tkinter.filedialog import *

root = Tk()
root.title("STUDENT DATA")


def submit_to():
    conn = sqlite3.connect('names.db')
    c = conn.cursor()
    # Create a db file initially and comment out next lines as they are made to auto create database.
    c.execute("""CREATE TABLE IF NOT EXISTS name(
    name text,
    father_name text,
    mother_name text,
    ssm integer,
    aadhar integer,
    category text,
    gender text,
    fees integer,
    total integer,
    address text,
    sibling integer,
    account integer
    )
    """)
    c.execute("""INSERT INTO name VALUES(:name,:father_name,:mother_name,:ssm,:aadhar,:category,
    :gender,:fees,:total,:address,:sibling,:account)""", {
        'name': name.get(),
        'father_name': father_name.get(),
        'mother_name': mother_name.get(),
        'ssm': ssm.get(),
        'aadhar': aadhar.get(),
        'category': cat.get(),
        'gender': gen.get(),
        'fees': fees.get(),
        'total': total.get(),
        'address': address.get(),
        'sibling': sibling.get(),
        'account': account.get()

    }
              )
    conn.commit()
    conn.close()
    name.delete(0, END)
    father_name.delete(0, END)
    mother_name.delete(0, END)
    cat.set("SELECT CATEGORY")
    gen.set("SELECT GENDER")
    fees.delete(0, END)
    total.delete(0, END)
    address.delete(0, END)
    sibling.delete(0, END)
    account.delete(0, END)
    aadhar.delete(0, END)
    ssm.delete(0, END)


head = Label(root, text="Database creater", anchor="e", font=("Helvetica", 25))
head.grid(row=0, column=0, pady=10, columnspan=4)

name_label = Label(root, text="Full Name:-")
name_label.grid(row=1, column=0, pady=5)
name = Entry(root,width=60)
name.grid(row=1, column=1, padx=10, pady=5,columnspan=3)

father_name_label = Label(root, text="Father's Name:-")
father_name_label.grid(row=2, column=0, pady=5)
father_name = Entry(root)
father_name.grid(row=2, column=1, padx=10, pady=5)

mother_name_label = Label(root, text="Mother's Name:-")
mother_name_label.grid(row=2, column=2, pady=5)
mother_name = Entry(root)
mother_name.grid(row=2, column=3, padx=10, pady=5)

ssm_label = Label(root, text="SSM's ID")
ssm_label.grid(row=3, column=0, pady=5)
ssm = Entry(root)
ssm.grid(row=3, column=1, padx=10, pady=5)

aadhar_label = Label(root, text="Aadhar No:-")
aadhar_label.grid(row=3, column=2, pady=5)
aadhar = Entry(root)
aadhar.grid(row=3, column=3, padx=10, pady=5)

category_label = Label(root, text="Category:-")
category_label.grid(row=4, column=0, pady=5)
cat = StringVar(root)
cat.set("SELECT CATEGORY")
category = OptionMenu(root, cat, "GENERAL", "SC", "ST", "OBC")
category.grid(row=4, column=1, padx=10, pady=5)

gender_label = Label(root, text="Gender:-")
gender_label.grid(row=4, column=2, pady=5)
gen = StringVar()
gen.set("SELECT GENDER")
gender = OptionMenu(root, gen, "MALE", "FEMALE", "OTHER")
gender.grid(row=4, column=3, padx=10, pady=5)

fees_label = Label(root, text="Total Fees:-")
fees_label.grid(row=5, column=0, pady=5)
fees = Entry(root)
fees.grid(row=5, column=1, padx=10, pady=5)

total_label = Label(root, text="Total Marks:-")
total_label.grid(row=5, column=2, pady=5)
total = Entry(root)
total.grid(row=5, column=3, padx=1, pady=5)

address_label = Label(root, text="Address:-")
address_label.grid(row=6, column=0, padx=10, pady=5)
address = Entry(root, width=60)
address.grid(row=6, column=1, padx=10, pady=5, columnspan=3)

sibling_label = Label(root, text="Number of brother/sister")
sibling_label.grid(row=7, column=0, padx=10, pady=5)
sibling = Entry(root)
sibling.grid(row=7, column=1, padx=10, pady=5)

account_label = Label(root, text="Account number")
account_label.grid(row=7, column=2, padx=10, pady=5)
account = Entry(root)
account.grid(row=7, column=3, padx=10, pady=5)


Button(root, text="Add to database", command=submit_to).grid(row=8, column=0, columnspan=4, padx=10, pady=10)


root.mainloop()

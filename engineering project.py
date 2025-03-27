#Modern Farmer's mentor -- report generator

#modules imported

#for machine learning component
import sklearn

#To work with files
import pickle #binary files 
import csv #csv files

#for plots
import matplotlib

#for data set generation part
import pandas as pd
import numpy as np

#for mysql interfacing
import mysql.connector as ms
mycon = ms.connect(host="localhost",user="root",passwd="lkarmy2005",database="proj") #establishing connection
mycursor = mycon.cursor() #creating cursor object

#for output - GUI representation
import tkinter as tk

#udf to handle signup - getting user input
def sign_up():
    #user inputs
    name = name_entry.get()
   
    password = password_entry.get()
    budget = budget_entry.get()
    soil = soil_entry.get()
    crop = crop_entry.get()
    weather = weather_entry.get()
    phoneno=phoneno_entry.get()
    query = "insert into inputTable values('{0}','{1}',{2},'{3}','{4}','{5}',{6}')".format(name,password,budget,soil,crop,weather,phoneno)
    mycursor.execute(query)
    mycon.commit()
    mycon.close()
    clear_entries()

def clear_entries():
    name_entry.delete(0,tk.END)
    phoneno_entry.delete(0,tk.END)
    budget_entry.delete(0,tk.END)
    soil_entry.delete(0,tk.END)
    crop_entry.delete(0,tk.END)
    weather_entry.delete(0,tk.END)
    password_entry.delete(0,tk.END)

def login():
    username = username_entry.get()
    password = password_entry.get()
    phoneno=phoneno_entry.get()
    un=input("enter un")
    passwd=input("epasswd")
    
    query = "select * from inputTable where name='{}' and password='{}'".format(un,passwd)
    mycursor.execute(query)
    result = mycursor.fetchall()
    
    if result!=None and result!=[]:
        status_label.config(text="Login successful!!!",fg="green")
    else:
        status_label.config(text="Invalid username or password!!!",fg="red")
    mycon.commit()
    mycon.close()

root = tk.Tk()
root.title("Modern Farmer's Mentor - Report generator")
tk.Label(root,text="Welcome to the Modern Farmer's Mentor",font=("Helvetica",16)).grid(row=0, columnspan=2, pady=10)



# Login Frame
login_frame = tk.Frame(root)
login_frame.grid(row=1, column=0, padx=20)

tk.Label(login_frame, text="Username:").grid(row=0, column=0, sticky="w")
tk.Label(login_frame, text="Password:").grid(row=1, column=0, sticky="w")
tk.Label(login_frame, text="phoneno").grid(row=2, column=0, sticky="w")

username_entry = tk.Entry(login_frame)
password_entry = tk.Entry(login_frame,show="*")
phoneno_entry = tk.Entry(login_frame)

username_entry.grid(row=0, column=1, padx=5, pady=5)
password_entry.grid(row=1, column=1, padx=5, pady=5)
phoneno_entry.grid(row=2, column=1, padx=5, pady=5)

login_button = tk.Button(login_frame, text="Loggin", command=login)
login_button.grid(row=3, columnspan=2, pady=10)

status_label = tk.Label(login_frame, text="", fg="green")
status_label.grid(row=3, columnspan=2)

# Sign Up Frame
signup_frame = tk.Frame(root)
signup_frame.grid(row=1, column=1, padx=20)

tk.Label(signup_frame, text="Name:").grid(row=0, column=0, sticky="w")
tk.Label(signup_frame, text="Password:").grid(row=1, column=0, sticky="w")
tk.Label(signup_frame, text="Budget:").grid(row=2, column=0, sticky="w")
tk.Label(signup_frame, text="Soil:").grid(row=3, column=0, sticky="w")
tk.Label(signup_frame, text="Crop:").grid(row=4, column=0, sticky="w")
tk.Label(signup_frame, text="Weather:").grid(row=5, column=0, sticky="w")
tk.Label(signup_frame, text="phoneno").grid(row=6, column=0, sticky="w")

name_entry = tk.Entry(signup_frame)
password_entry = tk.Entry(signup_frame, show="*")
budget_entry = tk.Entry(signup_frame)
soil_entry = tk.Entry(signup_frame)
crop_entry = tk.Entry(signup_frame)
weather_entry = tk.Entry(signup_frame)
phoneno_entry = tk.Entry(signup_frame)

name_entry.grid(row=0, column=1, padx=5, pady=5)
password_entry.grid(row=1, column=1, padx=5, pady=5)
budget_entry.grid(row=2, column=1, padx=5, pady=5)
soil_entry.grid(row=3, column=1, padx=5, pady=5)
crop_entry.grid(row=4, column=1, padx=5, pady=5)
weather_entry.grid(row=5, column=1, padx=5, pady=5)
phoneno_entry.grid(row=6, column=1, padx=5, pady=5)

signup_button = tk.Button(signup_frame, text="Sign Up", command=sign_up)
signup_button.grid(row=7, columnspan=2, pady=10)

root.mainloop()



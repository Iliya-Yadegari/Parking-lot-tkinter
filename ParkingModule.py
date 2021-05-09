from tkinter import *
import mysql.connector as msc

def write_fun(hourEntered,minEntered,hourExit,minExit,vehicle):
    
    if hourEntered == '' or minEntered == '' or hourExit == '' or minExit == '':
        
        messagebox.showerror('Error','You have left one or more of the areas blank')
        
    else:    
        sqlCommand = 'INSERT INTO parkingtimes (hourEntered,minEntered,hourExit,minExit,vehicle) VALUES (%s,%s,%s,%s,%s)'
        values = (hourEntered,minEntered,hourExit,minExit,vehicle)
        
        mycursor.execute(sqlCommand,values)
        mydb.commit()
        messagebox.showinfo('Result','Your infomation has been successfully stored.')
        
mydb = msc.connect(
    host = 'localhost',
    user = 'root',
    password = '',
    database = 'parkinglot'
    )
mycursor = mydb.cursor()
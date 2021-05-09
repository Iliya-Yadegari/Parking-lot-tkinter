from tkinter import *
import ParkingModule as pm

window = Tk()

window.title('Parking Lot times')
window.iconbitmap('parking-area.ico')

r = StringVar()
optionLst = ['car','bus','truck']
r.set(optionLst[0])

hourEntered_lbl = Label(window,text = 'Enter the hour in which you entered this parking lot(0 - 24) ===>').grid(row = 0, column = 0, padx = 10, pady = 10)
hourEntered_ent = Entry(window)
minEntered_lbl = Label(window,text = 'Enter the minute in which you entered this parking lot(0 - 59) ===>').grid(row = 1, column = 0, padx = 10, pady = 10)
minEntered_ent = Entry(window)
hourExit_lbl = Label(window,text = 'Enter the hour in which you exited this parking lot(0 - 24) ===>').grid(row = 2, column = 0, padx = 10, pady = 10)
hourExit_ent = Entry(window)
minExit_lbl = Label(window,text = 'Enter the minute in which you exited this parking lot(0 - 59) ===>').grid(row = 3, column = 0, padx = 10, pady = 10)
minExit_ent = Entry(window)
drop = OptionMenu(window,r,*optionLst).grid(row = 4, column = 0, padx = 10, pady = 10)
submit_btn = Button(window,text = 'Submit',width = 20,height = 3, command = lambda: pm.write_fun(hourEntered_ent.get(),minEntered_ent.get(),hourExit_ent.get(),minExit_ent.get(),r.get())).grid(row = 5, column = 0, padx = 10, pady = 10)

hourEntered_ent.grid(row = 0, column = 1, padx = 10, pady = 10)
minEntered_ent.grid(row = 1, column = 1, padx = 10, pady = 10)
hourExit_ent.grid(row = 2, column = 1, padx = 10, pady = 10)
minExit_ent.grid(row = 3, column = 1, padx = 10, pady = 10)

window.mainloop()
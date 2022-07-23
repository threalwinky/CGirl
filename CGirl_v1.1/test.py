import os
import datetime
from time import *
from datetime import datetime
from datetime import date

from tkinter import *
from tkinter.ttk import *


root = Tk()
root.title("Em be loli nhac thi")
root.iconbitmap("abc.ico")

root.geometry("1280x720+50+0")

bg = PhotoImage(file = "bg.png")

def calendar():
	time_1 = datetime.now()
	time_2 = datetime.strptime('2024:7:8:7:00:00',"%Y:%m:%d:%H:%M:%S")

	time_interval = time_2 - time_1
	time_interval_list = (str(time_interval)).split()
	print(time_interval_list)
	time_interval_string = "Còn " + time_interval_list[0] + " ngày, \n" + time_interval_list[2][:-13] + " giờ, " + time_interval_list[2][-12:-10] + " phút, \n" + time_interval_list[2][-9:-7] + " giây nữa là thi\nTHPT quốc gia \nrồi đó onii-chan."
	label1.config(text = time_interval_string)
	label1.after(1000, calendar)


label = Label(root,image = bg, font = ("Grave Snatchers.ttf", 50), background = 'black', foreground = 'red')
label.place(x = 0, y = 0)
label1 = Label( root,  font = ("TimesNewRoman", 32), background = 'white', foreground = 'black')
label1.place(x = 10, y = 20)
label.pack(anchor = 'center')
calendar()
root.mainloop()
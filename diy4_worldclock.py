import time
import pytz
from tkinter import *
from datetime import datetime

root = Tk()
root.geometry("500x300")

def times():
    home = pytz.timezone('Asia/Kolkata')
    time = datetime.now(home)
    current_time = time.strftime("%H:%M:%S")
    clock1.config(text=current_time)
    name1.config(text='India')

    home = pytz.timezone('America/New_York')
    time = datetime.now(home)
    current_time = time.strftime("%H:%M:%S")
    clock2.config(text=current_time)
    name2.config(text='USA')

    home = pytz.timezone('Australia/Victoria')
    time = datetime.now(home)
    current_time = time.strftime("%H:%M:%S")
    clock3.config(text=current_time)
    name3.config(text='Australia')

    home = pytz.timezone('Europe/London')
    time = datetime.now(home)
    current_time = time.strftime("%H:%M:%S")
    clock4.config(text=current_time)
    name4.config(text='UK')
    clock4.after(1,times)


#for tz in pytz.all_timezones: #(print all timezones):
#    print(tz)

name1 = Label(root, text="abc", font=("times",20,"bold"))
name1.place(x=10,y=10)
clock1 = Label(root, text="abc", font=("times",20,"bold"))
clock1.place(x=10,y=40)
nota1 = Label(root, text="Hours   Minutes   Seconds")
nota1.place(x=10,y=80)

name2 = Label(root, text="abc", font=("times",20,"bold"))
name2.place(x=300,y=10)
clock2 = Label(root, text="abc", font=("times",20,"bold"))
clock2.place(x=300,y=40)
nota2 = Label(root, text="Hours   Minutes   Seconds")
nota2.place(x=300,y=80)

name3 = Label(root, text="abc", font=("times",20,"bold"))
name3.place(x=10,y=150)
clock3 = Label(root, text="abc", font=("times",20,"bold"))
clock3.place(x=10,y=180)
nota3 = Label(root, text="Hours   Minutes   Seconds")
nota3.place(x=10,y=220)

name4 = Label(root, text="abc", font=("times",20,"bold"))
name4.place(x=300,y=150)
clock4 = Label(root, text="abc", font=("times",20,"bold"))
clock4.place(x=300,y=180)
nota4 = Label(root, text="Hours   Minutes   Seconds")
nota4.place(x=300,y=220)

times()
root.mainloop()
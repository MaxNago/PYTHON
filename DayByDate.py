from tkinter import*
import random
import datetime
from tkinter import messagebox
window = Tk()
window.title("Day")
window.minsize(50, 115)
window.maxsize(50, 115)
window.resizable(True, True)

totalValue=""
newTotalValue=""
codday=0
codmonth=0
codyear=0
day=0
month=0
year=0
tot=0
century=0
codcentury=0
curday = int(datetime.datetime.now().day)
curmonth = int(datetime.datetime.now().month)
curyear = int(datetime.datetime.now().year)
totcur=0
days=0
monthes=0
years=0
tots=0

entryDay =Entry(window, font = "TrebuchetMs 12", width = "7")
entryDay.grid(row=0, column=0)
entryMonth =Entry(window, font = "TrebuchetMs 12", width = "7")
entryMonth.grid(row=1, column=0)
entryYear =Entry(window, font = "TrebuchetMs 12", width = "7")
entryYear.grid(row=2, column=0)

def resultDay(day,month,year,century):
    day = int(entryDay.get())
    entryDay.delete(0, END)
    month = int(entryMonth.get())
    entryMonth.delete(0, END)
    century = int(str(entryYear.get())[:2])
    year = int(str(entryYear.get())[-2:])
    entryYear.delete(0, END)


    if month==1 or month == 10:
        codmonth=1
    elif month == 5:
        codmonth = 2
    elif month == 8:
        codmonth = 3
    elif month == 2 or month == 3 or month == 11:
        codmonth = 4
    elif month == 6:
        codmonth = 5
    elif month == 12 or month == 9:
        codmonth = 6
    elif month == 4 or month == 7:
        codmonth = 0



    if century==16:
        codcentury=6
    elif century==17:
        codcentury=4
    elif century == 18:
        codcentury = 2
    elif century == 19:
        codcentury = 0
    elif century == 20:
        codcentury = 6
    elif century == 21:
        codcentury = 4

    codyear = (codcentury + year + year // 4) % 7
    codday = (day + codmonth + codyear) % 7

    if codday == 0:
        messagebox.showinfo("День недли", "Суббота")
    elif codday == 1:
        messagebox.showinfo("День недли", "Воскресенье")
    elif codday == 2:
        messagebox.showinfo("День недли", "Понедельник")
    elif codday == 3:
        messagebox.showinfo("День недли", "Вторник")
    elif codday == 4:
        messagebox.showinfo("День недли", "Среда")
    elif codday == 5:
        messagebox.showinfo("День недли", "Четверг")
    elif codday == 6:
        messagebox.showinfo("День недли", "Пятница")

button15 =Button(window,text="WhichDay",bg ="green", font = "TrebuchetMs 12", width = "8", height="2", command = lambda:resultDay(day,month,year, century))
button15.grid(row=3, column=0)

window.mainloop()
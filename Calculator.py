from tkinter import*
import random
window = Tk()
window.title("CALC")
window.minsize(220, 250)
window.maxsize(220, 250)
window.resizable(True, True)

totalValue=""
randclr1 = "blue"
randclr2 = "red"
randclr3 = "pink"
colors = ["red", "blue", "green", "yellow", "pink", "grey", "darkmagenta", "peru"]

entry =Entry(window, font = "TrebuchetMs 12", width = "15")
entry.grid(row=0, column=0, columnspan="3")

def set_text(text,totalValue):
    totalValue=entry.get()
    entry.delete(0,END)
    totalValue+=text
    entry.insert(0, totalValue)

def clear():
    entry.delete(0,END)
    return

def plus(operand1,operand2):
    res=operand1+operand2
    entry.delete(0,END)
    entry.insert(0,res)

def umnoz(oper1,oper2):
    res=oper1*oper2
    entry.delete(0,END)
    entry.insert(0,res)

def delen(oper1,oper2):
    res=oper1/oper2
    entry.delete(0,END)
    entry.insert(0,res)

def minus(oper1,oper2):
    res=oper1-oper2
    entry.delete(0,END)
    entry.insert(0,res)

def info():
    window1 = Tk()
    window1.title("Info")
    window1.minsize(220, 250)
    window1.maxsize(220, 250)
    window1.resizable(False, False)

    def globalchange1():
        randclr1 = ""

        randclr1 = random.choice(colors)

        label1.config(text="Name -> Max", font="TrebuchetMs 17", fg=randclr1)

    def globalchange2():
        randclr2 = ""

        randclr2 = random.choice(colors)

        label2.config(text="Surname -> Nagornyi", font="TrebuchetMs 17", fg=randclr2)

    def globalchange3():
        randclr3 = ""

        randclr3 = random.choice(colors)

        label3.config(text="City -> Dnipro", font="TrebuchetMs 17", fg=randclr3)

    label1 = Label(window1)
    label1.config(text="Name -> Max", font="TrebuchetMs 17")
    label1.pack(padx=0, pady=10)

    label2 = Label(window1)
    label2.config(text="Surname -> Nagornyi", font="TrebuchetMs 17")
    label2.pack(padx=0, pady=10)

    label3 = Label(window1)
    label3.config(text="City -> Dnipro", font="TrebuchetMs 17")
    label3.pack(padx=0, pady=10)

    btnchange1 = Button(window1, text='Change color1', command=globalchange1)
    btnchange1.pack()

    btnchange2 = Button(window1, text='Change color2', command=globalchange2)
    btnchange2.pack()

    btnchange3 = Button(window1, text='Change color3', command=globalchange3)
    btnchange3.pack()

def result(totalValue):
    totalValue = entry.get()
    if("+" in totalValue):
        numberSumbol=totalValue.find("+")
        operand1=int(totalValue[0:numberSumbol])
        operand2 = int(totalValue[numberSumbol+1:totalValue.__len__()])
        plus(operand1, operand2)
    elif ("-" in totalValue):
        numberSumbol = totalValue.find("-")
        operand1 = int(totalValue[0:numberSumbol])
        operand2 = int(totalValue[numberSumbol + 1:totalValue.__len__()])
        minus(operand1, operand2)
    elif ("*" in totalValue):
        numberSumbol = totalValue.find("*")
        operand1 = int(totalValue[0:numberSumbol])
        operand2 = int(totalValue[numberSumbol + 1:totalValue.__len__()])
        umnoz(operand1, operand2)
    elif ("/" in totalValue):
        numberSumbol = totalValue.find("/")
        operand1 = int(totalValue[0:numberSumbol])
        operand2 = int(totalValue[numberSumbol + 1:totalValue.__len__()])
        delen(operand1, operand2)

button1 =Button(window,text="+",  bg ="peru",font = "TrebuchetMs 12", width = "5", height="2",command = lambda: set_text("+", totalValue) )
button1.grid(row=1, column=0)

button2 =Button(window,text="-",bg ="peru", font = "TrebuchetMs 12", width = "5", height="2",command = lambda: set_text("-", totalValue) )
button2.grid(row=2, column=0)

button3 =Button(window,text="*", bg ="peru", font = "TrebuchetMs 12", width = "5", height="2",command = lambda: set_text("*", totalValue) )
button3.grid(row=3, column=0)

button4 =Button(window,text="/",  bg ="peru",font = "TrebuchetMs 12", width = "5", height="2",command = lambda: set_text("/", totalValue) )
button4.grid(row=4, column=0)

button5 =Button(window,text="1", bg ="lightblue",font = "TrebuchetMs 12", width = "5", height="2", command = lambda: set_text("1", totalValue) )
button5.grid(row=1, column=1)

button6 =Button(window,text="4",bg ="lightblue", font = "TrebuchetMs 12", width = "5", height="2", command = lambda: set_text("4", totalValue) )
button6.grid(row=2, column=1)

button7 =Button(window,text="7",bg ="lightblue", font = "TrebuchetMs 12", width = "5", height="2", command = lambda: set_text("7", totalValue) )
button7.grid(row=3, column=1)

button8 =Button(window,text="0",bg ="lightblue",font = "TrebuchetMs 12", width = "5", height="2", command = lambda: set_text("0", totalValue) )
button8.grid(row=4, column=1)

button9 =Button(window,text="2", bg ="lightblue",font = "TrebuchetMs 12", width = "5", height="2", command = lambda: set_text("2", totalValue) )
button9.grid(row=1, column=2)

button10 =Button(window,text="5",bg ="lightblue", font = "TrebuchetMs 12", width = "5", height="2", command = lambda: set_text("5", totalValue) )
button10.grid(row=2, column=2)

button11 =Button(window,text="8", bg ="lightblue",font = "TrebuchetMs 12", width = "5", height="2", command = lambda: set_text("8", totalValue) )
button11.grid(row=3, column=2)

button12 =Button(window,text="CE",bg ="lightgreen", font = "TrebuchetMs 12", width = "5", height="2",command =  lambda: clear())
button12.grid(row=4, column=2)

button15 =Button(window,text="=",bg ="green", font = "TrebuchetMs 12", width = "5", height="2", command = lambda:result(totalValue))
button15.grid(row=4, column=3)

button13 =Button(window,text="3", bg ="lightblue",font = "TrebuchetMs 12", width = "5", height="2", command = lambda: set_text("3", totalValue) )
button13.grid(row=1, column=3)

button16 =Button(window,text="Info",  bg ="peru",font = "TrebuchetMs 12", width = "5", height="2", command = info)
button16.grid(row=0, column=3)

button14 =Button(window,text="6",bg ="lightblue", font = "TrebuchetMs 12", width = "5", height="2", command = lambda: set_text("6", totalValue) )
button14.grid(row=2, column=3)

button17 =Button(window,text="9", bg ="lightblue",font = "TrebuchetMs 12", width = "5", height="2", command = lambda: set_text("9", totalValue) )
button17.grid(row=3, column=3)

window.mainloop()
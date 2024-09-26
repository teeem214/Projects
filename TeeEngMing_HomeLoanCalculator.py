import tkinter
from tkinter import * 
from tkinter import scrolledtext 
from tkinter import ttk 
from tkinter.ttk import * 
from tkinter import messagebox 
from tkinter import filedialog 
from PIL import Image 
from time import * 
import time 
 
def results(): 
     
    global loanui,downpayui,error,intrateui,yearui,btresult,line1,line2,line3,line5,line6,period,month,intrate,balance,mintrate,mrepay,principle,totalprin,totalint,loan,downpay,intrate,year 
    error() 
    totalprin = 0.00 
    totalint = 0.00 
    loan = str(loanpy.get()) 
    downpay = str(downpaypy.get()) 
    intrate = str(intratepy.get()) 
    year = str(yearpy.get()) 
     
    loan = float(loan) 
    downpay = float(downpay) 
    intrate = float(intrate) 
    year = float(year) 
     
    balance = (loan-((loan*downpay)/100)) 
    mintrate = intrate/12/100 
    month = (year*12) 
    mrepay = (balance/((((1+mintrate)**month)-1)/(mintrate*(1+mintrate)**month))) 
     
    Label(window, text = format(mrepay, "0.2f"), background = "white").place(x = 221, y = 301) 
     
    line1 = ("======".rjust(3) + "=========".rjust(12) + "===============".rjust(17) + "=========".rjust(13)) 
    line2 = ("Period".rjust(3) + "Principle".rjust(12) + " Interest Rate ".rjust(17) + "Balance   ".rjust(15)) 
    line3 = ("======".rjust(3) + "=========".rjust(12) + "===============".rjust(17) + "=========".rjust(13)) 
     
    scroll.insert(INSERT, line1) 
    scroll.insert(INSERT, "\n" + line2) 
    scroll.insert(INSERT, "\n" + line3) 
     
    for period in range(int(month)): 
         
        intrate = balance*mintrate 
        principle = mrepay-intrate 
        balance = balance-principle 
         
        if balance<=0: 
            balance=0.00 
         
        line4 = (str(period + 1).rjust(4) + format(principle,"0.2f").rjust(12) + format(intrate, "0.2f").rjust(13) + format(balance, "0.2f").rjust(18)) 
     
        scroll.insert(INSERT, "\n" + line4) 
         
        totalprin = totalprin+principle 
        totalint = totalint+intrate 
 
    line5 = ("=====".rjust(3) + "=========".rjust(12) + "=========".rjust(13)) 
    line6 = ("Total".rjust(3) + format(totalprin, "0.2f").rjust(11) + format(totalint, "0.2f").rjust(13)) 
    line7 = ("=====".rjust(3) + "=========".rjust(12) + "=========".rjust(13)) 
     
    scroll.insert(INSERT, "\n" + line5) 
    scroll.insert(INSERT, "\n" + line6) 
    scroll.insert(INSERT, "\n" + line7) 
       
    loanui.configure(state = DISABLED) 
    downpayui.configure(state = DISABLED) 
    intrateui.configure(state = DISABLED) 
    yearui.configure(state = DISABLED) 
    btresult.configure(state = DISABLED) 
    btexport.configure(state = NORMAL) 
       
def resets(): 
     
    loanui.configure(state = NORMAL) 
    downpayui.configure(state = NORMAL) 
    intrateui.configure(state = NORMAL) 
    yearui.configure(state = NORMAL) 
    btresult.configure(state = NORMAL) 
    btexport.configure(state = DISABLED) 
     
    loanui.delete(0, END) 
    downpayui.delete(0, END) 
    intrateui.delete(0, END) 
    yearui.delete(0, END) 
    Label(window, text = "                          ", background = "white").place(x = 221, y = 301) 
    scroll.delete("0.0", END) 
 
def exports(): 
     
    filename = filedialog.asksaveasfilename() 
    files = open(filename,"w") 
    receipt = scroll.get("1.0",END) 
    files.write(receipt) 
    files.close() 
     
def error(): 
     
    loan = str(loanpy.get()) 
    try: 
        loan = float(loan) 
        if loan <= 0: 
            messagebox.showerror("Invalid Input!", "Your loan should not be negative or none value.") 
            loanpy.set(" ") 
    except ValueError: 
        messagebox.showerror("Invalid Input!", "Your loan should be numbers.") 
        loanpy.set(" ") 
         
    downpay = str(downpaypy.get()) 
    try: 
        downpay = float(downpay) 
        if downpay <= 0: 
            messagebox.showerror("Invalid Input!", "Your loan should not be negative or none value.") 
            downpaypy.set(" ") 
    except ValueError: 
        messagebox.showerror("Invalid Input!", "Your loan should be numbers.") 
        downpaypy.set(" ") 
     
    intrate = str(intratepy.get()) 
    try: 
        intrate = float(intrate) 
        if intrate <= 0: 
            messagebox.showerror("Invalid Input!", "Your loan should not be negative or none value.") 
            intratepy.set(" ") 
    except ValueError: 
        messagebox.showerror("Invalid Input!", "Your loan should be numbers.") 
        intratepy.set(" ") 
         
    year = str(yearpy.get()) 
    try: 
        year = float(year) 
        if year <= 0: 
            messagebox.showerror("Invalid Input!", "Your loan should not be negative or none value.") 
            yearpy.set(" ") 
    except ValueError: 
        messagebox.showerror("Invalid Input!", "Your loan should be numbers.") 
        yearpy.set(" ") 
         
def clocks(): 
     
    hour = time.strftime("%H") 
    minute = time.strftime("%M") 
    second = time.strftime("%S") 
    day = time.strftime("%A") 
    date = time.strftime("%d") 
    month = time.strftime("%b") 
    years = time.strftime("%Y") 
     
    lblTime.config(text = hour + ":" + minute + ":" + second + " " + day + "\n" + date + " " + month + " " + years, foreground = "white") 
    lblTime.after(1000, clocks) 
     
window = Tk() 
window.title("HOME LOAN CALCULATOR") 
window.iconbitmap("protection.ico") 
window.geometry("790x394") 
window.maxsize(790,394) 
window.minsize(790,394) 
 
bgbg = PhotoImage(file = "backgrounds.png") 
bgimage = Label(window, image = bgbg) 
bgimage.place(x = 0, y = 0) 
expbt = PhotoImage(file = "btnexp.png").subsample(5,5) 
resetbt = PhotoImage(file = "btnreset.png").subsample(5,5) 
resultbt = PhotoImage(file = "btnresult.png").subsample(5,5) 
 
lblTime = Label(window, text = " ", background = "grey") 
lblTime.place(x = 0, y = 0) 
clocks() 
 
loanpy = StringVar() 
downpaypy = StringVar() 
intratepy = StringVar() 
yearpy = StringVar() 
 
loanui = Entry(window, textvariable = loanpy, width = 13) 
loanui.place(x = 220, y = 192) 
 
downpayui = Entry(window, textvariable = downpaypy, width = 13) 
downpayui.place(x = 220, y = 219) 
 
intrateui = Entry(window, textvariable = intratepy, width = 13) 
intrateui.place(x = 220, y = 246) 
 
yearui = Entry(window, textvariable = yearpy, width = 13) 
yearui.place(x = 220, y = 273) 
 
btresult = Button(window, text = "Result", command = results, width = 8, image = resultbt) 
btresult.place(x = 229, y = 345) 
 
btreset = Button(window, text = "Reset", command = resets, width = 8, image = resetbt) 
btreset.place(x = 150, y = 345) 
 
btexport = Button(window, text = "Export", command = exports, width = 8, image = expbt) 
btexport.place(x = 680, y = 345) 
btexport.configure(state = DISABLED) 
 
scroll = scrolledtext.ScrolledText(window, wrap = WORD, width = 50, height = 18.5) 
scroll.configure(background = "#F2F3F4") 
scroll.config(cursor = "arrow") 
scroll.place(x = 335, y = 20) 
 
window.mainloop()
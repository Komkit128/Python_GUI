from tkinter import *
import tkinter as tk
import math
import parser
import tkinter.messagebox

root = Tk()
root.title("Scientfic Calculator")
root.configure(background = "powder blue")
root.resizable(width= False, height=False)
root.geometry("495x580+0+0")


calculator = Frame(root)
calculator.grid()

class Calculated():
     
     def __init__(self):
          self.total = ""

     def btnClick(self, number):
          self.total += str(number)
          self.display(self.total)

     def btnClearDisplay(self):
          self.total = ""
          self.display(self.total)
     
     def btnEqualsInput(self):
          sum = str(eval(self.total))
          self.display(sum)
          self.total = ""
     
     def display(self, value):
          txtDisplay.delete(0, END)
          txtDisplay.insert(0, value)

added_value = Calculated()

#========================Display Input================================# 
txtDisplay =   Entry(calculator, 
               font=('arial', 20, 'bold'),
               bg="powder blue",
               bd=30,
               width=29,
               justify=RIGHT)

txtDisplay.grid(row=0, column=0, columnspan=4, pady=1)
txtDisplay.insert(0, "0")

#=================Create Numberpad with forloop==========================#
numberpad = "789456123"
number = 0
btn = []
for j in range(2,5): # row 0 = Displayinput, 1 = ClearButton
     for k in range(3):
          btn.append(Button(calculator, width=6, height=2, font=('arial',20,'bold'), bd=4, text=numberpad[number] ))
          btn[number].grid(row = j, column = k, pady =2)
          #Input Number to display
          btn[number]["command"] = lambda x = numberpad [number] : added_value.btnClick(x) 
          number += 1
#====================== Standard Sign Math=====================================#

btnClear = Button(calculator,text=chr(67), width=6, height=2, font=('arial',20,'bold'), bd=4, bg="pink",
          command = added_value.btnClearDisplay()).grid(row = 1, column = 0, pady =2)

btnAllClear = Button(calculator,text=chr(67) + chr(69), width=6, height=2, font=('arial',20,'bold'), bd=4, bg="pink",
          command = added_value.btnClearDisplay()).grid(row = 1 , column = 1, pady =2)

btnSquareloot = Button(calculator,text="√", width=6, height=2, font=('arial',20,'bold'), bd=4, bg="pink")
btnSquareloot.grid(row = 1, column = 2, pady =2)

btnPlus = Button(calculator,text="+", width=6, height=2, font=('arial',20,'bold'), bd=4, bg="pink",
          command= lambda : added_value.btnClick("+")).grid(row = 1, column = 3, pady =2)

btnMinus = Button(calculator,text="-", width=6, height=2, font=('arial',20,'bold'), bd=4, bg="pink",
          command= lambda : added_value.btnClick("-")).grid(row = 2, column = 3, pady =2)

btnMultiple = Button(calculator,text="×", width=6, height=2, font=('arial',20,'bold'), bd=4, bg="pink",
          command= lambda : added_value.btnClick("×")).grid(row = 3, column = 3, pady =2)

btnDivision = Button(calculator,text="÷", width=6, height=2, font=('arial',20,'bold'), bd=4, bg="pink",
          command= lambda : added_value.btnClick("÷")).grid(row = 4, column = 3, pady =2)

btnZero = Button(calculator,text="0", width=6, height=2, font=('arial',20,'bold'), bd=4 ,
          command= lambda : added_value.btnClick("0")).grid(row = 5, column = 1, pady =2)

btnDot =  Button(calculator,text=".", width=6, height=2, font=('arial',20,'bold'), bd=4, bg="pink",
          command= lambda : added_value.btnClick(".")).grid(row = 5, column = 0, pady =2)

btnPM = Button(calculator,text=chr(177), width=6, height=2, font=('arial',20,'bold'), bd=4, bg="pink",
          command= added_value.btnClick(chr(177))).grid(row = 5, column = 2, pady =2)

btnEquals = Button(calculator,text="=", width=6, height=2, font=('arial',20,'bold'), bd=4, bg="red",
          command= added_value.btnEqualsInput()).grid(row = 5, column = 3, pady =2)

#====================== Scientific Sign Math =====================================#

#Row 1
btnPi = Button(calculator,text="π", width=6, height=2, font=('arial',20,'bold'), bd=4, bg="pink",
          command= added_value.btnClick("π")).grid(row = 1, column = 4, pady =2)

btnCos = Button(calculator,text="cos", width=6, height=2, font=('arial',20,'bold'), bd=4, bg="pink",
          command= added_value.btnClick("cos")).grid(row = 1, column = 5, pady =2)

btnTan = Button(calculator,text="tan", width=6, height=2, font=('arial',20,'bold'), bd=4, bg="pink",
          command= added_value.btnClick("tan")).grid(row = 1, column = 6, pady =2)

btnSin = Button(calculator,text="sin", width=6, height=2, font=('arial',20,'bold'), bd=4, bg="pink",
          command= added_value.btnClick("sin")).grid(row = 1, column = 7, pady =2)

"""
#Row 2
btn2Pi = Button(calculator,text="2π", width=6, height=2, font=('arial',20,'bold'), bd=4, bg="pink",
          command= added_value.2Pi()).grid(row = 2, column = 4, pady =2)


btnCosh = Button(calculator,text="cosh", width=6, height=2, font=('arial',20,'bold'), bd=4, bg="pink",
          command= added_value.cosh()).grid(row = 2, column = 4, pady =2)


btnTanh = Button(calculator,text="tanh", width=6, height=2, font=('arial',20,'bold'), bd=4, bg="pink",
          command= added_value.tanh()).grid(row = 2, column = 4, pady =2)


btnSinh = Button(calculator,text="sinh", width=6, height=2, font=('arial',20,'bold'), bd=4, bg="pink",
          command= added_value.sinh()).grid(row = 2, column = 4, pady =2)


#Row 3
btnlog = Button(calculator,text="log", width=6, height=2, font=('arial',20,'bold'), bd=4, bg="pink",
          command= added_value.log()).grid(row = 2, column = 4, pady =2)


btnExp = Button(calculator,text="Exp", width=6, height=2, font=('arial',20,'bold'), bd=4, bg="pink",
          command= added_value.exp()).grid(row = 2, column = 4, pady =2)


btnMod = Button(calculator,text="Mod", width=6, height=2, font=('arial',20,'bold'), bd=4, bg="pink",
          command= added_value.operation("mod")).grid(row = 2, column = 4, pady =2)


btnln = Button(calculator,text="ln", width=6, height=2, font=('arial',20,'bold'), bd=4, bg="pink",
          command= added_value.ln()).grid(row = 2, column = 4, pady =2)


#Row 4
btnlog2 = Button(calculator,text="log2", width=6, height=2, font=('arial',20,'bold'), bd=4, bg="pink",
          command= added_value.log()).grid(row = 2, column = 4, pady =2)


btnDeg = Button(calculator,text="Deg", width=6, height=2, font=('arial',20,'bold'), bd=4, bg="pink",
          command= added_value.Deg()).grid(row = 2, column = 4, pady =2)


btnacosh = Button(calculator,text="acosh", width=6, height=2, font=('arial',20,'bold'), bd=4, bg="pink",
          command= added_value.acosh()).grid(row = 2, column = 4, pady =2)


btnasinh = Button(calculator,text="asinh", width=6, height=2, font=('arial',20,'bold'), bd=4, bg="pink",
          command= added_value.asinh()).grid(row = 2, column = 4, pady =2)


#Row 5
btnlog10 = Button(calculator,text="log10", width=6, height=2, font=('arial',20,'bold'), bd=4, bg="pink",
          command= added_value.log10()).grid(row = 2, column = 4, pady =2)


btnlog1p = Button(calculator,text="log1p", width=6, height=2, font=('arial',20,'bold'), bd=4, bg="pink",
          command= added_value.log1p()).grid(row = 2, column = 4, pady =2)


btnexpm1 = Button(calculator,text="expm1", width=6, height=2, font=('arial',20,'bold'), bd=4, bg="pink",
          command= added_value.expm1().grid(row = 2, column = 4, pady =2)


btngamma = Button(calculator,text="gamma", width=6, height=2, font=('arial',20,'bold'), bd=4, bg="pink",
          command= added_value.gamma).grid(row = 2, column = 4, pady =2)


"""

#================================Menu and Function============================#

def iExit():
     iExit = tkinter.messagebox.askyesno("Scientific Calculator","Confrim if you want to close program?")
     if iExit > 0:
          root.destroy()
          return

def Scientific():
     root.resizable(width= False, height=False)
     root.geometry("944x568+0+0")

def Standard():
     root.resizable(width= False, height=False)
     root.geometry("490x580+0+0")

# Create Menu button
menubar = Menu(calculator)

#Menu name File Menu
filemenu = Menu(menubar, tearoff=0)
menubar.add_cascade(label = "File", menu= filemenu)
filemenu.add_command(label='Standard', command = Standard)
filemenu.add_command(label='Scientfic', command = Scientific)
filemenu.add_separator() 
filemenu.add_command(label='Exit', command = iExit)

#Menu Edit
editmenu = Menu(menubar, tearoff=0)
menubar.add_cascade(label = "Edit", menu= editmenu)
editmenu.add_command(label='Cut')
editmenu.add_command(label='Copy')
editmenu.add_separator() 
editmenu.add_command(label='Paste')

#Menu Help
helpmenu = Menu(menubar, tearoff=0)
menubar.add_cascade(label = "Help", menu= helpmenu)
helpmenu.add_command(label='View Help')
helpmenu.add_command(label='Tutorial')
helpmenu.add_separator() 
helpmenu.add_command(label='Paste')

#================================Menu====================================#



#Root 
root.configure(menu=menubar)
root.mainloop()


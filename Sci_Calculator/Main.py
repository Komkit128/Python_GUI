from tkinter import *
from sympy import *
import tkinter as tk
import math 
import parser
import tkinter.messagebox
import matplotlib.pyplot as plt

root = Tk()
#root.withdraw()
root.title("Scientfic Calculator")
root.configure(background = "powder blue")
root.resizable(width= False, height=False)
root.geometry("495x580+0+0")


calculator = Frame(root)
calculator.grid()

class Calculated():
     def __init__(self):
          self.total = 0
          self.current = ""
          self.op = ""
          self.input_value = True
          self.check_sum = False
          self.result = False

     def numberEnter(self,number):
          self.result = False
          first_number = txtDisplay.get()
          second_number = str(number)

          if self.input_value:
               self.current = second_number
               self.input_value = False
          else:
               if second_number == ".":
                    if second_number in first_number:
                         return
               self.current = first_number + second_number
          self.display(self.current)

     def sum_of_total(self):
          self.result = True
          self.current = float(self.current)
          if self.check_sum == True:
               print("Go To valid function")
               self.valid_funtion()
          else:
               print("Please choose the operation")
               self.total = float(txtDisplay.get())
     
     def valid_funtion(self):
          if self.op == "add": self.total += self.current
          if self.op == "sub": self.total -= self.current
          if self.op == "multiple": self.total *= self.current
          if self.op == "divide": self.total /= self.current
          if self.op == "mod": self.total %= self.current
          self.input_value = True
          self.check_sum = False
          self.display(self.total)

     def operation(self, op):
          self.current = float(self.current)
          if self.check_sum:
               self.valid_funtion()
          elif not self.result:
               self.total = self.current
               self.input_value = True
          #check_sum = True if having one operation
          self.check_sum = True
          self.op = op
          self.result = False
     
     def ClearEntry(self, value):
          print("Clear the number")
          self.result = False
          self.current = "0"
          self.display(self.current)
          self.input_value = True
          if value == "CE":
               self.total = 0

     def Advance_operation(self, value):
          self.result = False
          if txtDisplay.get() == "":
               pass
          else:
               if value == "sqrt" :     self.current = math.sqrt(float(txtDisplay.get()))
               if value == "pi" :       self.current = math.pi
               if value == "tau" :      self.current = math.tau
               if value == "E" :        self.current = math.e
               #Problem math.log(x[, base])
               if value == "log2":      self.current = math.log(float(txtDisplay.get()), 2)
               if value == "log10":     self.current = math.log(float(txtDisplay.get()), 10)
               if value == "radians" :  self.current = math.radians(float(txtDisplay.get()))

          self.display(self.current)
     
     def Trigonometry(self, value):
          self.result = False
          if txtDisplay.get() == "":
               pass
          else:
               if value == "sin" : self.current = math.sin(math.radians(float(txtDisplay.get())))
               if value == "cos" : self.current = math.cos(math.radians(float(txtDisplay.get())))
               if value == "tan" : self.current = math.tan(math.radians(float(txtDisplay.get())))
               if value == "sinh" : self.current = math.sinh(math.radians(float(txtDisplay.get())))
               if value == "cosh" : self.current = math.cosh(math.radians(float(txtDisplay.get())))
               if value == "tanh" : self.current = math.tanh(math.radians(float(txtDisplay.get())))
               if value == "asinh" : self.current = math.asinh(math.radians(float(txtDisplay.get())))
               if value == "acosh" : self.current = math.acosh(math.radians(float(txtDisplay.get())))

          self.display(self.current)
     
     def display(self, value):
          #value = value.strip("")
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
#txtDisplay.insert(0, "0")

#=================Create Numberpad with forloop==========================#
numberpad = "789456123"
number = 0
btn = []
for j in range(2,5): # row 0 = Displayinput, 1 = ClearButton
     for k in range(3):
          btn.append(Button(calculator, width=6, height=2, font=('arial',20,'bold'), bd=4, text=numberpad[number] ))
          btn[number].grid(row = j, column = k, pady =2)
          #Input Number to display
          btn[number]["command"] = lambda x = numberpad [number] : added_value.numberEnter(x) 
          number += 1
#====================== Standard Sign Math=====================================#

btnClear = Button(calculator,text=chr(67), width=6, height=2, font=('arial',20,'bold'), bd=4, bg="pink",
          command = lambda:added_value.ClearEntry("C")).grid(row = 1, column = 0, pady =2)

btnAllClear = Button(calculator,text=chr(67) + chr(69), width=6, height=2, font=('arial',20,'bold'), bd=4, bg="pink",
          command = lambda:added_value.ClearEntry("CE")).grid(row = 1 , column = 1, pady =2)

btnSquareloot = Button(calculator,text="√", width=6, height=2, font=('arial',20,'bold'), bd=4, bg="pink",
          command = lambda : added_value.Advance_operation("sqrt")).grid(row = 1, column = 2, pady =2)

btnPlus = Button(calculator,text="+", width=6, height=2, font=('arial',20,'bold'), bd=4, bg="pink",
          command= lambda : added_value.operation("add")).grid(row = 1, column = 3, pady =2)

btnMinus = Button(calculator,text="-", width=6, height=2, font=('arial',20,'bold'), bd=4, bg="pink",
          command= lambda : added_value.operation("sub")).grid(row = 2, column = 3, pady =2)

btnMultiple = Button(calculator,text="×", width=6, height=2, font=('arial',20,'bold'), bd=4, bg="pink",
          command= lambda : added_value.operation("multiple")).grid(row = 3, column = 3, pady =2)

btnDivision = Button(calculator,text="÷", width=6, height=2, font=('arial',20,'bold'), bd=4, bg="pink",
          command= lambda : added_value.operation("divide")).grid(row = 4, column = 3, pady =2)

btnZero = Button(calculator,text="0", width=6, height=2, font=('arial',20,'bold'), bd=4 ,
          command= lambda : added_value.numberEnter(0)).grid(row = 5, column = 1, pady =2)

btnDot =  Button(calculator,text=".", width=6, height=2, font=('arial',20,'bold'), bd=4, bg="pink",
          command= lambda : added_value.numberEnter(".")).grid(row = 5, column = 0, pady =2)

btnPM = Button(calculator,text=chr(177), width=6, height=2, font=('arial',20,'bold'), bd=4, bg="pink",
          command= lambda: added_value.Advance_operation("PM")).grid(row = 5, column = 2, pady =2)

btnEquals = Button(calculator,text="=", width=6, height=2, font=('arial',20,'bold'), bd=4, bg="red",
          command= added_value.sum_of_total).grid(row = 5, column = 3, pady =2)

#====================== Scientific Sign Math =====================================#

#Row 1
btnPi = Button(calculator,text="π", width=6, height=2, font=('arial',20,'bold'), bd=4, bg="pink",
          command= lambda:added_value.Advance_operation("pi")).grid(row = 1, column = 4, pady =2)

btnCos = Button(calculator,text="cos", width=6, height=2, font=('arial',20,'bold'), bd=4, bg="pink",
          command= lambda:added_value.Trigonometry("cos")).grid(row = 1, column = 5, pady =2)

btnTan = Button(calculator,text="tan", width=6, height=2, font=('arial',20,'bold'), bd=4, bg="pink",
          command= lambda:added_value.Trigonometry("tan")).grid(row = 1, column = 6, pady =2)

btnSin = Button(calculator,text="sin", width=6, height=2, font=('arial',20,'bold'), bd=4, bg="pink",
          command= lambda:added_value.Trigonometry("sin")).grid(row = 1, column = 7, pady =2)


#Row 2
btn2Pi = Button(calculator,text="2π", width=6, height=2, font=('arial',20,'bold'), bd=4, bg="pink",
          command= lambda:added_value.Trigonometry("")).grid(row = 2, column = 4, pady =2)


btnCosh = Button(calculator,text="cosh", width=6, height=2, font=('arial',20,'bold'), bd=4, bg="pink",
          command= lambda:added_value.Trigonometry("cosh")).grid(row = 2, column = 5, pady =2)


btnTanh = Button(calculator,text="tanh", width=6, height=2, font=('arial',20,'bold'), bd=4, bg="pink",
          command= lambda:added_value.Trigonometry("tanh")).grid(row = 2, column = 6, pady =2)


btnSinh = Button(calculator,text="sinh", width=6, height=2, font=('arial',20,'bold'), bd=4, bg="pink",
          command= lambda:added_value.Trigonometry("sinh")).grid(row = 2, column = 7, pady =2)


#Row 3
btnlog = Button(calculator,text="log10", width=6, height=2, font=('arial',20,'bold'), bd=4, bg="pink",
          command= lambda:added_value.Advance_operation("log10")).grid(row = 3, column = 4, pady =2)


btnExp = Button(calculator,text="exp", width=6, height=2, font=('arial',20,'bold'), bd=4, bg="pink",
          command= lambda:added_value.Advance_operation("exp")).grid(row = 3, column = 5, pady =2)


btnMod = Button(calculator,text="Mod", width=6, height=2, font=('arial',20,'bold'), bd=4, bg="pink",
          command= lambda:added_value.Advance_operation("mod")).grid(row = 3, column = 6, pady =2)


btnln = Button(calculator,text="ln", width=6, height=2, font=('arial',20,'bold'), bd=4, bg="pink",
          command= lambda:added_value.Advance_operation("ln")).grid(row = 3, column = 7, pady =2)


#Row 4
btnlog2 = Button(calculator,text="log2", width=6, height=2, font=('arial',20,'bold'), bd=4, bg="pink",
          command= added_value.Advance_operation("log2")).grid(row = 4, column = 4, pady =2)


btnRad = Button(calculator,text="radians", width=6, height=2, font=('arial',20,'bold'), bd=4, bg="pink",
          command= added_value.Advance_operation("radians")).grid(row = 4, column = 5, pady =2)


btnacosh = Button(calculator,text="acosh", width=6, height=2, font=('arial',20,'bold'), bd=4, bg="pink",
          command= added_value.Trigonometry("acosh")).grid(row = 4, column = 6, pady =2)


btnasinh = Button(calculator,text="asinh", width=6, height=2, font=('arial',20,'bold'), bd=4, bg="pink",
          command= added_value.Trigonometry("asinh")).grid(row = 4, column = 7, pady =2)


#Row 5
btnlog10 = Button(calculator,text="log10", width=6, height=2, font=('arial',20,'bold'), bd=4, bg="pink",
          command= added_value.Advance_operation("log10")).grid(row = 5, column = 4, pady =2)


btnlog1p = Button(calculator,text=(r'log$\frac{1}{P}'), width=6, height=2, font=('arial',20,'bold'), bd=4, bg="pink",
          command= added_value.Advance_operation("log1p")).grid(row = 5, column = 5, pady =2)


btnexpm1 = Button(calculator,text="expm1", width=6, height=2, font=('arial',20,'bold'), bd=4, bg="pink",
          command= added_value.Advance_operation("expm1")).grid(row = 5, column = 6, pady =2)


btngamma = Button(calculator,text="gamma", width=6, height=2, font=('arial',20,'bold'), bd=4, bg="pink",
          command= added_value.Advance_operation("gamma")).grid(row = 5, column = 7, pady =2)


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


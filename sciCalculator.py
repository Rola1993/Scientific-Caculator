# -*-coding: utf-8-*-
from tkinter import *
from tkinter import messagebox
import math


class sciCalculator:
    def __init__(self, master):
        master.title('My Calulator')
        master.geometry()
        self.e = Entry(master, bg='grey94', fg='blue4')
        self.e.grid(row=0, column=0, columnspan=6, pady=5)
        self.e.focus_set()  # Sets focus on the input text area
        self.value = 0
        self.curEquation = '0'
        self.e.insert(0, self.value)

        Button(master, text="=", width=10, command=lambda: self.equals()).grid(row=4, column=4, columnspan=2)
        Button(master, text='AC', width=3, command=lambda: self.allClear()).grid(row=1, column=4)
        Button(master, text='C', width=3, command=lambda: self.clear()).grid(row=1, column=5)
        Button(master, text="+", width=3, command=lambda: self.action('+')).grid(row=4, column=3)
        Button(master, text="x", width=3, command=lambda: self.action('x')).grid(row=2, column=3)
        Button(master, text="-", width=3, command=lambda: self.action('-')).grid(row=3, column=3)
        Button(master, text="÷", width=3, command=lambda: self.action('÷')).grid(row=1, column=3)
        Button(master, text="%", width=3, command=lambda: self.action('%')).grid(row=4, column=2)
        Button(master, text="7", width=3, command=lambda: self.action(7)).grid(row=1, column=0)
        Button(master, text="8", width=3, command=lambda: self.action(8)).grid(row=1, column=1)
        Button(master, text="9", width=3, command=lambda: self.action(9)).grid(row=1, column=2)
        Button(master, text="4", width=3, command=lambda: self.action(4)).grid(row=2, column=0)
        Button(master, text="5", width=3, command=lambda: self.action(5)).grid(row=2, column=1)
        Button(master, text="6", width=3, command=lambda: self.action(6)).grid(row=2, column=2)
        Button(master, text="1", width=3, command=lambda: self.action(1)).grid(row=3, column=0)
        Button(master, text="2", width=3, command=lambda: self.action(2)).grid(row=3, column=1)
        Button(master, text="3", width=3, command=lambda: self.action(3)).grid(row=3, column=2)
        Button(master, text="0", width=3, command=lambda: self.action(0)).grid(row=4, column=0)
        Button(master, text=".", width=3, command=lambda: self.action('.')).grid(row=4, column=1)
        Button(master, text="(", width=3, command=lambda: self.action('(')).grid(row=2, column=4)
        Button(master, text=")", width=3, command=lambda: self.action(')')).grid(row=2, column=5)
        Button(master, text="x²", width=3, command=lambda: self.powerFunc(2)).grid(row=3, column=5)
        Button(master, text="√", width=3, command=lambda: self.powerFunc(0.5)).grid(row=3, column=4)

    def convertOperator(self):

        input_equation = self.e.get()  # To fetch the current entry text
        self.curEquation = input_equation.replace('÷', '/')
        self.curEquation = self.curEquation.replace('x', '*')

    def equals(self):
        self.convertOperator()
        try:
            self.value = eval(self.curEquation)  # eval() interprets a string as code, which could be a security hole.
        except:
            self.e.delete(0, END)
            messagebox.showinfo("Alert", "Equation entered is invalid!")
        else:  # This would only run if no exception occurs. And an error here would NOT be caught.
            self.e.delete(0, END)
            self.e.insert(0, self.value)
        # finally: This would be printed in every case.

    def powerFunc(self, power):

        self.convertOperator()
        try:
            self.value = eval(self.curEquation)
        except:
            self.e.delete(0, END)
            messagebox.showinfo("Alert", "Equation entered is invalid!")
        else:
            self.sqval = math.pow(self.value, power)
            self.e.delete(0, END)
            self.e.insert(0, self.sqval)

    def allClear(self):
        self.e.delete(0, END)

    def clear(self):
        txt = self.e.get()[:-1]
        self.e.delete(0, END)
        self.e.insert(0, txt)

    def action(self, new_char):
        self.e.insert(END, new_char)


# Main
if __name__ == '__main__':
    root = Tk()
    app = sciCalculator(root)
    root.mainloop()

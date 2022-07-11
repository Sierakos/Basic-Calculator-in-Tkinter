# Calculator in tkinter #

from tkinter import *
from tkinter import ttk

class Calculator():

    def __init__(self, root):
        root.title('Calculator')
        root.geometry('400x300')

        self.value = StringVar()

        self.val = ""
        self.val_1 = ""

        self.mainframe = ttk.Frame(root, padding=15)
        self.mainframe.grid(column=0,row=0, sticky=N)
        root.rowconfigure(0, weight=1)
        root.columnconfigure(0, weight=1)

        # s = ttk.Style()
        # s.configure('bg-blue.TFrame', background='blue')
        self.entry_frame = ttk.Frame(self.mainframe, padding=10)
        self.entry_frame.grid(row=0, column=0, sticky=N)

        self.buttons_frame = ttk.Frame(self.mainframe, padding=10)
        self.buttons_frame.grid(row=1, column=0, sticky=N)

        self.createEntry()
        self.createButtons()

        ### mainloop ###
        root.mainloop()


    def createEntry(self):
        self.calc_entry = ttk.Entry(self.entry_frame, width=25, font='Times 15', textvariable=self.value, state=DISABLED)
        self.calc_entry.grid(column=0, row=0)

    def createButtons(self):
        self.numbers = [0,1,2,3,4,5,6,7,8,9]
        

        ttk.Button(self.buttons_frame, text=self.numbers[1], command=lambda : self.press(1)).grid(column=0, row=0)
        ttk.Button(self.buttons_frame, text=self.numbers[2], command=lambda : self.press(2)).grid(column=1, row=0)
        ttk.Button(self.buttons_frame, text=self.numbers[3], command=lambda : self.press(3)).grid(column=2, row=0)
        ttk.Button(self.buttons_frame, text=self.numbers[4], command=lambda : self.press(4)).grid(column=0, row=1)
        ttk.Button(self.buttons_frame, text=self.numbers[5], command=lambda : self.press(5)).grid(column=1, row=1)
        ttk.Button(self.buttons_frame, text=self.numbers[6], command=lambda : self.press(6)).grid(column=2, row=1)
        ttk.Button(self.buttons_frame, text=self.numbers[7], command=lambda : self.press(7)).grid(column=0, row=2)
        ttk.Button(self.buttons_frame, text=self.numbers[8], command=lambda : self.press(8)).grid(column=1, row=2)
        ttk.Button(self.buttons_frame, text=self.numbers[9], command=lambda : self.press(9)).grid(column=2, row=2)

        ttk.Button(self.buttons_frame, text='/', command=lambda : self.mathSymbolPress("/")).grid(column=3, row=0)
        ttk.Button(self.buttons_frame, text='*', command=lambda : self.mathSymbolPress("*")).grid(column=3, row=1)
        ttk.Button(self.buttons_frame, text='-', command=lambda : self.mathSymbolPress("-")).grid(column=3, row=2)
        ttk.Button(self.buttons_frame, text='+', command=lambda : self.mathSymbolPress("+")).grid(column=3, row=3)

        ttk.Button(self.buttons_frame, text=",", command=self.addComa).grid(column=0, row=3)
        ttk.Button(self.buttons_frame, text=self.numbers[0], command=lambda : self.press(0)).grid(column=1, row=3)
        ttk.Button(self.buttons_frame, text="=", command=self.equ).grid(column=2, row=3)

    def press(self, num):
        self.val += str(self.numbers[num])
        self.value.set(self.val)

    def addComa(self):
        self.val += "."
        self.value.set(self.val)

    def mathSymbolPress(self, symbol):
        self.val_1 = self.val
        self.val = ""
        self.m_sym = symbol

    def equ(self):
        if self.m_sym == "+":
            res = float(self.val_1) + float(self.val)
            self.value.set(res)
            self.val = res
        if self.m_sym == "-":
            res = float(self.val_1) - float(self.val)
            self.value.set(res)
            self.val = res
        if self.m_sym == "*":
            res = float(self.val_1) * float(self.val)
            self.value.set(res)
            self.val = res
        if self.m_sym == "/":
            res = float(self.val_1) / float(self.val)
            self.value.set(res)
            self.val = res

        self.val_1 = ""

root = Tk()
Calculator(root)
root.mainloop()


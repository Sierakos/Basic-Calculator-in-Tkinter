import tkinter as tk

LARGE_FONT = ("Verdana", 12)

BACKGROUND_COLOR = "#DDDDDD"
BUTTONS_FONT = ("Arial", 30)
LABEL_FONT = ("Arial", 25)
TOTAL_LABEL_FONT = ("Arial", 10)

class SciencePage(tk.Frame):
    def __init__(self, parent, controller):
        tk.Frame.__init__(self, parent)

        self.value = ""
        self.total_value = ""

        self.digits = {
            1:(1,0), 2:(1,1), 3:(1,2),
            4:(2,0), 5:(2,1), 6:(2,2),
            7:(3,0), 8:(3,1), 9:(3,2),
            ".":(4,0), 0:(4,1)
        }

        # self.symbols = ['/', '*', '-', '+']
        self.symbols = {
            1: ['/', '*', '-', '+'],
            2: ['\u221Ax' ,'\u221Bx', 'x\u00B2', 'x\u00B3'],
            3: ['(', ')', 'x!', '10\u207F']
        }

        self.window_frame = self.create_window_frame()
        self.window_frame.columnconfigure(0, weight=1)
        
        self.buttons_frame = self.create_buttons_frame()

        for i in range(0,5):
            self.buttons_frame.rowconfigure(i, weight=1)
            self.buttons_frame.columnconfigure(i, weight=1)

        # self.buttons_frame.rowconfigure(5, weight=1)
        
        self.window_label, self.window_total_label = self.create_window_labels()
        self.create_buttons()
        self.create_math_buttons()
        self.create_equals_button()
        self.create_clear_button()

    def create_window_frame(self):
        frame = tk.Frame(self, height="150")
        # frame.grid(row=0, column=0, sticky=tk.NSEW)
        frame.pack(expand=True, fill="both")
        return frame

    def create_buttons_frame(self):
        frame = tk.Frame(self)
        # frame.grid(row=1, column=0, sticky=tk.NSEW)
        frame.pack(side="top", expand=True, fill="both")
        return frame

    def create_window_labels(self):
        label = tk.Label(self.window_frame, text=self.value, font=LABEL_FONT)
        label.grid(row=1,column=0, padx=20, pady=20, sticky=tk.E)

        total_label = tk.Label(self.window_frame, text=self.total_value, font=TOTAL_LABEL_FONT)
        total_label.grid(row=0,column=0,sticky=tk.E)
        return label, total_label

    def create_buttons(self):
        for digit, places in self.digits.items():
            tk.Button(self.buttons_frame, text=digit, font=BUTTONS_FONT, command=lambda digit=digit: self.push_digit(digit)).grid(row=places[0], column=places[1], sticky=tk.NSEW)

    def create_math_buttons(self):
        i = 1
        for symbol in self.symbols[1]:
            tk.Button(self.buttons_frame, text=symbol, font=BUTTONS_FONT, command=lambda symbol=symbol: self.push_math_buttons(symbol)).grid(row=i, column=3, sticky=tk.NSEW)
            i += 1

        i = 1
        for symbol in self.symbols[2]:
            tk.Button(self.buttons_frame, text=symbol, font=BUTTONS_FONT, command=lambda symbol=symbol: self.sqrt_or_square(symbol)).grid(row=i, column=4, sticky=tk.NSEW)
            i += 1

        i = 1
        for symbol in self.symbols[3]:
            tk.Button(self.buttons_frame, text=symbol, font=BUTTONS_FONT, command=lambda symbol=symbol: self.push_math_buttons_3(symbol)).grid(row=5, column=i, sticky=tk.NSEW)
            i += 1

    def sqrt_of_2(self):
        self.value = str(eval(self.value)**0.5)
        self.update_value()

    def sqrt_of_3(self):
        val = 1.000000000000/3.000000000000
        self.value = str(round(eval(self.value)**(val), 10))
        self.update_value()
    
    def pow_of_2(self):
        self.value = str(eval(self.value)**2)
        self.update_value()

    def pow_of_3(self):
        self.value = str(eval(self.value)**3)
        self.update_value()

    def sqrt_or_square(self, symbol):
        if symbol == "\u221Ax":
            self.sqrt_of_2()
        elif symbol == "\u221Bx":
            self.sqrt_of_3()
        elif symbol == "x\u00B2":
            self.pow_of_2()
        elif symbol == "x\u00B3":
            self.pow_of_3()

    def push_math_buttons_3(self, symbol):
        if symbol == "(" or symbol == ")":
            self.value += symbol
            self.total_value += self.value
            self.value = ""
            self.update_total_value()
            self.update_value()
        elif symbol == "x!":
            x = int(self.value)
            val = 1
            for i in range(x):
                val = val * (i+1)
            self.value = str(val)
            self.update_value()
        elif symbol == "10\u207F":
            x = int(self.value)
            val = 10**x
            self.value = str(val)
            self.update_value()

    def create_equals_button(self):
        tk.Button(self.buttons_frame, text="=", font=BUTTONS_FONT, command=self.push_equal_buttons).grid(row=4, column=2, sticky=tk.NSEW)

    def create_clear_button(self):
        tk.Button(self.buttons_frame, text="Clear", font=BUTTONS_FONT, command=self.clear).grid(row=0, column=0, columnspan=5, sticky=tk.NSEW)

    def clear(self):
        self.value = ""
        self.total_value = ""
        self.update_value()
        self.update_total_value()

    def push_digit(self, digit):
        if "." in self.value and digit == ".":
            pass
        else:
            self.value += str(digit)
        self.update_value()

    def push_math_buttons(self, symbol):
        self.value += symbol
        if (self.total_value == "" or self.total_value != "" and self.value not in self.symbols[1]):
            self.total_value += self.value
        # elif self.total_value[-1] in self.symbols:
        else:
            new = self.total_value.replace(self.total_value[-1], symbol)
            self.total_value = new
        self.value = ""
        self.update_value()
        self.update_total_value()

    def push_equal_buttons(self):
        self.total_value += self.value
        try:
            self.value = str(eval(self.total_value))
            self.total_value = ""
        except Exception:
            self.value = "Error"
        finally:
            self.update_value()

        self.update_value()
        self.update_total_value()

    def update_value(self):
        self.window_label.config(text=self.value[:10])

    def update_total_value(self):
        self.window_total_label.config(text=self.total_value[:10])
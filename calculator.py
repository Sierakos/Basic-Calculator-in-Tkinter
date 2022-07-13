import tkinter as tk

LARGE_FONT = ("Verdana", 12)

BACKGROUND_COLOR = "#DDDDDD"
BUTTONS_FONT = ("Arial", 30)
LABEL_FONT = ("Arial", 25)
TOTAL_LABEL_FONT = ("Arial", 10)

class Calculator(tk.Tk):
    def __init__(self, *args, **kwargs):
        tk.Tk.__init__(self, *args, **kwargs)

        container = tk.Frame(self)
        container.pack(side="top", fill="both", expand = True)

        container.grid_rowconfigure(0, weight=1)
        container.grid_columnconfigure(0, weight=1)

        self.create_menubar()

        self.frames = {}

        frame = StandardPage(container, self)
        frame_2 = SciencePage(container, self)

        self.frames[StandardPage] = frame
        self.frames[SciencePage] = frame_2

        # print(str(self.frames[SciencePage]))
        # print("frames : " + str(self.frames))

        frame.grid(row=0, column=0, sticky="nsew")
        frame_2.grid(row=0, column=0, sticky="nsew")

        self.show_frame(StandardPage)

    def show_frame(self, cont):
        frame = self.frames[cont]
        frame.tkraise()

    def create_menubar(self):
        menubar = tk.Menu(self)
        viewmenu = tk.Menu(menubar, tearoff=0)
        viewmenu.add_command(label="Standard", command = lambda x=StandardPage: self.show_frame(x))
        viewmenu.add_command(label="Science", command = lambda x=SciencePage: self.show_frame(x))
        viewmenu.add_command(label="Programistic", command="")

        menubar.add_cascade(label="View", menu=viewmenu)
        self.config(menu=menubar)

class StandardPage(tk.Frame):
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

        self.symbols = ['/', '*', '-', '+']

        self.window_frame = self.create_window_frame()
        self.window_frame.columnconfigure(0, weight=1)
        
        self.buttons_frame = self.create_buttons_frame()
        for i in range(0,4):
            self.buttons_frame.rowconfigure(i, weight=1)
            self.buttons_frame.columnconfigure(i, weight=1)

        self.buttons_frame.rowconfigure(4, weight=1)
        
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
        for symbol in self.symbols:
            tk.Button(self.buttons_frame, text=symbol, font=BUTTONS_FONT, command=lambda symbol=symbol: self.push_math_buttons(symbol)).grid(row=i, column=3, sticky=tk.NSEW)
            i += 1

    def create_equals_button(self):
        tk.Button(self.buttons_frame, text="=", font=BUTTONS_FONT, command=self.push_equal_buttons).grid(row=4, column=2, sticky=tk.NSEW)

    def create_clear_button(self):
        tk.Button(self.buttons_frame, text="Clear", font=BUTTONS_FONT, command=self.clear).grid(row=0, column=0, columnspan=4, sticky=tk.NSEW)

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
        if self.total_value == "":
            self.total_value += self.value
        else:
            if self.total_value[-1] in self.symbols:
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
            2: ['\u221Ax' ,'\u221Bx', 'x\u00B2', 'x\u00B3']
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
        if self.total_value == "":
            self.total_value += self.value
        else:
            if self.total_value[-1] in self.symbols[1]:
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

app = Calculator()
app.title("Calculator")
app.geometry("400x600")
app.resizable(0,0)
app.mainloop()
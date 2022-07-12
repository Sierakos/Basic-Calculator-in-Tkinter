# Calculator in tkinter #
from tkinter import *

BACKGROUND_COLOR = "#DDDDDD"
BUTTONS_FONT = ("Arial", 30)
LABEL_FONT = ("Arial", 25)
TOTAL_LABEL_FONT = ("Arial", 10)

class Calculator():
    def __init__(self):
        self.root = Tk()
        self.root.resizable(0,0)
        self.root.title("Calculator")

        self.value = ""
        self.total_value = ""

        self.digits = {
            1:(1,0), 2:(1,1), 3:(1,2),
            4:(2,0), 5:(2,1), 6:(2,2),
            7:(3,0), 8:(3,1), 9:(3,2),
            ".":(4,0), 0:(4,1)
        }

        self.symbols = ['/', '*', '-', '+']

        self.container_frame = self.create_container_frame()

        self.window_frame = self.create_window_frame()
        self.window_frame.columnconfigure(0, weight=1)
        
        self.buttons_frame = self.create_buttons_frame()
        
        self.window_label, self.window_total_label = self.create_window_labels()
        self.create_buttons()
        self.create_math_buttons()
        self.create_equals_button()
        self.create_clear_button()

    def run(self):
        self.root.mainloop()

    def create_container_frame(self):
        frame = Frame(self.root, bg=BACKGROUND_COLOR)
        frame.grid(row=0, column=0, sticky=NSEW)
        frame.columnconfigure(1, weight=1)
        frame.rowconfigure(1, weight=1)
        return frame

    def create_window_frame(self):
        frame = Frame(self.container_frame)
        frame.grid(row=0, column=0, sticky=NSEW)
        return frame

    def create_buttons_frame(self):
        frame = Frame(self.container_frame)
        frame.grid(row=1, column=0, sticky=NSEW)
        return frame

    def create_window_labels(self):
        label = Label(self.window_frame, text=self.value, font=LABEL_FONT)
        label.grid(row=1,column=0, padx=20, pady=20, sticky=E)

        total_label = Label(self.window_frame, text=self.total_value, font=TOTAL_LABEL_FONT)
        total_label.grid(row=0,column=0,sticky=E)
        return label, total_label

    def create_buttons(self):
        for digit, places in self.digits.items():
            Button(self.buttons_frame, text=digit, font=BUTTONS_FONT, command=lambda digit=digit: self.push_digit(digit)).grid(row=places[0], column=places[1], sticky=NSEW)

    def create_math_buttons(self):
        i = 1
        for symbol in self.symbols:
            Button(self.buttons_frame, text=symbol, font=BUTTONS_FONT, command=lambda symbol=symbol: self.push_math_buttons(symbol)).grid(row=i, column=3, sticky=NSEW)
            i += 1

    def create_equals_button(self):
        Button(self.buttons_frame, text="=", font=BUTTONS_FONT, command=self.push_equal_buttons).grid(row=4, column=2, sticky=NSEW)

    def create_clear_button(self):
        Button(self.buttons_frame, text="Clear", font=BUTTONS_FONT, command=self.clear).grid(row=0, column=0, columnspan=4, sticky=NSEW)

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

if __name__ == "__main__":
    calc = Calculator()
    calc.run()



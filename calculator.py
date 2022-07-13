from programmers_page import ProgrammersPage
from standard_page import StandardPage
from science_page import SciencePage

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
        frame_3 = ProgrammersPage(container, self)

        self.frames[StandardPage] = frame
        self.frames[SciencePage] = frame_2
        self.frames[ProgrammersPage] = frame_3

        frame.grid(row=0, column=0, sticky="nsew")
        frame_2.grid(row=0, column=0, sticky="nsew")
        frame_3.grid(row=0, column=0, sticky="nsew")

        self.show_frame(StandardPage)

    def show_frame(self, cont):
        frame = self.frames[cont]
        frame.tkraise()

    def create_menubar(self):
        menubar = tk.Menu(self)
        viewmenu = tk.Menu(menubar, tearoff=0)
        viewmenu.add_command(label="Standard", command = lambda x=StandardPage: self.show_frame(x))
        viewmenu.add_command(label="Science", command = lambda x=SciencePage: self.show_frame(x))
        viewmenu.add_command(label="Programmers", command= lambda x=ProgrammersPage: self.show_frame(x))

        menubar.add_cascade(label="View", menu=viewmenu)
        self.config(menu=menubar)

class App():
    def __init__(self, *args, **kwargs):
        self.app = Calculator()
        self.app.title("Calculator")
        self.app.geometry("400x600")
        self.app.resizable(0,0)

    def run(self):
        self.app.mainloop()

if __name__ == "__main__":
    app = App()
    app.run()
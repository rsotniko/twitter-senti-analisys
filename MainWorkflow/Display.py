import tkinter as tk
from Tkinter import Tk, BOTH
from ttk import Frame, Button, Style


class Display(tk.Frame):
    def __init__(self, parent):
        tk.Frame.__init__(self, parent)
        self.style = Style()
        self.parent = parent
        self.initUI()

    def initUI(self):
        self.parent.title("Quit button")
        self.style.theme_use("default")

        self.pack(fill=BOTH, expand=1)

        quitButton = Button(self, text="Quit", command=self.quit)
        quitButton.place(x=1, y=1)

    def centerWindow(self):
        w = 700
        h = 450

        sw = self.parent.winfo_screenwidth()
        sh = self.parent.winfo_screenheight()

        x = (sw - w) / 2
        y = (sh - h) / 2
        self.parent.geometry('%dx%d+%d+%d' % (w, h, x, y))


def main():
    root = Tk()
    app = Display(root)
    app.centerWindow()
    root.mainloop()


if __name__ == '__main__':
    main()

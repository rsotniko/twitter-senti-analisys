# import tkinter as tk
#
#
# class Display(tk.Frame):
#     def __init__(self, root):
#         super().__init__(root)
#         self.add_img = tk.PhotoImage(
#             file='/Users/dimadolgosheev/PycharmProjects/twitter-senti-analisys/play.gif')  # Указать свой путь к файлу
#         self.init_main()
#
#     def init_main(self):
#         tool_bar = tk.Frame(bd=2)
#         tool_bar.pack(side=tk.TOP, fill=tk.X)
#         btn = tk.Button(tool_bar, text="Analyze", command=self.click_button, bg='#d7d8e0', compound=tk.TOP, bd=0,
#                         image=self.add_img)
#         btn.pack(side=tk.LEFT)
#
#     def show_message():
#         tk.messagebox.showinfo("GUI Python", tk.message.get())
#
#     def click_button(self):
#         Child()
#
#
# class Child(tk.Toplevel):
#     def __init__(self):
#         super().__init__(root)
#         self.init_child()
#
#     def init_child(self):
#         self.title("Result")  # Кнопка для запуска и вывода результата
#         w = 700
#         h = 450
#         sw = root.winfo_screenwidth()
#         sh = root.winfo_screenheight()
#         x = (sw - w) / 2
#         y = (sh - h) / 2
#         self.geometry('%dx%d+%d+%d' % (w, h, x, y))
#         self.resizable(False, False)
#         self.grab_set()
#         self.focus_set()
#
#
# if __name__ == '__main__':
#     root = tk.Tk()
#     root.title("GUI")
#     w = 700
#     h = 450
#     sw = root.winfo_screenwidth()
#     sh = root.winfo_screenheight()
#     x = (sw - w) / 2
#     y = (sh - h) / 2
#     root.geometry('%dx%d+%d+%d' % (w, h, x, y))
#     root.resizable(False, False)
#     app = Display(root)
#     app.pack()
#     root.mainloop()
from tkinter import *
from tkinter import messagebox


def clear():
    hashtag_entry.delete(0, END)
    num_entry.delete(0, END)


# Для теста
def display():
    messagebox.showinfo("Result", "Ваш хештег: " + hashtag_entry.get() + "\nКолличество сообщений: " + num_entry.get())


root = Tk()
root.title("RNN")
w = 350
h = 150
sw = root.winfo_screenwidth()
sh = root.winfo_screenheight()
x = (sw - w) / 2
y = (sh - h) / 2
root.geometry('%dx%d+%d+%d' % (w, h, x, y))
root.resizable(False, False)

hashtag_label = Label(text="#")
num_label = Label(text="Number of messages")

hashtag_label.grid(row=0, column=0, sticky="w")
num_label.grid(row=1, column=0, sticky="w")

hashtag_entry = Entry()
num_entry = Entry()

hashtag_entry.grid(row=0, column=1, padx=5, pady=5)
num_entry.grid(row=1, column=1, padx=5, pady=5)

# вставка начальных данных
hashtag_entry.insert(0, "RNN")
num_entry.insert(0, "10000")

run_button = Button(text="Run", command=display)
clear_button = Button(text="Clear", command=clear)

run_button.grid(row=2, column=0, padx=5, pady=5, sticky="e")
clear_button.grid(row=2, column=1, padx=5, pady=5, sticky="e")

root.mainloop()

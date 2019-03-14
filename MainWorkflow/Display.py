from tkinter import *
from tkinter import messagebox
from tkinter import scrolledtext


def clear():
    hashtag_entry.delete(0, END)
    num_entry.delete(0, END)


def retFalse():
    handle = open("result.txt", "r")
    _str = handle.read().replace(";", " ").replace("\n", " ")
    handle.close()
    lst = []
    lst = _str.split(" ")
    _cf = 0;
    for r in lst:
        if r == "false":
            _cf = _cf + 1
    return _cf


def retTrue():
    handle = open("result.txt", "r")
    _str = handle.read().replace(";", " ").replace("\n", " ")
    handle.close()
    lst = []
    lst = _str.split(" ")
    _ct = 0;
    for r in lst:
        if r == "true":
            _ct = _ct + 1
    return _ct


def GetMark(_ct, _cf):
    if _ct < _cf:
        return "\nОтрицательных коментариев больше "
    if _cf < _ct:
        return "\nОтрицательных коментариев меньше "
    if _cf == _ct:
        return "\nОтрицательных и положительных коментариев поровну "


def display():
    # Тут будет вызов функции для анализа файла
    # Отпарсим результат в нужный нам формат
    # Записываем в файл result txt - результат, отображаем
    messagebox.showinfo("INFO", "Data is loading, please wait")
    window = Tk()
    window.title("Result")
    w = 300
    h = 600
    sw = window.winfo_screenwidth()
    sh = window.winfo_screenheight()
    x = (sw - w) / 2
    y = (sh - h) / 2
    window.geometry('%dx%d+%d+%d' % (w, h-30, x, y))
    window.resizable(False, False)
    _ct = retTrue()
    _cf = retFalse()
    handle = open("result.txt", "r")
    _maintxt = handle.read().replace(";", " ")
    _res = _maintxt + "\n\nКол-во положительных отзывов = " + _ct.__str__() + "\nКол-во отрицательных отзывов = " + _cf.__str__() + GetMark(_ct, _cf)
    txt = scrolledtext.ScrolledText(window, width=40, height=35)
    txt.grid(column=0, row=0)
    txt.insert(INSERT, _res)
    save_button = Button(window, text="Save", command=save)
    # save_button.grid(row=2, column=2, padx=5, pady=5, sticky="e")
    save_button.grid(row=1, column=0, padx=5, pady=5, sticky="e")
    window.mainloop()


def save():
    handle = open("output.txt", "w")
    res = open("result.txt", "r")
    _res = res.read()
    _ct = retTrue()
    _cf = retFalse()
    handle.write(_res + "\n\nКол-во положительных отзывов = " + _ct.__str__() + "\nКол-во отрицательных отзывов = " + _cf.__str__() + GetMark(_ct, _cf) )
    handle.close()
    messagebox.showinfo("INFO", "Результат сохранен в output.txt")


root = Tk()
root.title("RNN")
w = 400
h = 130
sw = root.winfo_screenwidth()
sh = root.winfo_screenheight()
x = (sw - w) / 2
y = (sh - h) / 2
root.geometry('%dx%d+%d+%d' % (w-70, h, x, y))
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

run_button.grid(row=2, column=1, padx=5, pady=5, sticky="e")
clear_button.grid(row=2, column=0, padx=5, pady=5, sticky="e")

root.mainloop()

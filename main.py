import threading
import time
import pyautogui

import tkinter as tk

from tkinter import messagebox
from tkinter import *
from tkinter import ttk

root = Tk()
root.title("Кликер")
root.geometry("300x240+670+300")
# root.minsize(300,220)
# root.maxsize(300,220)

root.resizable(False, False)

icon = PhotoImage(file = "icon.png")
root.iconphoto(False, icon)

# ttk.Style().configure(".",  font="helvetica 13", foreground="#004D40", padding=8, background="#B2DFDB")

time_click = 1.0
number_of_clicks = 0

def clik():
    threading.Thread(target=main2).start()

def main2():
    label3.config(text="3",font=("Arial", 14))
    time.sleep(1)
    label3.config(text="2",font=("Arial", 14))
    time.sleep(1)
    label3.config(text="1",font=("Arial", 14))
    time.sleep(1)
    label3.config(text="Програма \n Работает")
    time.sleep(1)
    while_number = 0
    while while_number != number_of_clicks:
        while_number+=1
        time.sleep(time_click)
        print(while_number)
        pyautogui.click()
    label3.config(text="Програма \n Завершила")
    time.sleep(1)

def get():
    global number_of_clicks
    number_of_clicks = int(entry.get())
    print(number_of_clicks)

def dismiss(window):
    window.grab_release()
    window.destroy()
def edit_click():
    newWindow = tk.Toplevel(root)
    newWindow.geometry("300x220")
    newWindow.title("Руководство")
    labelExample = tk.Label(newWindow, text = "Ведите количество кликов,\n И выберете периодичность.\n Нажмите запуск.")
    labelExample.pack()
    close_button = ttk.Button(newWindow, text="Закрыть окно", command=lambda: dismiss(newWindow))
    close_button.pack(anchor="s", expand=1)
    newWindow.grab_set()

def c_c1():
    global time_click
    time_click = 1.0
    print(time_click)
def c_c2():
    global time_click
    time_click = 0.6
    print(time_click)
def c_c3():
    global time_click
    time_click = 0.3
    print(time_click)


label = Label(text="Настройки")
label.pack(padx=[5, 236])

label1 = Label(text="Количество кликов")
label1.pack(padx=[5,188])

label2 = Label(text="Периодичность кликов")
label2.place(x=2, y=59, width=136, height=25)

label3 = Label(text="")
label3.place(x=109, y=142, width=100, height=42)


btn1 = ttk.Button(text="1(с)", command=c_c1)
btn1.place(x=5, y=84, width=80, height=25)

btn2 = ttk.Button(text="0.6(с)", command=c_c2)
btn2.place(x=109, y=84, width=80, height=25)

btn2 = ttk.Button(text="0.3(с)", command=c_c3)
btn2.place(x=215, y=84, width=80, height=25)

btn3 = ttk.Button(text="Сохранить", command=get)
btn3.place(x=5, y=154, width=90, height=35)

btn4 = ttk.Button(text="Запуск",command=clik)
btn4.place(x=5, y=190, width=290, height=25)


entry = ttk.Entry()
entry.place(x=6, y=41, width=80, height=18)


main_menu = Menu()
file_menu = Menu(tearoff=0)

file_menu.add_command(label="Руководство", command=edit_click)
file_menu.add_separator()

main_menu.add_cascade(label="Помощь", menu=file_menu , )
root.config(menu=main_menu)


def finish():
    root.destroy()  # ручное закрытие окна и всего приложения
    print("Закрытие приложения")
root.protocol("WM_DELETE_WINDOW", finish)
root.mainloop()

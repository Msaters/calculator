from tkinter import *
import math

MainRoot = Tk()
MainRoot.title("Kalkulator")
root = Label(MainRoot, bg="#a6a6a6")
root.pack()
e = Entry(root, width=60, borderwidth=5, justify="right")
e.grid(row = 0, column=0, columnspan = 4, padx=10, pady=10)

def int_check():
    num = float(e.get())
    if(num % 1 == 0):
        num = int(num)
        e.delete(0, END)
        e.insert(0 , num)

def button_click(number):
    entered = str(e.get())
    e.delete(0, END)
    e.insert(0, entered + str(number))

def button_add():
    global first_number
    first_number = float(e.get())
    global math_sign
    math_sign = "+"
    e.delete(0, END)

def button_sub():
    global first_number
    first_number = float(e.get())
    global math_sign
    math_sign = "-"
    e.delete(0, END)

def button_div():
    global first_number
    first_number = float(e.get())
    global math_sign
    math_sign = "/"
    e.delete(0, END)

def button_multi():
    global first_number
    first_number = float(e.get())
    global math_sign
    math_sign = "*"
    e.delete(0, END)

def button_mod():
    global first_number
    first_number = float(e.get())
    global math_sign
    math_sign = "%"
    e.delete(0, END)

def button_leftBracket():
    inside = e.get()
    e.delete(0, END)
    e.insert(0, inside + '(')

def button_rightBracket():
    inside = e.get()
    e.delete(0, END)
    e.insert(0, inside + ')')

def button_point():
    inside = e.get()
    e.delete(0, END)
    e.insert(0, inside + ',')

def button_clear():
    e.delete(0, END)

def button_delte():
    e.delete(len(e.get()) - 1, END)

def button_sqrt():
    number = float(e.get())
    number = math.sqrt(number)
    e.delete(0, END)
    e.insert(0 , str(number))
    int_check()

def button_pow2():
    number = float(e.get())
    number = number * number
    e.delete(0, END)
    e.insert(0 , str(number))
    int_check()

def button_equal():
    number = float(eval(e.get()))
    print(number)
    e.delete(0 , END)
    if(math_sign == "+"):
        e.insert(0, first_number + number)
    if (math_sign == "-"):
        e.insert(0, first_number - number)
    if (math_sign == "*"):
        e.insert(0, first_number * number)
    if (math_sign == "/"):
        e.insert(0, first_number / number)
    if (math_sign == "%"):
        e.insert(0, first_number % number)
    int_check()

def on_enter(e):
    e.widget['background'] = '#666666'

def on_leave(e):
    e.widget['background'] = '#404040'

def on_enter1(e):
    e.widget['background'] = '#999999'

def on_leave1(e):
    e.widget['background'] = '#737373'

def on_enterC(e):
    e.widget['background'] = "#ff5c33"

def on_leaveC(e):
    e.widget['background'] = "#ff471a"

def on_press(event):
    catched_char = event.char
    if(event.keycode == 8):
        button_backspace.invoke()
        button_backspace.flash()
    if(catched_char == "1"):
        button_1.invoke()
        button_1.flash()
    if (catched_char == "2"):
        button_2.invoke()
        button_2.flash()
    if (catched_char == "3"):
        button_3.invoke()
        button_3.flash()
    if (catched_char == "4"):
        button_4.invoke()
        button_4.flash()
    if (catched_char == "5"):
        button_5.invoke()
        button_5.flash()
    if (catched_char == "6"):
        button_6.invoke()
        button_6.flash()
    if (catched_char == "7"):
        button_7.invoke()
        button_7.flash()
    if (catched_char == "8"):
        button_8.invoke()
        button_8.flash()
    if (catched_char == "9"):
        button_9.invoke()
        button_9.flash()
    if (catched_char == "0"):
        button_0.invoke()
        button_0.flash()
    if (catched_char == "+"):
        inside = e.get()
        e.delete(0, END)
        e.insert(0, inside + '+')
        button_add.flash()
    if (catched_char == "-"):
        inside = e.get()
        e.delete(0, END)
        e.insert(0, inside + '-')
        button_sub.flash()
    if (catched_char == "*"):
        inside = e.get()
        e.delete(0, END)
        e.insert(0, inside + '*')
        button_multi.flash()
    if (catched_char == "/"):
        inside = e.get()
        e.delete(0, END)
        e.insert(0, inside + '/')
        button_div.flash()
    if (catched_char == "="):
        number = float(eval(e.get()))
        e.delete(0, END)
        e.insert(0 ,number)
        int_check()
        button_equal.flash()
    if (catched_char == "("):
        button_leftBracket.invoke()
        button_leftBracket.flash()
    if (catched_char == ")"):
        button_rightBracket.invoke()
        button_rightBracket.flash()
    if (catched_char == "%"):
        button_mod.invoke()
        button_mod.flash()
    if (catched_char == ","):
        button_point.invoke()
        button_point.flash()

MainRoot.bind("<Key>", on_press)

button_power = Button(root, text="x^2", padx=34, pady=20, borderwidth=3, bg = "#737373", command = button_pow2, fg = "white", activebackground = "#cccccc")
button_sqrt = Button(root, text="sqrt(x)", padx=26, pady=20, borderwidth=3,bg = "#737373", command = button_sqrt, fg = "white", activebackground = "#cccccc")
button_div = Button(root, text="÷", padx=40, pady=20, borderwidth=3, bg = "#737373", command = button_div, fg = "white", activebackground = "#cccccc")
button_backspace = Button(root, text="⌫", padx=36, pady=20, borderwidth=3, bg = "#737373", command = button_delte, fg = "white", activebackground = "#cccccc")

button_leftBracket = Button(root, text="(", padx=41, pady=20, borderwidth=3, bg = "#737373", command = button_leftBracket, fg = "white", activebackground = "#cccccc")
button_rightBracket = Button(root, text=")", padx=41, pady=20, borderwidth=3,bg = "#737373", command = button_rightBracket, fg = "white", activebackground = "#cccccc")
button_mod = Button(root, text="%", padx=38, pady=20, borderwidth=3, bg = "#737373", command = button_mod, fg = "white", activebackground = "#cccccc")
button_point = Button(root, text=",", padx=42, pady=20, borderwidth=3, bg = "#737373", command = button_point, fg = "white", activebackground = "#cccccc")

button_7 = Button(root, text="7", padx=40, pady=20, borderwidth=3, bg="#404040", command = lambda: button_click(7), fg = "white", activebackground = "#666")
button_8 = Button(root, text="8", padx=40, pady=20, borderwidth=3, bg="#404040", command = lambda: button_click(8), fg = "white", activebackground = "#666")
button_9 = Button(root, text="9", padx=40, pady=20, borderwidth=3, bg="#404040", command = lambda: button_click(9), fg = "white", activebackground = "#666")
button_multi = Button(root, text="x", padx=40, pady=20, borderwidth=3, bg = "#737373", command = button_multi, fg = "white", activebackground = "#cccccc")

button_4 = Button(root, text="4", padx=40, pady=20, borderwidth=3, bg="#404040", command = lambda: button_click(4), fg = "white", activebackground = "#666")
button_5 = Button(root, text="5", padx=40, pady=20, borderwidth=3, bg="#404040", command = lambda: button_click(5), fg = "white", activebackground = "#666")
button_6 = Button(root, text="6", padx=40, pady=20, borderwidth=3, bg="#404040", command = lambda: button_click(6), fg = "white", activebackground = "#666")
button_add = Button(root, text="+", padx=40, pady=20, borderwidth=3, bg = "#737373", command = button_add, fg = "white", activebackground = "#cccccc")

button_1 = Button(root, text="1", padx=40, pady=20, borderwidth=3, bg="#404040", command = lambda: button_click(1), fg = "white", activebackground = "#666")
button_2 = Button(root, text="2", padx=40, pady=20, borderwidth=3, bg="#404040", command = lambda: button_click(2), fg = "white", activebackground = "#666")
button_3 = Button(root, text="3", padx=40, pady=20, borderwidth=3, bg="#404040", command = lambda: button_click(3), fg = "white", activebackground = "#666")
button_sub = Button(root, text="-", padx=42, pady=20, borderwidth=3, bg = "#737373", command = button_sub, fg = "white", activebackground = "#cccccc")

button_0 = Button(root, text="0", padx=40, pady=20, borderwidth=3, bg="#737373", command = lambda: button_click(0), fg = "white", activebackground =  "#cccccc")
button_equal = Button(root, text="=", padx=88, pady=20, borderwidth=3, bg = "#ff471a", command = button_equal, fg = "white", activebackground = "#ff582b")
button_clear = Button(root, text="Clear", padx=31, pady=20, borderwidth=3, bg = "#737373", command = button_clear, fg = "white", activebackground =  "#cccccc")

button_1.grid(row = 5, column=0)
button_2.grid(row = 5, column=1)
button_3.grid(row = 5, column=2)
button_4.grid(row = 4, column=0)
button_5.grid(row = 4, column=1)
button_6.grid(row = 4, column=2)
button_7.grid(row = 3, column=0)
button_8.grid(row = 3, column=1)
button_9.grid(row = 3, column=2)

buttons = [button_1, button_2, button_3, button_4, button_5, button_6, button_7, button_8, button_9]

for button in buttons:
    button.bind("<Enter>", on_enter)
    button.bind("<Leave>", on_leave)

button_leftBracket.grid(row = 2, column = 0)
button_rightBracket.grid(row = 2, column = 1)
button_point.grid(row = 2, column = 2)
button_mod.grid(row = 2, column = 3)
button_power.grid(row = 1, column=0)
button_sqrt.grid(row = 1, column=1)
button_div.grid(row = 1, column=2)
button_backspace.grid(row = 1, column=3)
button_multi.grid(row = 3, column=3)
button_add.grid(row = 4, column=3)
button_sub.grid(row = 5, column=3)
button_0.grid(row = 6, column=0)
button_clear.grid(row = 6, column=3)

buttons1 = [button_power,button_sqrt,button_div,button_backspace,button_multi,button_add,button_sub,button_0, button_clear, button_leftBracket, button_rightBracket, button_mod, button_point]

for button in buttons1:
    button.bind("<Enter>", on_enter1)
    button.bind("<Leave>", on_leave1)

button_equal.grid(row = 6, column=1, columnspan = 2)

button_equal.bind("<Enter>", on_enterC)
button_equal.bind("<Leave>", on_leaveC)

MainRoot.mainloop()


import tkinter as tk

field_text = " "

def add_to_field(something) :
    global field_text
    field_text = field_text + str(something)
    field.delete('1.0','end')
    field.insert('1.0',field_text)

def calculate() :
    global field_text
    result = eval(field_text)
    field.delete('1.0','end')
    field.insert('1.0',result)

def clear() :
    global field_text
    field_text = " "
    field.delete('1.0','end')
                
main_window = tk.Tk()
main_window.title("Simple calculator")
main_window.geometry("370x350")
field = tk.Text(main_window,height=1,width= 26,font=("Calibri",21))
field.grid(row=1,column=1,columnspan=4)

# Let's  create the Number Buttons

btn1 = tk.Button(main_window,text = "1", bg = 'Red', command= lambda: add_to_field(1),width=7, font=("Calibri",15))
btn1.grid(row=4,column=1)

btn2 = tk.Button(main_window,text = "2", bg = 'Red', command= lambda: add_to_field(2),width=7, font=("Calibri",15))
btn2.grid(row=4,column=2)


btn3 = tk.Button(main_window,text = "3", bg = 'Red', command= lambda: add_to_field(3),width=7, font=("Calibri",15))
btn3.grid(row=4,column=3)

btn4 = tk.Button(main_window,text = "4", bg = 'Red', command= lambda: add_to_field(4),width=7, font=("Calibri",15))
btn4.grid(row=3,column=1)

btn5 = tk.Button(main_window,text = "5", bg = 'Red', command= lambda: add_to_field(5),width=7, font=("Calibri",15))
btn5.grid(row=3,column=2)

btn6 = tk.Button(main_window,text = "6", bg = 'Red', command= lambda: add_to_field(6),width=7, font=("Calibri",15))
btn6.grid(row=3,column=3)

btn7 = tk.Button(main_window,text = "7", bg = 'Red', command= lambda: add_to_field(7),width=7, font=("Calibri",15))
btn7.grid(row=2,column=1)

btn8 = tk.Button(main_window,text = "8", bg = 'Red', command= lambda: add_to_field(8),width=7, font=("Calibri",15))
btn8.grid(row=2,column=2)

btn9 = tk.Button(main_window,text = "9", bg = 'Red', command= lambda: add_to_field(9),width=7, font=("Calibri",15))
btn9.grid(row=2,column=3)

btn0 = tk.Button(main_window,text = "0", bg = 'Red', command= lambda: add_to_field(0),width=7, font=("Calibri",15))
btn0.grid(row=5,column=1)

#Now the operations button and the clear button

btn_plus = tk.Button(main_window,text = "+", bg = 'Yellow', command= lambda: add_to_field("+"),width=7, font=("Calibri",15))
btn_plus.grid(row=4,column=4)

btn_minus = tk.Button(main_window,text = "-", bg = 'Yellow', command= lambda: add_to_field("-"),width=7, font=("Calibri",15))
btn_minus.grid(row=5,column=4)

btn_into = tk.Button(main_window,text = "*", bg = 'Yellow', command= lambda: add_to_field("*"),width=7, font=("Calibri",15))
btn_into.grid(row=3,column=4)

btn_division = tk.Button(main_window,text = "/", bg = 'Yellow', command= lambda: add_to_field("/"),width=7, font=("Calibri",15))
btn_division.grid(row=2,column=4)

btn_clear = tk.Button(main_window,text = "C", bg = 'Green', command= lambda: clear(),width=7, font=("Calibri",15))
btn_clear.grid(row=5,column=3)

btn_decimal = tk.Button(main_window,text = ".", bg = 'Yellow', command= lambda: add_to_field("."),width=7, font=("Calibri",15))
btn_decimal.grid(row=5,column=2)

btn_parenthesis1 = tk.Button(main_window,text = "(", bg = 'Blue', command= lambda: add_to_field("("),width=7, font=("Calibri",15))
btn_parenthesis1.grid(row=6,column=1)

btn_parenthesis2 = tk.Button(main_window,text = ")", bg = 'Blue', command= lambda: add_to_field(")"),width=7, font=("Calibri",15))
btn_parenthesis2.grid(row=6,column=2)

btn_equal = tk.Button(main_window,text = "=", bg = 'Orange', command= lambda: calculate(),width=16, font=("Calibri",15))
btn_equal.grid(row=6,column=3,columnspan=4)

main_window.mainloop()

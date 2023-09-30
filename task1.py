#Compozent Internship Basic Task
#Calculator app

from tkinter import Tk, Canvas, Button, Entry

def calculate():
    try:
        expression = entry.get()
        result = str(eval(expression))
        entry.delete(0, 'end')
        entry.insert('end', result)
    except Exception as e:
        entry.delete(0, 'end')
        entry.insert('end', 'Error')

def clear():
    entry.delete(0, 'end')

def button_click(char):
    current = entry.get()
    entry.delete(0, 'end')
    entry.insert('end', current + str(char))

window = Tk()
window.title("Calculator")
window.configure(bg="#D3D3CE")

entry = Entry(window,bg="#D3D3CE", width=20, font=("Arial", 20))
entry.grid(row=0, column=0, columnspan=4)

buttons = [
    '7', '8', '9', '/',
    '4', '5', '6', '*',
    '1', '2', '3', '-',
    '0', '+', '=', 'C'
]

row_val = 1
col_val = 0

for button in buttons:
    if button == 'C':
        Button(window, text=button, padx=20, pady=15, bg="#f00",fg="#fff", font=("Arial", 18), command=clear).grid(row=row_val, column=col_val)
    else:
        Button(window, text=button, padx=20, pady=15, bg="#F0F047", fg="#000", font=("Arial", 18),
               command=lambda b=button: button_click(b) if b != '=' else calculate()).grid(row=row_val, column=col_val)
    
    col_val += 1
    if col_val > 3:
        col_val = 0
        row_val += 1

window.mainloop()

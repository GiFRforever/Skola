import tkinter as tk
from tkinter import messagebox


# define function for addition
def addition(a, b):
    return a + b


# define function for subtraction
def subtraction(a, b):
    return a - b


# define function for multiplication
def multiplication(a, b):
    return a * b


# define function for division
def division(a, b):
    if b == 0:
        messagebox.showerror("Error", "Division by zero is not allowed!")
        return None
    else:
        return a / b


# define function to execute the desired operation
def execute_operation():
    a = float(num1_entry.get())
    b = float(num2_entry.get())

    if operation_var.get() == "1. Addition":
        result = addition(a, b)
    elif operation_var.get() == "2. Subtraction":
        result = subtraction(a, b)
    elif operation_var.get() == "3. Multiplication":
        result = multiplication(a, b)
    elif operation_var.get() == "4. Division":
        result = division(a, b)
    else:
        messagebox.showerror("Error", "idk what happened")
        return None

    if result is not None:
        result_text.set(str(result))


# create the main window
root = tk.Tk()
root.title("Počítání")

# create widgets
operation_var = tk.StringVar()
result_text = tk.StringVar()

num1_label = tk.Label(root, text="Enter first number:")
num1_entry = tk.Entry(root)

num2_label = tk.Label(root, text="Enter second number:")
num2_entry = tk.Entry(root)

operation_label = tk.Label(root, text="Select operation:")
operation_menu = tk.OptionMenu(
    root,
    operation_var,
    "1. Addition",
    "2. Subtraction",
    "3. Multiplication",
    "4. Division",
)

execute_button = tk.Button(root, text="Execute Operation", command=execute_operation)

result_label = tk.Label(root, text="Result:")
result_entry = tk.Entry(root, textvariable=result_text)

# position widgets
num1_label.grid(row=0, column=0)
num1_entry.grid(row=0, column=1)

num2_label.grid(row=1, column=0)
num2_entry.grid(row=1, column=1)

operation_label.grid(row=2, column=0)
operation_menu.grid(row=2, column=1)

execute_button.grid(row=3, column=0, columnspan=2)

result_label.grid(row=4, column=0)
result_entry.grid(row=4, column=1)

# run the main loop
root.mainloop()

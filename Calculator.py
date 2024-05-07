import tkinter as tk
from tkinter import messagebox, simpledialog
import math

def main():
    window = tk.Tk()
    window.title('Advanced Area Calculator')

    frame = tk.Frame(window, bg="grey")
    frame.pack(padx=10, pady=10)

    entry = tk.Entry(frame, width=18, font=('Arial', 24), borderwidth=2, relief="solid", state="readonly")
    entry.grid(row=0, column=0, columnspan=4, padx=5, pady=5)

    def add_to_entry(symbol):
        entry.config(state=tk.NORMAL)
        entry.insert(tk.END, symbol)
        entry.config(state="readonly")

    def clear_entry():
        entry.config(state=tk.NORMAL)
        entry.delete(0, tk.END)
        entry.config(state="readonly")

    def calculate_result():
        entry.config(state=tk.NORMAL)
        try:
            result = eval(entry.get())
            entry.delete(0, tk.END)
            entry.insert(0, result)
        except:
            messagebox.showerror("Error", "Invalid Input")
        entry.config(state="readonly")

    def delete_last():
        entry.config(state=tk.NORMAL)
        current = entry.get()
        length = len(current) - 1
        entry.delete(length, tk.END)
        entry.config(state="readonly")

    def calculate_area():
        shape = shape_var.get()
        if shape == "Select Shape":
            messagebox.showinfo("Info", "Please select a valid shape")
            return
        entry.config(state=tk.NORMAL)
        area = 0
        if shape == 'Circle':
            radius = simpledialog.askfloat("Input", "Enter the radius:")
            area = math.pi * radius ** 2
        elif shape == 'Square':
            side = simpledialog.askfloat("Input", "Enter the side length:")
            area = side ** 2
        elif shape == 'Rectangle':
            width = simpledialog.askfloat("Input", "Enter the width:")
            height = simpledialog.askfloat("Input", "Enter the height:")
            area = width * height
        elif shape == 'Triangle':
            base = simpledialog.askfloat("Input", "Enter the base length:")
            height = simpledialog.askfloat("Input", "Enter the height:")
            area = 0.5 * base * height
        entry.delete(0, tk.END)
        entry.insert(0, f"Area = {area:.2f}")
        entry.config(state="readonly")

    button_texts = [
        ('7', 1, 0), ('8', 1, 1), ('9', 1, 2), ('/', 1, 3),
        ('4', 2, 0), ('5', 2, 1), ('6', 2, 2), ('*', 2, 3),
        ('1', 3, 0), ('2', 3, 1), ('3', 3, 2), ('-', 3, 3),
        ('0', 4, 1), ('+', 4, 2), ('.', 4, 0)
    ]

    for (text, row, col) in button_texts:
        button = tk.Button(frame, text=text, padx=20, pady=20, bg="light grey", font=('Arial', 16),
                           command=lambda text=text: add_to_entry(text))
        button.grid(row=row, column=col, sticky="nsew")

    equal_button = tk.Button(frame, text='=', padx=20, pady=20, bg="light grey", font=('Arial', 16),
                             command=calculate_result)
    equal_button.grid(row=4, column=3, sticky="nsew")

    tk.Button(frame, text='Clear', padx=20, pady=20, bg="light grey", font=('Arial', 16), command=clear_entry).grid(
        row=1, column=4,sticky="nsew")

    tk.Button(frame, text='Del', padx=20, pady=20, bg="light grey", font=('Arial', 16), command=delete_last).grid(
        row=2, column=4, sticky="nsew")

    tk.Button(frame, text='Calculate Shape', padx=20, pady=20, bg="light grey", font=('Arial', 16),
              command=calculate_area).grid(row=4, column=4, sticky="nsew")

    shape_var = tk.StringVar(window)
    shape_var.set("Select Shape")  # default value
    shapes = ['Circle', 'Square', 'Rectangle', 'Triangle']
    shape_menu = tk.OptionMenu(frame, shape_var, *shapes)
    shape_menu.config(font=('Arial', 16), bg="light grey", width=12)
    shape_menu.grid(row=3, column=4, sticky="nsew")

    window.resizable(True, True)
    window.mainloop()

if __name__ == '__main__':
    main()

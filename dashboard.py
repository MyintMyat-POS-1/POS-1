import tkinter as tk
from tkinter import messagebox

def open_add_product():
    messagebox.showinfo("Info", "Add Product clicked")

def open_view_products():
    messagebox.showinfo("Info", "View Products clicked")

def exit_app():
    root.destroy()

root = tk.Tk()
root.title("POS Dashboard")
root.geometry("400x300")

label = tk.Label(root, text="Welcome to POS Dashboard", font=("Arial", 16))
label.pack(pady=20)

btn_add = tk.Button(root, text="Add Product", width=20, command=open_add_product)
btn_add.pack(pady=10)

btn_view = tk.Button(root, text="View Products", width=20, command=open_view_products)
btn_view.pack(pady=10)

btn_exit = tk.Button(root, text="Exit", width=20, command=exit_app)
btn_exit.pack(pady=10)

root.mainloop()

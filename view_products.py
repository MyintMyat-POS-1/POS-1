import tkinter as tk
from tkinter import ttk
import sqlite3

def fetch_products():
    conn = sqlite3.connect('db.sqlite3')
    c = conn.cursor()
    c.execute("SELECT id, name, price, stock FROM products")
    rows = c.fetchall()
    conn.close()
    return rows

def load_products():
    for row in tree.get_children():
        tree.delete(row)

    for product in fetch_products():
        tree.insert('', tk.END, values=product)

# Create GUI window
root = tk.Tk()
root.title("Product List")
root.geometry("500x300")

# Table
columns = ('ID', 'Name', 'Price', 'Stock')
tree = ttk.Treeview(root, columns=columns, show='headings')

for col in columns:
    tree.heading(col, text=col)
    tree.column(col, width=100)

tree.pack(fill=tk.BOTH, expand=True)

# Scrollbar
scrollbar = ttk.Scrollbar(root, orient='vertical', command=tree.yview)
tree.configure(yscrollcommand=scrollbar.set)
scrollbar.pack(side='right', fill='y')

# Refresh button
refresh_btn = tk.Button(root, text="Refresh", command=load_products)
refresh_btn.pack(pady=5)

# Load data on startup
load_products()

root.mainloop()

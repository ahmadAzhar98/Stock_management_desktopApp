from tkinter import *
from tkinter import messagebox
import pymysql

# Function to connect to the database
def connection():
    conn = pymysql.connect(
        host='localhost',
        user='root',
        password='',
        db='stock_management'
    )
    return conn

# Function to add product to the database
def add_product(name_entry, quantity_entry, price_entry, category_entry):
    name = name_entry.get()
    quantity = quantity_entry.get()
    price = price_entry.get()
    category = category_entry.get()
    
    if not name or not quantity or not price or not category:
        messagebox.showwarning("Input Error", "All fields are required.")
        return
    
    try:
        conn = connection()
        cursor = conn.cursor()
        
        sql = "INSERT INTO products (name, quantity, price, category) VALUES (%s, %s, %s, %s)"
        cursor.execute(sql, (name, quantity, price, category))
        conn.commit()
        conn.close()
        
        messagebox.showinfo("Success", "Product added successfully.")
        
        # Clear the input fields after successful submission
        name_entry.delete(0, END)
        quantity_entry.delete(0, END)
        price_entry.delete(0, END)
        category_entry.delete(0, END)
    
    except Exception as e:
        messagebox.showerror("Error", f"An error occurred: {e}")

# Function to create the Add Products window
def create_add_products_window():
    # Create the Add Products window
    add_products_window = Tk()
    add_products_window.title("Add Products")
    add_products_window.geometry("700x500")
    
    # Labels and entry fields
    name_label = Label(add_products_window, text="Product Name")
    name_label.pack(pady=5)
    name_entry = Entry(add_products_window)
    name_entry.pack(pady=5)
    
    quantity_label = Label(add_products_window, text="Quantity")
    quantity_label.pack(pady=5)
    quantity_entry = Entry(add_products_window)
    quantity_entry.pack(pady=5)
    
    price_label = Label(add_products_window, text="Price")
    price_label.pack(pady=5)
    price_entry = Entry(add_products_window)
    price_entry.pack(pady=5)
    
    category_label = Label(add_products_window, text="Category")
    category_label.pack(pady=5)
    category_entry = Entry(add_products_window)
    category_entry.pack(pady=5)
    
    # Add Product button
    add_button = Button(add_products_window, text="Add Product", command=lambda: add_product(name_entry, quantity_entry, price_entry, category_entry))
    add_button.pack(pady=10)
    
    # Back button
    back_button = Button(add_products_window, text="Back", command=lambda: add_products_window.destroy())  # Or call a function to go back
    back_button.pack(pady=10)
    
    return add_products_window

# Function to open the Add Products page
def open_add_products_page():
    window = create_add_products_window()
    window.mainloop()

# Now you can call open_add_products_page() to open this page wherever required.

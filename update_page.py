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

# Function to search for a product by ID
def search_product(product_id_entry, name_entry, quantity_entry, price_entry, category_entry, update_button):
    product_id = product_id_entry.get().strip()

    if not product_id:
        messagebox.showwarning("Error", "Please enter a Product ID")
        return

    try:
        conn = connection()
        cursor = conn.cursor()
        sql = "SELECT * FROM products WHERE id = %s"
        cursor.execute(sql, (product_id,))
        product = cursor.fetchone()

        if product:
            name_entry.delete(0, END)
            name_entry.insert(0, product[1])

            quantity_entry.delete(0, END)
            quantity_entry.insert(0, product[2])

            price_entry.delete(0, END)
            price_entry.insert(0, product[3])

            category_entry.delete(0, END)
            category_entry.insert(0, product[4])
            
            update_button.config(state=NORMAL)
        else:
            messagebox.showerror("Error", "Product not found")

        conn.close()
    except Exception as e:
        messagebox.showerror("Error", f"An error occurred: {e}")

# Function to update the product details
def update_product(product_id_entry, name_entry, quantity_entry, price_entry, category_entry):
    product_id = product_id_entry.get().strip()
    name = name_entry.get().strip()
    quantity = quantity_entry.get().strip()
    price = price_entry.get().strip()
    category = category_entry.get().strip()

    if not name or not quantity or not price or not category:
        messagebox.showwarning("Error", "Please fill out all fields")
        return

    try:
        conn = connection()
        cursor = conn.cursor()
        sql = """
        UPDATE products 
        SET name = %s, quantity = %s, price = %s, category = %s 
        WHERE id = %s
        """
        cursor.execute(sql, (name, quantity, price, category, product_id))
        conn.commit()
        messagebox.showinfo("Success", "Product updated successfully")
        conn.close()
    except Exception as e:
        messagebox.showerror("Error", f"An error occurred: {e}")

# Function to create the Update Product window
def create_update_window(go_back_callback):
    update_window = Tk()
    update_window.title("Update Product")
    update_window.geometry("1024x700")

    # Labels and entry for Product ID
    product_id_label = Label(update_window, text="Enter Product ID:")
    product_id_label.pack(pady=10)
    product_id_entry = Entry(update_window)
    product_id_entry.pack(pady=5)

    # Search Button
    search_button = Button(update_window, text="Search", command=lambda: search_product(product_id_entry, name_entry, quantity_entry, price_entry, category_entry, update_button))
    search_button.pack(pady=10)

    # Labels and entry fields for updating product details
    name_label = Label(update_window, text="Name:")
    name_label.pack(pady=5)
    name_entry = Entry(update_window)
    name_entry.pack(pady=5)

    quantity_label = Label(update_window, text="Quantity:")
    quantity_label.pack(pady=5)
    quantity_entry = Entry(update_window)
    quantity_entry.pack(pady=5)

    price_label = Label(update_window, text="Price:")
    price_label.pack(pady=5)
    price_entry = Entry(update_window)
    price_entry.pack(pady=5)

    category_label = Label(update_window, text="Category:")
    category_label.pack(pady=5)
    category_entry = Entry(update_window)
    category_entry.pack(pady=5)

    # Update Button (Initially disabled)
    update_button = Button(update_window, text="Update Product", command=lambda: update_product(product_id_entry, name_entry, quantity_entry, price_entry, category_entry), state=DISABLED)
    update_button.pack(pady=20)

    # Back Button
    back_button = Button(update_window, text="Back", command=go_back_callback)
    back_button.pack(pady=10)

    return update_window

# Function to open the Update Product page
def open_update_product_page():
    def go_back():
        update_window.destroy()
        import home_page
        home_page.open_home_page()

    update_window = create_update_window(go_back)
    update_window.mainloop()

# Now you can call open_update_product_page() to open this page wherever required.

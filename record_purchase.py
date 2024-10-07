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

# Function to handle recording a purchase
def record_purchase(product_id_entry, sale_price_entry, quantity_entry):
    product_id = product_id_entry.get().strip()
    sale_price = sale_price_entry.get().strip()
    quantity_purchased = quantity_entry.get().strip()

    if not product_id or not sale_price or not quantity_purchased:
        messagebox.showwarning("Error", "Please fill all fields")
        return

    try:
        conn = connection()
        cursor = conn.cursor()
        
        # Check if product exists
        cursor.execute("SELECT quantity FROM products WHERE id = %s", (product_id,))
        result = cursor.fetchone()
        
        if not result:
            messagebox.showerror("Error", "Product ID does not exist")
            conn.close()
            return

        quantity_in_stock = result[0]
        quantity_purchased = int(quantity_purchased)
        sale_price = float(sale_price)

        if quantity_purchased > quantity_in_stock:
            messagebox.showerror("Error", "Quantity purchased exceeds stock")
            conn.close()
            return

        # Update quantity in stock
        new_quantity_in_stock = quantity_in_stock - quantity_purchased
        cursor.execute("UPDATE products SET quantity = %s WHERE id = %s", (new_quantity_in_stock, product_id))

        # Record the purchase in the sales table
        total_sales = quantity_purchased * sale_price
        cursor.execute("INSERT INTO sales (product_id, quantity_sold, sale_price, total_sale, sale_date) VALUES (%s, %s, %s, %s, NOW())",
                       (product_id, quantity_purchased, sale_price, total_sales))
        
        conn.commit()

        # Check if the stock is low
        if new_quantity_in_stock < 10:
            messagebox.showwarning("Low Stock", f"Warning: Stock is low for product ID {product_id}. Only {new_quantity_in_stock} left.")
        
        conn.close()
        
        messagebox.showinfo("Success", f"Purchase recorded successfully. Total Sales: {total_sales:.2f}")
        
    except Exception as e:
        messagebox.showerror("Error", f"An error occurred: {e}")

# Function to create the Record Purchase window
def create_record_purchase_window(go_back_callback):
    record_purchase_window = Tk()
    record_purchase_window.title("Record Purchase")
    record_purchase_window.geometry("800x500")

    # Labels and entries
    product_id_label = Label(record_purchase_window, text="Product ID")
    product_id_label.pack(pady=10)
    product_id_entry = Entry(record_purchase_window)
    product_id_entry.pack(pady=5)

    sale_price_label = Label(record_purchase_window, text="Sale Price")
    sale_price_label.pack(pady=10)
    sale_price_entry = Entry(record_purchase_window)
    sale_price_entry.pack(pady=5)

    quantity_label = Label(record_purchase_window, text="Quantity Purchased")
    quantity_label.pack(pady=10)
    quantity_entry = Entry(record_purchase_window)
    quantity_entry.pack(pady=5)

    # Buttons
    record_button = Button(record_purchase_window, text="Record Purchase", command=lambda: record_purchase(product_id_entry, sale_price_entry, quantity_entry))
    record_button.pack(pady=20)

    back_button = Button(record_purchase_window, text="Back", command=go_back_callback)
    back_button.pack(pady=10)

    return record_purchase_window

# Function to open the Record Purchase page
def open_record_purchase_page():
    def go_back():
        record_purchase_window.destroy()
        import home_page
        home_page.open_home_page()

    record_purchase_window = create_record_purchase_window(go_back)
    record_purchase_window.mainloop()

# Now you can call open_record_purchase_page() to open this page wherever required.

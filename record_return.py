from tkinter import *
from tkinter import messagebox
import pymysql
from datetime import datetime

# Function to connect to the database
def connection():
    conn = pymysql.connect(
        host='localhost',
        user='root',
        password='',
        db='stock_management'
    )
    return conn

# Function to handle recording a return
def record_return(product_id_entry, return_price_entry, quantity_entry):
    product_id = product_id_entry.get().strip()
    return_price = return_price_entry.get().strip()
    quantity_returned = quantity_entry.get().strip()

    if not product_id or not return_price or not quantity_returned:
        messagebox.showwarning("Error", "Please fill all fields")
        return

    try:
        conn = connection()
        cursor = conn.cursor()

        # Check if product exists
        cursor.execute("SELECT quantity FROM products WHERE id = %s", (product_id,))
        product_result = cursor.fetchone()

        if not product_result:
            messagebox.showerror("Error", "Product ID does not exist")
            conn.close()
            return

        # Check if there are sales records for the product
        cursor.execute("SELECT quantity_sold, total_sale FROM sales WHERE product_id = %s ORDER BY sale_date DESC LIMIT 1", (product_id,))
        sales_result = cursor.fetchone()

        if not sales_result:
            messagebox.showerror("Error", "No sales record found for this product")
            conn.close()
            return

        quantity_in_stock = product_result[0]
        quantity_returned = int(quantity_returned)
        return_price = float(return_price)
        quantity_sold = sales_result[0]
        total_sales = sales_result[1]

        if quantity_returned > quantity_sold:
            messagebox.showerror("Error", "Return quantity exceeds sold quantity")
            conn.close()
            return

        # Update quantity in stock
        new_quantity_in_stock = quantity_in_stock + quantity_returned
        cursor.execute("UPDATE products SET quantity = %s WHERE id = %s", (new_quantity_in_stock, product_id))

        # Insert new sales record for the return
        total_return_sales = quantity_returned * return_price
        cursor.execute("INSERT INTO sales (product_id, quantity_sold, sale_price, total_sale, sale_date) VALUES (%s, %s, %s, %s, %s)",
                       (product_id, -quantity_returned, return_price, -total_return_sales, datetime.now()))

        conn.commit()
        conn.close()

        messagebox.showinfo("Success", "Return recorded successfully")

    except Exception as e:
        messagebox.showerror("Error", f"An error occurred: {e}")

# Function to create the Record Return window
def create_record_return_window(go_back_callback):
    record_return_window = Tk()
    record_return_window.title("Record Return")
    record_return_window.geometry("800x500")

    # Labels and entries
    product_id_label = Label(record_return_window, text="Product ID")
    product_id_label.pack(pady=10)
    product_id_entry = Entry(record_return_window)
    product_id_entry.pack(pady=5)

    return_price_label = Label(record_return_window, text="Return Price")
    return_price_label.pack(pady=10)
    return_price_entry = Entry(record_return_window)
    return_price_entry.pack(pady=5)

    quantity_label = Label(record_return_window, text="Quantity Returned")
    quantity_label.pack(pady=10)
    quantity_entry = Entry(record_return_window)
    quantity_entry.pack(pady=5)

    # Buttons
    record_button = Button(record_return_window, text="Record Return", command=lambda: record_return(product_id_entry, return_price_entry, quantity_entry))
    record_button.pack(pady=20)

    back_button = Button(record_return_window, text="Back", command=go_back_callback)
    back_button.pack(pady=10)

    return record_return_window

# Function to open the Record Return page
def open_record_return_page():
    def go_back():
        record_return_window.destroy()
        import home_page
        home_page.open_home_page()

    record_return_window = create_record_return_window(go_back)
    record_return_window.mainloop()

# Now you can call open_record_return_page() to open this page wherever required.

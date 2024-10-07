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

# Function to delete a product by Product ID
def delete_product(product_id_entry):
    try:
        # Validate that the input is an integer
        product_id = int(product_id_entry.get())
    except ValueError:
        messagebox.showwarning("Input Error", "Product ID must be an integer.")
        return
    
    if not product_id:
        messagebox.showwarning("Input Error", "Please enter a Product ID.")
        return
    
    try:
        conn = connection()
        cursor = conn.cursor()
        
        # Check if product exists before attempting to delete
        cursor.execute("SELECT * FROM products WHERE id = %s", (product_id,))
        result = cursor.fetchone()
        
        if not result:
            messagebox.showerror("Error", "Product with this ID does not exist.")
            return
        
        # Delete product from the database
        sql = "DELETE FROM products WHERE id = %s"
        cursor.execute(sql, (product_id,))
        conn.commit()
        conn.close()
        
        messagebox.showinfo("Success", "Product deleted successfully.")
        product_id_entry.delete(0, END)
    
    except Exception as e:
        messagebox.showerror("Error", f"An error occurred: {e}")

# Function to create the Delete Products window
def create_delete_products_window(go_back_callback):
    # Create the Delete Products window
    delete_products_window = Tk()
    delete_products_window.title("Delete Product")
    delete_products_window.geometry("400x200")
    
    # Label and entry field for Product ID
    product_id_label = Label(delete_products_window, text="Product ID")
    product_id_label.pack(pady=10)
    product_id_entry = Entry(delete_products_window)
    product_id_entry.pack(pady=10)
    
    # Delete Product button
    delete_button = Button(delete_products_window, text="Delete Product", command=lambda: delete_product(product_id_entry))
    delete_button.pack(pady=10)
    
    # Back button
    back_button = Button(delete_products_window, text="Back", command=go_back_callback)
    back_button.pack(pady=10)
    
    return delete_products_window

# Function to open the Delete Products page
def open_delete_products_page():
    def go_back():
        delete_products_window.destroy()
        import home_page
        home_page.open_home_page()
    
    delete_products_window = create_delete_products_window(go_back)
    delete_products_window.mainloop()

# Now you can call open_delete_products_page() to open this page wherever required.

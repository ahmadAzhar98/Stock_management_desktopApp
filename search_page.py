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

# Function to perform the search
def search_product(product_name_entry, min_price_entry, max_price_entry, category_entry, result_frame):
    product_name = product_name_entry.get().strip()
    min_price = min_price_entry.get().strip()
    max_price = max_price_entry.get().strip()
    category = category_entry.get().strip()

    try:
        conn = connection()
        cursor = conn.cursor()

        query = "SELECT * FROM products WHERE 1=1"
        params = []

        if product_name:
            query += " AND name LIKE %s"
            params.append(f"%{product_name}%")
        
        if min_price and max_price:
            query += " AND price BETWEEN %s AND %s"
            params.append(min_price)
            params.append(max_price)

        if category:
            query += " AND category = %s"
            params.append(category)

        cursor.execute(query, tuple(params))
        results = cursor.fetchall()
        
        # Clear previous results
        for widget in result_frame.winfo_children():
            widget.destroy()

        if results:
            for i, result in enumerate(results):
                result_label = Label(result_frame, text=f"{i+1}. Name: {result[1]}, Price: {result[2]}, Category: {result[4]}")
                result_label.pack(anchor='w', pady=5)
        else:
            no_result_label = Label(result_frame, text="No products found.")
            no_result_label.pack()

        conn.close()
    except Exception as e:
        messagebox.showerror("Error", f"An error occurred: {e}")

# Function to create the Search Products window
def create_search_window(go_back_callback):
    search_window = Tk()
    search_window.title("Search Product")
    search_window.geometry("700x500")

    # Labels and entries for search criteria
    product_name_label = Label(search_window, text="Product Name:")
    product_name_label.pack(pady=5)
    product_name_entry = Entry(search_window)
    product_name_entry.pack(pady=5)

    min_price_label = Label(search_window, text="Min Price:")
    min_price_label.pack(pady=5)
    min_price_entry = Entry(search_window)
    min_price_entry.pack(pady=5)

    max_price_label = Label(search_window, text="Max Price:")
    max_price_label.pack(pady=5)
    max_price_entry = Entry(search_window)
    max_price_entry.pack(pady=5)

    category_label = Label(search_window, text="Category:")
    category_label.pack(pady=5)
    category_entry = Entry(search_window)
    category_entry.pack(pady=5)

    # Search button
    search_button = Button(search_window, text="Search", command=lambda: search_product(product_name_entry, min_price_entry, max_price_entry, category_entry, result_frame))
    search_button.pack(pady=10)

    # Frame to display search results
    result_frame = Frame(search_window)
    result_frame.pack(pady=20, fill=BOTH, expand=True)

    # Back button
    back_button = Button(search_window, text="Back", command=go_back_callback)
    back_button.pack(pady=10)

    return search_window

# Function to open the Search Products page
def open_search_products_page():
    def go_back():
        search_window.destroy()
        import home_page
        home_page.open_home_page()

    search_window = create_search_window(go_back)
    search_window.mainloop()

# Now you can call open_search_products_page() to open this page wherever required.

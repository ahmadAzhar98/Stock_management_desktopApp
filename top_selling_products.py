from tkinter import *
from tkinter import scrolledtext
import pymysql

def connection():
    conn = pymysql.connect(
        host='localhost',
        user='root',
        password='',
        db='stock_management'
    )
    return conn

def generate_top_selling_products():
    try:
        conn = connection()
        cursor = conn.cursor()
        
        cursor.execute("SELECT product_id, SUM(quantity_sold) AS total_quantity FROM sales GROUP BY product_id ORDER BY total_quantity DESC LIMIT 10")
        top_products = cursor.fetchall()

        result_text.delete(1.0, END)
        result_text.insert(END, "Top-Selling Products Report\n")
        result_text.insert(END, "Product ID | Total Quantity Sold\n")
        for product_id, total_quantity in top_products:
            result_text.insert(END, f"{product_id} | {total_quantity}\n")

        conn.close()

    except Exception as e:
        result_text.delete(1.0, END)
        result_text.insert(END, f"An error occurred: {e}")

def back_button():
    import sales_and_report
    sales_and_report.open_sales_and_reporting()  

# Create a window for top-selling products
top_products_window = Tk()
top_products_window.title("Top-Selling Products Report")
top_products_window.geometry("800x500")

# Button to generate report
generate_button = Button(top_products_window, text="Generate Report", command=generate_top_selling_products)
generate_button.pack(pady=20)

# Text widget to display results
result_text = scrolledtext.ScrolledText(top_products_window, wrap=WORD, width=100, height=30)
result_text.pack(pady=10)

# Back button
back_button = Button(top_products_window, text="Back", command=back_button)
back_button.pack(pady=10)

# Start the window loop
top_products_window.mainloop()

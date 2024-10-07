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

def generate_revenue_analysis():
    try:
        conn = connection()
        cursor = conn.cursor()
        
        cursor.execute("SELECT SUM(total_sale) FROM sales")
        total_revenue = cursor.fetchone()[0]

        result_text.delete(1.0, END)
        result_text.insert(END, "Revenue Analysis Report\n")
        result_text.insert(END, f"Total Revenue: {total_revenue:.2f}\n")

        conn.close()

    except Exception as e:
        result_text.delete(1.0, END)
        result_text.insert(END, f"An error occurred: {e}")

def back_button():
    import sales_and_report
    sales_and_report.open_sales_and_reporting()  

# Create a window for revenue analysis
revenue_window = Tk()
revenue_window.title("Revenue Analysis Report")
revenue_window.geometry("800x500")

# Button to generate report
generate_button = Button(revenue_window, text="Generate Report", command=generate_revenue_analysis)
generate_button.pack(pady=20)

# Text widget to display results
result_text = scrolledtext.ScrolledText(revenue_window, wrap=WORD, width=100, height=30)
result_text.pack(pady=10)

# Back button
back_button = Button(revenue_window, text="Back", command=back_button)
back_button.pack(pady=10)

# Start the window loop
revenue_window.mainloop()

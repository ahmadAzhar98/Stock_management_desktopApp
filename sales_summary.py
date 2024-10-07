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

def generate_sales_summary():
    try:
        conn = connection()
        cursor = conn.cursor()
        
        cursor.execute("SELECT DATE(sale_date), SUM(total_sale) FROM sales GROUP BY DATE(sale_date)")
        summary_results = cursor.fetchall()

        result_text.delete(1.0, END)
        result_text.insert(END, "Sales Summary Report\n")
        result_text.insert(END, "Date       | Total Sales\n")
        for date, total_sale in summary_results:
            result_text.insert(END, f"{date.strftime('%Y-%m-%d')} | {total_sale:.2f}\n")

        conn.close()

    except Exception as e:
        result_text.delete(1.0, END)
        result_text.insert(END, f"An error occurred: {e}")

def back_button():
    import sales_and_report
    sales_and_report.open_sales_and_reporting()  

# Create a window for sales summary
summary_window = Tk()
summary_window.title("Sales Summary Report")
summary_window.geometry("800x500")

# Button to generate report
generate_button = Button(summary_window, text="Generate Report", command=generate_sales_summary)
generate_button.pack(pady=20)

# Text widget to display results
result_text = scrolledtext.ScrolledText(summary_window, wrap=WORD, width=100, height=30)
result_text.pack(pady=10)

# Back button
back_button = Button(summary_window, text="Back", command=back_button)
back_button.pack(pady=10)

# Start the window loop
summary_window.mainloop()

from tkinter import *

def open_sales_and_reporting():
    # Create the main window
    main_window = Tk()
    main_window.title("Sales and Reporting")
    main_window.geometry("800x500")  # Width x Height

    # Function to navigate to daily sales report
    def daily_sales():
        main_window.destroy()
        import sales_summary

    # Function to navigate to top selling products
    def top_selling():
        main_window.destroy()
        import top_selling_products

    # Function to navigate to revenue analysis
    def revenue_analysis():
        main_window.destroy()
        import revenue_analysis

    # Function to go back to the home page
    def go_back():
        import home_page
        main_window.destroy()
        home_page.open_home_page()      

    # Create buttons and attach actions
    dailySales = Button(main_window, text="Daily Sales Report", command=daily_sales, width=20, height=2)
    dailySales.pack(pady=10)

    topSelling = Button(main_window, text="Top Selling Products", command=top_selling, width=20, height=2)
    topSelling.pack(pady=10)

    revenueAnalysis = Button(main_window, text="Revenue Analysis", command=revenue_analysis, width=20, height=2)
    revenueAnalysis.pack(pady=10)

    backButton = Button(main_window, text="Back", command=go_back, width=20, height=2)
    backButton.pack(pady=10)

    # Start the Tkinter event loop
    main_window.mainloop()



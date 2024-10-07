from tkinter import *

def open_home_page():
    # Create the home window
    home_window = Tk()
    home_window.title("Home Page")
    home_window.geometry("1000x700")

    # Function to open the add product page
    def add_button():
        # home_window.withdraw() 
        import add_page
        add_page.open_add_products_page()
    
    def delete_button():
        # home_window.destroy()  
        import delete_page
        delete_page.open_delete_products_page()

    def search_button():
        # home_window.destroy()  
        import search_page
        search_page.open_search_products_page()   

    def update_button():
        # home_window.destroy()  
        import update_page
        update_page.open_update_product_page()  
    
    def record_purchase():
        # home_window.destroy()  
        import record_purchase
        record_purchase.open_record_purchase_page() 
    
    def record_return():
        # home_window.destroy()  
        import record_return
        record_return.open_record_return_page()                

    def sales_and_report():
        # home_window.destroy()  
        import sales_and_report
        sales_and_report.open_sales_and_reporting()    

    def logout():
        # home_window.destroy()
        import login
        login.login_window()
        
    def restore():
        import backup
        backup.create_backup_window()  

    # Create buttons
    product_management_button = Button(home_window, text="Add Product", command=add_button, width=20, height=2)
    product_management_button.pack(pady=10)

    deleteButton = Button(home_window, text="Delete Product", command = delete_button, width=20, height=2)
    deleteButton.pack(pady=10)

    updateButton = Button(home_window, text="Update Product", command = update_button , width=20, height=2)
    updateButton.pack(pady=10)

    searchButton = Button(home_window, text="Search Product", command = search_button , width=20, height=2)
    searchButton.pack(pady=10)

    recordPurchase = Button(home_window, text="Record Purchase", command = record_purchase , width=20, height=2)
    recordPurchase.pack(pady=10)

    recordReturn = Button(home_window, text="Record Return", command = record_return , width=20, height=2)
    recordReturn.pack(pady=10)

    restoreDB = Button(home_window, text="Restore Database", command = restore, width=20, height=2)
    restoreDB.pack(pady=10)

    salesReport = Button(home_window, text="Sales & Reporting", command = sales_and_report , width=20, height=2)
    salesReport.pack(pady=10)

    logout_button = Button(home_window, text="Logout", command=logout , width=20, height=2)
    logout_button.pack(pady=10)

    # Start the home window loop
    home_window.mainloop()

# Now you can call open_home_page() to open the home page wherever required.

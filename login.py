from tkinter import *
from tkinter import messagebox
import pymysql

def connection():
    conn = pymysql.connect(
        host='localhost',
        user='root',
        password='',
        db='stock_management'
    )
    return conn

def login_window():
    # Create a login window
    login_window = Tk()
    login_window.title("Login")
    login_window.geometry("768x334")

    # Function to verify login credentials
    def login():
        username = username_entry.get()
        password = password_entry.get()

        if not username or not password:
            messagebox.showwarning("Error", "Please enter both username and password")
            return

        try:
            conn = connection()
            cursor = conn.cursor()
            sql = "SELECT * FROM users WHERE user_name = %s AND password = %s"
            cursor.execute(sql, (username, password))
            result = cursor.fetchone()

            if result:
                messagebox.showinfo("Success", "Login successful")
                login_window.destroy()  # Close the login window
                open_homepage()  # Open main.py
            else:
                messagebox.showerror("Error", "Invalid credentials")

            conn.close()
        except Exception as e:
            messagebox.showerror("Error", f"An error occurred: {e}")

    # Open the main.py (your main application)
    def open_homepage():
        import home_page
        home_page.open_home_page()

    def register_page():
        # login_window.destroy()
        import register
        register.register_window()

    # Labels and entries for the login form
    username_label = Label(login_window, text="Username")
    username_label.pack(pady=10)
    username_entry = Entry(login_window)
    username_entry.pack(pady=10)

    password_label = Label(login_window, text="Password")
    password_label.pack(pady=10)
    password_entry = Entry(login_window, show="*")
    password_entry.pack(pady=10)

    # Login button
    login_button = Button(login_window, text="Login", command=login)
    login_button.pack(pady=20)

    register_button = Button(login_window, text="Register", command=register_page)
    register_button.pack(pady=10)

    # Start the login window loop
    login_window.mainloop()

# To run this script from the command line
if __name__ == "__main__":
    login_window()

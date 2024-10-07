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

def register_window():
    def register():
        first_name = first_name_entry.get()
        last_name = last_name_entry.get()
        username = username_entry.get()
        password = password_entry.get()
        address = address_entry.get()
        
        if not (first_name and last_name and username and password and address):
            messagebox.showwarning("Error", "Please fill in all fields")
            return
        
        try:
            conn = connection()
            cursor = conn.cursor()
            sql = "INSERT INTO users (first_name, last_name, user_name, password, address) VALUES (%s, %s, %s, %s, %s)"
            cursor.execute(sql, (first_name, last_name, username, password, address))
            conn.commit()
            conn.close()
            messagebox.showinfo("Success", "Registration successful")
            register_win.destroy()  # Close the registration window
            
            # Open login window after successful registration
            open_login_screen()
        except Exception as e:
            messagebox.showerror("Error", f"An error occurred: {e}")

    def open_login_screen():
        import login
        login.login_window()

    def back():
        register_win.destroy()
        import login
        login.login_window()

    # Create the registration window
    register_win = Tk()
    register_win.title("Register")
    register_win.geometry("768x500")

    # Registration form labels and entries
    first_name_label = Label(register_win, text="First Name")
    first_name_label.pack(pady=5)
    first_name_entry = Entry(register_win)
    first_name_entry.pack(pady=5)

    last_name_label = Label(register_win, text="Last Name")
    last_name_label.pack(pady=5)
    last_name_entry = Entry(register_win)
    last_name_entry.pack(pady=5)

    username_label = Label(register_win, text="Username")
    username_label.pack(pady=5)
    username_entry = Entry(register_win)
    username_entry.pack(pady=5)

    password_label = Label(register_win, text="Password")
    password_label.pack(pady=5)
    password_entry = Entry(register_win, show="*")
    password_entry.pack(pady=5)

    address_label = Label(register_win, text="Address")
    address_label.pack(pady=5)
    address_entry = Entry(register_win)
    address_entry.pack(pady=5)

    # Register button
    register_button = Button(register_win, text="Register", command=register)
    register_button.pack(pady=20)

    # Back button
    back_button = Button(register_win, text="Back", command=back)
    back_button.pack(pady=20)

    # Start the registration window loop
    register_win.mainloop()

# To call the function and open the registration window
register_window()

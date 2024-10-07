from tkinter import *
from tkinter import messagebox
import pymysql
from tkinter import filedialog
import shutil

def connection():
    conn = pymysql.connect(
        host='localhost',
        user='root',
        password='',
        db='stock_management'
    )
    return conn

def go_back():
    # delete_products_window.destroy()
    import home_page
    home_page.open_home_page()

def backup_database():
    try:
        # Choose the location to save the backup
        file_path = filedialog.asksaveasfilename(defaultextension=".sql",
                                               filetypes=[("SQL files", "*.sql")])
        if not file_path:
            return

        conn = connection()
        cursor = conn.cursor()
        
        # Execute the backup command
        cursor.execute("SHOW TABLES")
        tables = cursor.fetchall()
        
        with open(file_path, 'w') as f:
            for table_name in tables:
                table_name = table_name[0]
                cursor.execute(f"SHOW CREATE TABLE {table_name}")
                create_table_stmt = cursor.fetchone()[1]
                f.write(f"{create_table_stmt};\n\n")

                cursor.execute(f"SELECT * FROM {table_name}")
                rows = cursor.fetchall()
                for row in rows:
                    values = ', '.join(f"'{str(v).replace('\'', '\\\'')}'" for v in row)
                    f.write(f"INSERT INTO {table_name} VALUES ({values});\n")
                f.write("\n")
        
        conn.close()
        messagebox.showinfo("Success", "Database backup completed successfully.")
    
    except Exception as e:
        messagebox.showerror("Error", f"An error occurred during backup: {e}")

def restore_database():
    try:
        # Choose the file to restore from
        file_path = filedialog.askopenfilename(filetypes=[("SQL files", "*.sql")])
        if not file_path:
            return

        # Confirm restoration
        if not messagebox.askyesno("Confirm", "Are you sure you want to restore the database? This will overwrite existing data."):
            return

        conn = connection()
        cursor = conn.cursor()
        
        with open(file_path, 'r') as f:
            sql_script = f.read()
        
        # Execute the SQL script
        cursor.execute("SET foreign_key_checks = 0")  # Disable foreign key checks for restoration
        cursor.execute(sql_script)
        cursor.execute("SET foreign_key_checks = 1")  # Re-enable foreign key checks
        
        conn.commit()
        conn.close()
        messagebox.showinfo("Success", "Database restored successfully.")
    
    except Exception as e:
        messagebox.showerror("Error", f"An error occurred during restoration: {e}")

def create_backup_window():
    backup_window = Toplevel()
    backup_window.title("Database Backup and Restore")
    backup_window.geometry("400x200")

    # Backup button
    backup_button = Button(backup_window, text="Backup Database", command=backup_database)
    backup_button.pack(pady=20)

    # Restore button
    restore_button = Button(backup_window, text="Restore Database", command=restore_database)
    restore_button.pack(pady=20)
    
    # Close button
    close_button = Button(backup_window, text="Back", command= go_back)
    close_button.pack(pady=10)

# Example usage
# Uncomment the following line to create the backup window:
# create_backup_window()

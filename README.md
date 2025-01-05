# Stock Management App
This is a desktop application for stock management build in Python.

# Prerequisite
Database must be already created and its optional that the db is populated.

# Intructions 
1 - Install Tkinter GUI
brew install python-tk

2 - Install the dependency
pip install PyMySQL==1.1.1

3 - Change your database credentials.
go to login.py then connection function

    conn = pymysql.connect(
        host='localhost',
        user='<your username>',
        password='<your password>',
        db='<your database>'
    )
    
4 - Run the application from your CLI
python3 login.py 

# User Interface

![Picture 1](https://github.com/user-attachments/assets/e2e6a038-0287-4eaa-bde7-6e6001225376)

![Picture 2](https://github.com/user-attachments/assets/85087f94-0fd7-43b7-a6a8-777220336b31)

![Picture 3](https://github.com/user-attachments/assets/8ec86470-78e7-4c0e-a740-440d023fcd22)


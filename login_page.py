import sqlite3
import time
import pandas as pd
import sys
import getpass
import os

toolbar_width = 40

# used sqlite to create new database connection
con = sqlite3.connect('empDB.sqlite')

# probe function will draw a progress bar

u_name = ""
Emp_ID = ""
pwd = ""
Emp_Name = ""
Emp_Age = ""
Emp_Qualification = ""
Emp_Salary = ""
Emp_Dept = ""


def probe():
    # setup toolbar
    sys.stdout.write("[%s]" % (" " * toolbar_width))
    sys.stdout.flush()
    sys.stdout.write("\b" * (toolbar_width+1)) # return to start of line, after '['

    for i in range(toolbar_width):
        time.sleep(0.1) # do real work here
        # update the bar
        sys.stdout.write("-")
        sys.stdout.flush()

    sys.stdout.write("]\n") # this ends the progress bar


def createdb():
    try:
        qry = """
            CREATE TABLE USER_DB
            (Emp_ID varchar(20) PRIMARY KEY NOT NULL, employee_name varchar(30) NOT NULL, emp_age Int(2) NOT NULL, 
            Qualification varchar(20) NOT NULL, Salary int NOT NULL, Dept varchar(20) NOT NULL,
             username varchar(20) NOT NULL, password varchar(8) NOT NULL);"""
        # global con
        # con = sqlite3.connect('mydb.sqlite')
        con.execute(qry)
        con.commit()

    except:
        print("database is online")
    login()


def start_pro():
    os.system("cls")
    print("-" * 75)
    print("""
                    Welcome to X_one Employee Database
                            Management System

            Kindly Select the options from below list.
                1) New Employee data creation
                2) Employee Database
                3) Exit

            """)
    # login()
    choice = int(input(">> "))
    if choice == 1:
        insert_data()
    elif choice == 2:
        validate_u()
        # login()
    else:
        exit()
    print("-" * 75)
# accepts inputs from user


def after_login_screen():
    os.system("cls")
    print("""
                    Welcome to x_one Employee Database
                            Management System
            User: {}    
            Kindly Select the options from below list.
                1) insert new Employee
                2) update record
                3) Delete record
                4) View records
                5) Exit

            """.format(u_name))

    choice = int(input(">> "))

    if choice == 1:
        insert_data()
    elif choice == 2:
        update_data()
    elif choice == 3:
        del_records()
    elif choice == 4:
        checklog()


        # after_login_screen()
    else:
        start_pro()
    print("-" * 75)


def inilog():
    print("-"*75)

    global u_name
    global Emp_ID
    global pwd
    global Emp_Name
    global Emp_Age
    global Emp_Qualification
    global Emp_Salary
    global Emp_Dept

    Emp_ID = int(input("Employee ID: "))
    Emp_Name = str(input("Employee Name: "))
    Emp_Age = int(input("Employee Age: "))
    Emp_Qualification = str(input("Employee Qualification: "))
    Emp_Salary = int(input("Employee Salary: "))
    Emp_Dept = str(input("Employee Department: "))
    u_name = str(input("Username: "))
    # pwd= str(input("Password: "))
    pwd = getpass.getpass()
    # print(pwd)
    print("-" * 75)
    return Emp_ID, Emp_Name, Emp_Age, Emp_Qualification, Emp_Salary, Emp_Dept, u_name, pwd


def update_data():
    # checklog()
    # inilog()
    stmt = "select * from USER_DB"
    db = con.execute(stmt)
    rs = db.fetchall()

    # print(db.description[0])
    Emp_ID = input("Enter Employee ID to update the records.")
    jf = pd.DataFrame(rs, columns=[x[0] for x in db.description])
    print(jf)
    # print(Emp_ID)
    # print(jf.get('Emp_ID'))
    if Emp_ID in jf.values:
        # print("inside if")
        Emp_Name = str(input("Employee Name: "))
        Emp_Age = int(input("Employee Age: "))
        Emp_Qualification = str(input("Employee Qualification: "))
        Emp_Salary = int(input("Employee Salary: "))
        Emp_Dept = str(input("Employee Department: "))
        u_name = str(input("Username: "))
        # pwd= str(input("Password: "))
        pwd = getpass.getpass()

        in_data = [Emp_Name, Emp_Age, Emp_Qualification, Emp_Salary, Emp_Dept, u_name, pwd, Emp_ID]
        stmt = "update USER_DB set employee_name = ?,emp_age = ?, Qualification = ?, Salary =? , Dept = ?, username=?, password=? where Emp_ID=? ;"
        con.execute(stmt, in_data)
        con.commit()
        exit_plan()
    else:
        print("inside else")


def exit_plan():
    for i in range(0, 3):
        ch = input("Do you want to exit?")
        ch.lower()
        if ch == "y" or ch=="yes":
            start_pro()
        elif ch == "n" or ch =="no":
            after_login_screen()
        else:
            print("invalid response")
            continue

def insert_data():
    inilog()
    print("Updating new data into the db")
    in_data = [Emp_ID, Emp_Name, Emp_Age, Emp_Qualification, Emp_Salary, Emp_Dept, u_name, pwd]
    print(in_data)
    stmt = "insert into USER_DB values (?,?,?,?,?,?,?,?);"
    con.execute(stmt, in_data)
    con.commit()
    probe()
    print("db updated!")
    # exit_plan()


def checklog():
    stmt = "select * from USER_DB"
    db = con.execute(stmt)
    rs = db.fetchall()
    # global in_data
    # in_data = [u_name]
    print("Fetching user details")
    probe()
    print(pd.DataFrame(rs, columns=[x[0] for x in db.description]))
    exit_plan()

def login():
    global u_name
    global pwd
    print("Kindly Enter your username and password to login.")
    u_name = str(input("Username: "))
    pwd = getpass.getpass()
    # validate_u()
    start_pro()
    return u_name, pwd



def validate_u():
    # inilog()
    # login()
    # print(u_name)
    in_data = [u_name]
    # print(in_data)
    probe()

    c = con.cursor()
    # print(in_data)
    f1 = c.execute("select * from USER_DB where username = ?", in_data)
    rs = f1.fetchall()

    try:

        if u_name == rs[0][6] and pwd == rs[0][7]:
            print("\n User Found!!")
            after_login_screen()

        else:
            print("invalid username password!")
            # print("{0} attempts are remaining".format(i))
    except IndexError:
        print("User not available in the system. Try creating new user.")


def del_records():
    global Emp_ID
    print("Kindly enter the Employee ID of the record which needs to be deleted.")
    Emp_ID= input("Employee ID: ")
    c = con.cursor()
    # print(in_data)

    stmt = "select * from USER_DB"
    db = con.execute(stmt)
    rs = db.fetchall()

    # print(db.description[0])

    jf = pd.DataFrame(rs, columns=[x[0] for x in db.description])
    # print(Emp_ID)
    # print(jf.get('Emp_ID'))
    if Emp_ID in jf.values:
        f1 = c.execute("delete from USER_DB where Emp_ID= ?", Emp_ID)
    else:
        print("Invalid Employee ID: ", Emp_ID)

    checklog()
    exit_plan()



# insert_data()
createdb()
# checklog()
#
# u = [input("username: ")]
# # stmt = r"'"
# # print(u)
# db= con.execute("select password from userdb where username = ?",(u))
# c = con.cursor()
# db = c.execute("select * from user_db")
# rs = db.fetchall()
# print(rs)


# stmt = "select * from USER_DB"
# db = con.execute(stmt)
# rs = db.fetchall()
# print(pd.DataFrame(rs, columns=[x[0] for x in db.description]))
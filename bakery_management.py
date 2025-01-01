import mysql.connector
from datetime import datetime

# Establishing the connection
con = mysql.connector.connect(host="localhost", user="root", password="sona17")
cur = con.cursor()

# Creating the database and tables
cur.execute("CREATE DATABASE IF NOT EXISTS items")
cur.execute("USE items")
cur.execute("CREATE TABLE IF NOT EXISTS cs(sno INT, products VARCHAR(20), cost INT)")

# Inserting initial data into cs table if empty
cur.execute("SELECT * FROM cs")
res = cur.fetchall()
if not res:
    cur.execute("INSERT INTO cs VALUES (1, 'CAKE', 50)")
    cur.execute("INSERT INTO cs VALUES (2, 'PASTRY', 20)")
    cur.execute("INSERT INTO cs VALUES (3, 'MILK', 60)")
    cur.execute("INSERT INTO cs VALUES (4, 'BUTTER', 20)")
    cur.execute("INSERT INTO cs VALUES (5, 'CHEESE', 30)")
    con.commit()

cur.execute("CREATE TABLE IF NOT EXISTS vip(sno INT, varieties VARCHAR(20))")
cur.execute("SELECT * FROM vip")
res = cur.fetchall()
if not res:
    cur.execute("INSERT INTO vip VALUES (1, 'VANILLA')")
    cur.execute("INSERT INTO vip VALUES (2, 'CHOCOLATE')")
    cur.execute("INSERT INTO vip VALUES (3, 'STRAWBERRY')")
    cur.execute("INSERT INTO vip VALUES (4, 'BUTTER-SCOTCH')")
    con.commit()

cur.execute("CREATE TABLE IF NOT EXISTS worker(sno INT, Name VARCHAR(20), Salary INT)")
cur.execute("SELECT * FROM worker")
res = cur.fetchall()
if not res:
    cur.execute("INSERT INTO worker VALUES (1, 'MUKESH', 12365)")
    cur.execute("INSERT INTO worker VALUES (2, 'RAM', 1235)")
    cur.execute("INSERT INTO worker VALUES (3, 'SURESH', 25634)")
    cur.execute("INSERT INTO worker VALUES (4, 'RAJU', 6352)")
    con.commit()

print("|...........................WELCOME.........................|")
print("|..............................TO...........................|")
print("|....................BAKERY MANAGEMENT SYSTEM...............|")

ch = ''
while ch != 'N' and ch != 'n':
    print("\n\n PLEASE CHOOSE\n 1. FOR ADMIN\n 2. FOR CUSTOMER\n 3. FOR EXIT:\n")
    choice = int(input("ENTER YOUR CHOICE: "))
    
    if choice == 1:
        admin = input("USERNAME: ")
        password = int(input("ENTER PASSWORD: "))
        if password == 1234:
            print("HELLO SIR YOU LOGGED IN AS ADMIN SUCCESSFULLY")
            print("Press 1 TO ADD ITEM: ")
            print("Press 2 TO SEE ITEMS: ")
            print("Press 3 TO UPDATE COST OF THE ITEM: ")
            print("Press 4 TO ADD VARIETIES OF CAKE: ")
            print("Press 5 TO ADD WORKER: ")
            print("Press 6 TO SEE WORKER: ")
            print("Press 7 TO UPDATE SALARY: ")
            
            c = int(input("ENTER YOUR CHOICE: "))
            if c == 1:
                def add():
                    sno = int(input("ENTER SNO: "))
                    product1 = input("ENTER PRODUCT NAME: ")
                    cost = int(input("ENTER COST: "))
                    d1 = (sno, product1, cost)
                    s1 = 'INSERT INTO cs VALUES (%s, %s, %s)'
                    cur.execute(s1, d1)
                    con.commit()
                    print("ADDED SUCCESSFULLY")
                add()
            elif c == 2:
                def items():
                    print("ITEMS IN THE SHOP: ")
                    sql = "SELECT * FROM cs"
                    cur.execute(sql)
                    res = cur.fetchall()
                    for serial_no, products, cost in res:
                        print(serial_no, ":", "\t", products, ":\t\t", 'cost', cost)
                items()
            elif c == 3:
                def money():
                    sno = input("Enter the sno of product: ")
                    n_cost = int(input("Enter the Rupees to be added: "))
                    cur.execute("UPDATE cs SET cost = cost + %s WHERE sno = %s", (n_cost, sno))
                    con.commit()
                    print("TABLE AFTER UPDATION:")
                    sq = "SELECT * FROM cs"
                    cur.execute(sq)
                    res = cur.fetchall()
                    for sno, products, cost in res:
                        print(sno, ":", "\t", products, ":\t", cost)
                money()
            elif c == 4:
                def variety():
                    sno = int(input("Enter sno: "))
                    varieties = input("Enter variety: ")
                    d2 = (sno, varieties)
                    s2 = 'INSERT INTO vip VALUES (%s, %s)'
                    cur.execute(s2, d2)
                    con.commit()
                    print("VARIETY ADDED SUCCESSFULLY")
                variety()
            elif c == 5:
                def add_worker():
                    sno = int(input("Enter sno: "))
                    emp = input("Enter name: ")
                    salary = int(input("Enter the salary: "))
                    dx = (sno, emp, salary)
                    sy = 'INSERT INTO worker VALUES (%s, %s, %s)'
                    cur.execute(sy, dx)
                    con.commit()
                    print("WORKER ADDED SUCCESSFULLY")
                add_worker()
            elif c == 6:
                def workers():
                    print("Workers in the shop:")
                    sql = "SELECT * FROM worker"
                    cur.execute(sql)
                    res = cur.fetchall()
                    for sno, name, salary in res:
                        print(sno, ":", "\t", name, ":\t", salary)
                workers()
            elif c == 7:
                def update_salary():
                    print("Choose 1 to increase the salary:")
                    print("Choose 2 to decrease:")
                    name = input("Enter the name of EMPLOYEE: ")
                    n_salary = int(input("Enter the Rupees to be added: "))
                    sig = int(input("Enter choice (1/2): "))
                    if sig == 1:
                        cur.execute("UPDATE worker SET salary = salary + %s WHERE Name = %s", (n_salary, name))
                        con.commit()
                        print("TABLE AFTER UPDATION:")
                        sq = "SELECT * FROM worker"
                        cur.execute(sq)
                        res = cur.fetchall()
                        for sno, name, salary in res:
                            print(sno, ":", "\t", name, ":\t", salary)
                    elif sig == 2:
                        cur.execute("UPDATE worker SET salary = salary - %s WHERE Name = %s", (n_salary, name))
                        con.commit()
                        print("TABLE AFTER UPDATION:")
                        sq = "SELECT * FROM worker"
                        cur.execute(sq)
                        res = cur.fetchall()
                        for sno, name, salary in res:
                            print(sno, ":", "\t", name, ":\t", salary)
                update_salary()
            else:
                print("SORRY.. You have entered the Wrong Input, Input From 1 to 7")
        else:
            print("WRONG PASSWORD")
    
    elif choice == 2:
        name = input("Enter your name: ")
        phone = int(input("Enter your phone number: "))
        print('Press 1 to see the MENU')
        print('Press 2 to order an item')
        c = int(input('Enter your choice: '))
        if c == 1:
            def items():
                print("Items in the shop:")
                sql = "SELECT * FROM cs"
                cur.execute(sql)
                res = cur.fetchall()
                for serial_no, products, cost in res:
                    print(serial_no, ":", "\t", products, ":\t", cost)
            items()
        elif c == 2:
            print("What do you want to order?")
            sql = "SELECT * FROM cs"
            cur.execute(sql)
            res = cur.fetchall()
            for serial_no, products, cost in res:
                print(serial_no, ":", "\t", products, ":\t", cost)
            d = int(input("Enter your Serial No of the Item to Buy: "))
            qty = int(input("Enter Quantity: "))
            cur.execute("SELECT cost FROM cs WHERE sno = %s", (d,))
            cost = cur.fetchone()[0]
            total_amount = qty * cost
            print("\nYOUR BILL")
            print("CUSTOMER NAME: ", name)
            print("CONTACT NUMBER: ", phone)
            print("ITEM: ", d)
            print("QUANTITY: ", qty)
            print("TOTAL AMOUNT: ", total_amount)
            print("THANK YOU FOR ORDERING")
            print("Date: ", datetime.now())
        else:
            print("WRONG ANSWER")
    
    ch = input("DO YOU WANT TO CONTINUE? (Y/N): ")
    
con.close()
               

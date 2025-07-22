import sqlite3
#Creating a database (atm.db).
conn=sqlite3.connect("atm.db")
cur=conn.cursor()

#Creating a table (accounts).
cur.execute('''
create table if not exists accounts(acc integer primary  key autoincrement, name text, pin integer, balance real)
''')
conn.commit()

#Creating a Account.
def create(name,pin, balance):
    cur.execute("insert into accounts(name, pin, balance) values (?,?,?)",(name, pin, balance))
    conn.commit()
    # print("Account created successfully!!")
create("Arpit",2025,4500000)

#Login the account.
def login(acc,pin):
    cur.execute("select * from accounts where acc=? and pin=?", (acc,pin))
    user=cur.fetchone()
    if user:
        print("Hello",user[1])
        return user
    else:
        print("Invalid user or pin.")
        return None

#Check the balance.
def bal(acc):
    cur.execute("select  balance from accounts where acc=?",(acc,))
    balance=cur.fetchone()
    print("Your current balance is:",balance[0])

#Deposit into the account.
def dep(acc,amt):
    cur.execute("update accounts set balance = balance+ ? where acc=?",(amt,acc))
    conn.commit()
    print("Balance updated!!")

#Withdrawl money.
def wid(acc,amt):
    cur.execute("select balance from accounts where acc= ?",(acc,))
    balance= cur.fetchone()[0]
    if balance < amt:
        print("Insufficient balance!")
    else:
        cur.execute("update accounts set balance= balance-? where acc=?",(amt,acc))
        conn.commit()
        print("Balance updated!")

#MAIN
print("======Welcome to ATM Simulator======")
acc=int(input("Enter your account number:"))
pin=int(input("Enter your pin:"))

user=login(acc,pin)
if not user:
    exit()

while True:
    print("""     ====MENU====
    Enter 1 to check your balance
    Enter 2 to deposit the money
    Enter 3 to withdrawl money
    Enter 4 to Exit!!
    """)
    a=int(input())
    if a== 1:
        bal(acc)
    elif a==2:
        amt=int(input("Enter amount to deposit:"))
        dep(acc,amt)
    elif a==3:
        amt=int(input("Enter amount to withdrawl:"))
        wid(acc,amt)
    elif a==4:
        print("<<<EXITING>>>")
        break
    else:
        print("!!!INVALID INPUT!!!")


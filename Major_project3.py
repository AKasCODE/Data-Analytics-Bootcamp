import sqlite3
conn=sqlite3.connect("library.db")  #Establishing connection to 'library.db'.
cur=conn.cursor()

cur.execute("CREATE TABLE IF NOT EXISTS books(bid INTEGER PRIMARY KEY AUTOINCREMENT, name TEXT, author TEXT, price INTEGER, quantity INTEGER)")
conn.commit()

cur.execute("CREATE TABLE IF NOT EXISTS record(id INTEGER PRIMARY KEY AUTOINCREMENT, bid INTEGER, user TEXT, issue_date TEXT, return_date TEXT)")
conn.commit()

#Add book in library stock.
def add(name, author, price, quantity):
    cur.execute("INSERT INTO books(name, author, price, quantity) VALUES(?,?,?,?)",(name, author,price, quantity))
    conn.commit()

#Issue a book
def issue(bid, user, date):
    cur.execute("SELECT quantity FROM books WHERE bid=?", (bid,))
    a=cur.fetchone()
    if a[0]<1:
        print("BOOK OUT OF STOCK!!")
    else:
        cur.execute("UPDATE books SET quantity= quantity-1 WHERE bid=?",(bid,))
        cur.execute("INSERT INTO record(bid, user, issue_date) VALUES (?,?,?)",(bid, user, date))
        conn.commit()
        print("Book issued!")

#Return a book
def retur(id,date):
    cur.execute("SELECT bid FROM record WHERE id=?",(id,))
    a=cur.fetchone()
    cur.execute("UPDATE books SET quantity= quantity+1 WHERE bid = ?", (a[0],))
    cur.execute("UPDATE record SET return_date=? WHERE id = ?", (date,id))
    conn.commit()
    print("Book returned.")

#Show available books.
def show():
    cur.execute("SELECT * FROM books")
    bk=cur.fetchall()
    print(">>>AVAILABLE BOOKS<<<")
    for i in bk:
        print(f"ID: {i[0]}\t Name: {i[1]}\t Author: {i[2]}\t Price: {i[3]}\t Quantity: {i[4]}")

#Show record of issue and return. 
def rec():
    cur.execute("SELECT * FROM record")
    bk=cur.fetchall()
    print(">>>>>>RECORD<<<<<<")
    for i in bk:
        print(f"ID: {i[0]}\t Book Id: {i[1]}\t User: {i[2]}\t Issue Date: {i[3]}\t Return Date: {i[4]}")

print("======WELCOME TO LIBRARY MANAGEMENT SYSTEM======")
while True:
    print('''
    Enter 1 to add book
    Enter 2 to see books
    Enter 3 to issue book
    Enter 4 to return book
    Enter 5 to see records
    Enter 6 to exit!! 
    ''')
    a=int(input("Enter:"))
    
    if a==1:
        n=input("Enter book name:")
        au=input("Enter author name:")
        p=int(input("Enter price:"))
        q=int(input("Enter quantity:"))
        add(n, au, p, q)
    elif a==2:
        show()
    elif a==3:
        i=int(input("Enter book Id:"))
        u=input("Enter user name:")
        d=input("Enter issue date:")
        issue(i, u, d)
    elif a==4:
        i=int(input("Enter issue Id:"))
        rd=input("Enter return date:")
        retur(i,rd)
    elif a==5:
        rec()
    elif a==6:
        print("Thanks for visiting!")
        break
    else:
        print("INVALID INPUT!!!")
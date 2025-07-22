import sqlite3
conn=sqlite3.connect("bill.db")  #Establishing connection to 'bill.db'.
cur=conn.cursor()

cur.execute("CREATE TABLE IF NOT EXISTS product(pid INTEGER PRIMARY KEY AUTOINCREMENT, name TEXT, price INTEGER)")
conn.commit()

cur.execute("CREATE TABLE IF NOT EXISTS cart(cid INTEGER PRIMARY KEY AUTOINCREMENT, pid INTEGER, Quantity INTEGER)")
conn.commit()

#Function to add product.
def add_pro(name,price):
    cur.execute("INSERT INTO product(name,price) VALUES(?,?)",(name,price))
    conn.commit()
    print("Item created successfully.")

add_pro("Black_pen",20)
add_pro("Blue_pen",20)
add_pro("Pencil",10)
add_pro("Eraser",5)
add_pro("sharpner",5)

#Function to see available products.
def show_pro():
    cur.execute("SELECT * FROM product")
    item=cur.fetchall()
    print("---AVAILABLE PRODUCTS---")
    print("P_id\t Name\t Price")
    for i in item:
        print(f"Id: {i[0]}\t Name:{i[1]}\t Price: {i[2]}")

#Function to add item to cart.
def add_car(pid,quantity):
    cur.execute("INSERT INTO cart(pid,quantity) VALUES(?,?)",(pid,quantity))
    conn.commit()
    print("Item added to the cart successfully")

#Genrate bill
def gen():
    cur.execute("""SELECT product.name, product.price, cart.quantity, (product.price*cart.quantity)
    FROM cart JOIN product ON cart.pid=product.pid 
    """)
    item=cur.fetchall()
    grand=0
    print(">>>>>YOUR BILL<<<<<")
    for i in item:
        print(f"Name: {i[0]}\t Price: {i[1]}\t Quantity: {i[2]}\t Total: {i[3]}")
        grand+= i[3]
    print("Grand Total:",grand)

#Clear the cart
def clear():
    cur.execute("DELETE FROM cart")
    conn.commit()
    print("Cart cleared.")

#Remove item from the cart.
def rem(pid):
    cur.execute("DELETE FROM cart WHERE pid=?",(pid,))
    conn.commit()
    print("Item removed from cart.")


print("======WELCOME TO BILL SIMULATOR======")
while True:
    show_pro()
    print("""     ====MENU====
    Enter 1 to add new product
    Enter 2 to add item to the cart
    Enter 3 to view bill
    Enter 4 to clear cart      
    Enter 5 to remove item from the cart
    Enter 6 to Exit!!
    """)
    a=int(input("Enter:"))

    if a==1:
        n=input("Enter name:")
        p=int(input("Enter price:"))
        add_pro(n,p)
    elif a==2:
        i=int(input("Enter product id:"))
        q=int(input("Enter quantity:"))
        add_car(i,q)
    elif a==3:
        gen()
    elif a==4:
        clear()
    elif a==5:
        i=int(input("Enter id of the product to remove:"))
        rem(i)
    elif a==6:
        print("Thanks for visiting!!")
        break
    else:
        print("Invalid Input!!!")

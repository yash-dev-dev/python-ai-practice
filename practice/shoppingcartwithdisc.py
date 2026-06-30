total=0
cart=[]
n=int(input("enter num of items"))
for i in range(n):
    name=input("enter item name")
    price=int(input("enter price of the item"))
    cart.append((name,price))

def view_cart():
    print(f"{cart}")

def checkout():
    global total
    for name,price in cart:
        total=total+price
    if total>1000:
     disc=total*(10/100)   
     total=total-disc
    elif total>500:
     disc=total*(20/100)
     total=total-disc

def bill():
    view_cart()
    checkout()
    print(f"the total final bill is ${total}")
bill()

products = {
    "apple" : 50,
    "banana": 100,
    "chips" : 80,
    "bread":  30,
    "juice": 150}
cart = []
def show_products():
    print("\n products")
    for item, price in products.items():
        print(item, "=", price)

def add_products():
    item = input("enter product name :")
    if item in products:
        cart.append(item)
        print(item, "added to cart")
    else:
        print("product not found")
def show_cart():
    print("your cart ")
    total = 0
    for item in cart:
        print(item, "=", products[item])
        total = total + products[item]
    print("total =", total)

while True:
    print( "1. show products")
    print("2. add product to cart")
    print("3. view cart")
    print("4. Exit")
    choice = input("Enter your choice:")
    if choice == "1":
        print("showing products ...")
        show_products()
            
    elif choice == "2":
        print("Adding product...")
        add_products()
            
    elif choice == "3":
        print("showing cart ...")
        show_cart()
            
    elif choice == "4":
        print("Thank you!")
        break
    else:
        print("Invalid choice! please try again")

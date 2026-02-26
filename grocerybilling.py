grocery = {}
n = int(input("Enter number of items: "))

for _ in range(n):
    name = input("Item name: ")
    price = float(input("Price: "))
    qty = int(input("Quantity: "))
    grocery[name] = {"price": price, "quantity": qty}

total = sum(item["price"] * item["quantity"] for item in grocery.values())

print("Total Bill:", total)

if total > 1000:
    total *= 0.9

print("Final Amount:", total)
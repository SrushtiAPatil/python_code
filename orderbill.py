orders = []

n = int(input("Enter number of items ordered: "))

for i in range(n):
    item = input("Item name: ")
    price = float(input("Price: "))
    qty = int(input("Quantity: "))
    
    order = {
        "item": item,
        "details": (price, qty)
    }
    orders.append(order)

print("\n🍔 Canteen Bill")
total = 0
for o in orders:
    price, qty = o["details"]
    cost = price * qty
    total += cost
    print(o["item"], "→ ₹", cost)

print("Total Amount to Pay: ₹", total)

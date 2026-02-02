lst = []

n = int(input("Enter number of elements: "))
for i in range(n):
    lst.append(int(input(f"Enter element {i+1}: ")))

print("\nOriginal List:", lst)

lst.insert(1, 99)
print("After insert(1,99):", lst)

lst.append(50)
print("After append(50):", lst)

lst.extend([70, 80])
print("After extend([70,80]):", lst)

lst.remove(50)
print("After remove(50):", lst)

lst.pop()
print("After pop():", lst)

print("Index of 99:", lst.index(99))
print("Count of 99:", lst.count(99))

lst.sort()
print("After sort():", lst)

lst.reverse()
print("After reverse():", lst)

print("Max:", max(lst))
print("Min:", min(lst))
print("Sum:", sum(lst))
print("Length:", len(lst))

lst.clear()
print("After clear():", lst)

name_to_search = input("Enter name to search: ")

found = False
with open("students.txt", "r") as f:
    for line in f:
        name, marks = line.strip().split(",")
        if name == name_to_search:
            print(f"Found: {name} → {marks}")
            found = True
            break

if not found:
    print("Student not found")

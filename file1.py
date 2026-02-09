delete_name = input("Enter name to delete: ")

with open("students.txt", "r") as f:
    lines = f.readlines()

with open("students.txt", "w") as f:
    for line in lines:
        name, marks = line.strip().split(",")
        if name != delete_name:
            f.write(line)

print("Record deleted (if existed)")

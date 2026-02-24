students = {}

def add_student(id, name):
    students[id] = name

def view_students():
    for id, name in students.items():
        print(id, name)

def delete_student(id):
    students.pop(id, None)

add_student(1, "Amit")
add_student(2, "Priya")

view_students()

delete_student(1)

print("After Delete:")
view_students()
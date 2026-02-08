import pickle


student = {
    "name": "Srushti",
    "age": 21,
    "course": "Computer Engineering"
}


with open("student.pkl", "wb") as file:
    pickle.dump(student, file)

print("Data stored successfully!")

with open("student.pkl", "rb") as file:
    loaded_student = pickle.load(file)

print("Data read from file:")
print(loaded_student)

class Employee:

    def __init__(self, emp_id, name, salary):
        self.emp_id = emp_id
        self.name = name
        self.salary = salary

    def calculate_salary(self):
        return self.salary


class Manager(Employee):

    def calculate_salary(self):
        bonus = 5000
        return self.salary + bonus


class Developer(Employee):

    def calculate_salary(self):
        bonus = 3000
        return self.salary + bonus


m1 = Manager(101, "Rahul", 40000)
d1 = Developer(102, "Anita", 35000)

print("Manager Salary:", m1.calculate_salary())
print("Developer Salary:", d1.calculate_salary())

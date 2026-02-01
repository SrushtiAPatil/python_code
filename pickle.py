import pickle
with open("data.pickle", "ab") as f:
    ename=input("enter the employee name :")
    age = input("enter the employee age :")
    salary = input("enter the employee salary :")
    lst=[]
    lst.append(ename)
    lst.append(age)
    lst.append(salary)
    pickle.dump(lst, f)
    print(" Employee details saved successfully")

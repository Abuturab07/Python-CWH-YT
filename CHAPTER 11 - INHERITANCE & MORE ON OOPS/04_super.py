class Employee:
    def __init__(self):
        print("Constructor of Employee")
    a = 1

class Programmer(Employee):
    def __init__(self):
        print("Constructor of Programmer")
    b = 2

class Manager(Programmer):
    def __init__(self):
        super().__init__()
        print("Constructor of Manager")
    c = 3

# o = Employee() # Prints the attribute 
# print(o.a) # Prints the attribute
# # print(o.b) # Shows an error because there is no b attribute in employee class

# o = Programmer()
# print(o.a, o.b)

o = Manager()
print(o.a, o.b, o.c)
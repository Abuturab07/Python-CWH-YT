class Employee:
    a = 1

class Programmer(Employee):
    b = 2

class Manager(Programmer):
    c = 3

o = Employee() # Prints the attribute 
print(o.a) # Prints the attribute
# print(o.b) # Shows an error because there is no b attribute in employee class

o = Programmer()
print(o.a, o.b)

o = Manager()
print(o.a, o.b, o.c)
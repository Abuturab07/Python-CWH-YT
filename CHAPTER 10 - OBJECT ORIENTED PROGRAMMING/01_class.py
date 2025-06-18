# A class is a blueprint for creating object

class Employee:
    language = "Python"  # This is a class attribute
    salary = 120000

harry = Employee()
harry.name = "Harry"  # This is an instance attribute
print(harry.name, harry.language)

imam = Employee() #objet
imam.name = "Imam Mohammad Abuturab"
print(imam.salary, imam.name)

# An attribute that belongs to the Instance (object)
# Here name is instance attribute and lanyage and salary are class attributes as they directly belong to the class
class Employee:
    language = "Python"  # This is a class attribute
    salary = 120000

harry = Employee()
harry.language = "JavaScript"  # This is an object attribute
print(harry.salary, harry.language)

# Instance attributes, take preference over class attributes during assignment & retrieval


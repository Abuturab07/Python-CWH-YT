# __init__() is a special method which is first run as soon as the object is created
# __init__() method is also known as constructor
# It takes ‘self’ argument and can also take further arguments

class Employee:
    language = "Python"  
    salary = 120000

    def __init__(self, name, salary, language): # dunder method(means which starts form double underscore), which is automatically called
        self.name = name
        self.salary = salary
        self.language = language
        print("I am creating an object")

    def getInfo(self): 
        print(f"The language is {self.language}. The salary is {self.salary}")

    @staticmethod 
    def greet(self): 
        print("Good morning")

harry = Employee("Harry", 130000, "JavaScript")
# harry.name = "Harry"
print(harry.name, harry.salary, harry.language)

# rohan = Employee()

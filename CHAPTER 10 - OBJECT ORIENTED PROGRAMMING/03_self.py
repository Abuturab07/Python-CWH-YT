class Employee:
    language = "Python"  # This is a class attribute
    salary = 120000

    def getInfo(self): # if self not given then it will give an error
        print(f"The language is {self.language}. The salary is {self.salary}")

    @staticmethod # decorator to mark greet as a static method
    # no need for self 
    # it means we dont need any proerties form object
    def greet(self): 
        print("Good morning")

harry = Employee()
harry.language = "JavaScript"  # This is an object attribute

harry.getInfo() # here self is harry
#OR
Employee.getInfo(harry) # both are same

harry.greet()
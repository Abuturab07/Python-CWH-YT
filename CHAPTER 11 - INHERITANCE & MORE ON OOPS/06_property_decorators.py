class Employee:
    a = 1

    @classmethod # ab instance attribute nhi dikhaega 
    def show(cls):
        print(f"The class attribute of a is {cls.a}")

    @property # getter method 
    def name(self):
        return f"{self.fname} {self.lname}"
    
    @name.setter
    def name(self, value):
        self.fname = value.split(" ")[0]  # split fucthon name to list me split kr deta hai
        self.lname = value.split(" ")[1]


e = Employee()
e.a = 45
e.name = "Harry Khan"
print(e.name)
print(e.fname, e.lname)
e.show()

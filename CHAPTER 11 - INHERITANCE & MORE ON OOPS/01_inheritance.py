class Employee:
    company = "ITC"
    name = "Default name"
    def show(self):
        print(f"The name of the employee is {self.name} and salary is {self.salary}")


class Programmer(Employee):
    company = "ITC Infotech"
    def showLanguage(self):
        print(f"The company name is {self.company} and he is good with {self.language} language")

a = Employee()
b = Programmer()

print(a.company, b.company)

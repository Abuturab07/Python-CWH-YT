class Programmer:
    company = "Microsoft"

    def __init__(self, name, salary, pin):
        self.name = name
        self.salary = salary
        self.pin = pin


p = Programmer("Harry", 120000, 241001)
print(p.name, p.company, p.salary, p.pin)
I = Programmer("Imam", 999999, 694200)
print(I.name, I.company, I.salary, I.pin)

class calculator:
    def __init__(self, n):
        self.n = n
        
    def square(self):
        print(f"The square is {self.n*self.n}")
    def cube(self):
        print(f"The cube is {self.n*self.n*self.n}")
    def sqroot(self):
        print(f"The square root is {self.n**1/2}")
p = calculator(4)
p.square()
p.cube()
p.sqroot()

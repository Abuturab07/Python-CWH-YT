class TowDVector:
    def __init__(self, i, j):
        self.i = i
        self.j = j

    def show(self):
        print(f"Vector is {self.i}i + {self.j}j")

class ThreeDVector(TowDVector):
    def __init__(self, i, j, k):
        super().__init__(i, j)
        self.k = k

    def show(self):
        print(f"Vector is {self.i}i + {self.j}j + {self.k}k")

a = TowDVector(1, 2)
a.show()
b = ThreeDVector(5, 2, 3)
b.show()
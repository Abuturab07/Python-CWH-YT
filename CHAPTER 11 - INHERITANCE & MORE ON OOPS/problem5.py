class Vector:
    def __init__(self, components):
        self.components = components  # List representing vector components
        self.n = len(components)  # Dimension of the vector

    def __add__(self, other):
        if self.n != other.n:
            raise ValueError("Vectors must have the same dimensions for addition.")
        return Vector([self.components[i] + other.components[i] for i in range(self.n)])

    def __mul__(self, other):
        if self.n != other.n:
            raise ValueError("Vectors must have the same dimensions for dot product.")
        return sum(self.components[i] * other.components[i] for i in range(self.n))

    def __str__(self):
        return f"Vector({self.components})"


# Example usage:
v1 = Vector([1, 2, 3])
v2 = Vector([4, 5, 6])

# Vector addition
print(v1 + v2)  # Output: Vector([5, 7, 9])

# Dot product
print(v1 * v2)  # Output: 32  (1*4 + 2*5 + 3*6 = 4 + 10 + 18)

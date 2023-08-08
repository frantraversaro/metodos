import matplotlib.pyplot as plt
import numpy as np


# Ejemplo vector de 2 dimensiones

class Vector2D:
    def __init__(self, x, y):
        self.x = x
        self.y = y

    def __add__(self, other):
        if not isinstance(other, Vector2D):
            raise ValueError("Unsupported!!")
        else:
            return Vector2D(self.x + other.x, self.y + other.y)

    def __mul__(self, value):
        if not isinstance(value, (int, float)):
            raise ValueError('Unsupported!!')
        else:
            return Vector2D(self.x * value, self.y * value)

    def __rmul__(self, value):
        return self * value

    def __repr__(self):
        return f"Vector2D({self.x},{self.y})"


class Vector3D:
    def __init__(self, x, y, z):
        self.x = x
        self.y = y
        self.z = z

    def __add__(self, other):
        if not isinstance(other, Vector3D):
            raise ValueError("Unsupported!!")
        else:
            return Vector3D(self.x + other.x, self.y + other.y, self.z + other.z)

    def __mul__(self, value):
        if not isinstance(value, (int, float)):
            raise ValueError('Unsupported!!')
        else:
            return Vector3D(self.x * value, self.y * value, self.z * value)

    def __rmul__(self, value):
        return self * value

    def __repr__(self):
        return f"Vector3D({self.x},{self.y}, {self.z})"


## Para Implementar en clase

class Vector:
    def __init__(self, components: list):
        # initialize vector
        self.components = components
        self.dimension = None  # (hint: you are going to need the dimension of the vector here!)


    def __eq__(self, other):
        return self.components == other.components

    def __add__(self, other):
        if not isinstance(other, Vector):
            raise ValueError("Unsupported!!")
        elif self.dimension != other.dimension:
            raise ValueError("Vector must have the same dimensions to be summed")
        else:
            # Implement the sum
            pass

    def __mul__(self, value):
        if not isinstance(value, (int, float)):
            raise ValueError('Unsupported!!')
        else:
            # Implement scalar multiplication
            pass

    def __rmul__(self, value):
        return self * value

    def __repr__(self):
        # Implement the representation
        pass



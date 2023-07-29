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
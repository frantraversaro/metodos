class Vector:
  def __init__(self, components:list):
    self.components = components
    self.dimension = len(components)

  def __eq__(self, other):
      return self.components == other.components

  def __add__(self, other):
    if not isinstance(other, Vector):
      raise ValueError("Unsupported!!")
    elif self.dimension != other.dimension:
      raise ValueError("Vector must have the same dimensions to be summed")
    else:
      return Vector([i+j for i,j in zip(self.components, other.components)])

  def __mul__(self, value):
    if not isinstance(value, (int, float)):
      raise ValueError('Unsupported!!')
    else:
      return Vector([value*component for component in self.components])

  def __rmul__(self, value):
    return self * value

  def __repr__(self):
    return f"Vector({', '.join([str(c) for c in self.components])})"
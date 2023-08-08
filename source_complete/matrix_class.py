from source_complete.vector_class import Vector
class Matrix:
    def __init__(self, vector_columns: list):
        self.vector_columns = vector_columns

        self.m = self.vector_columns[0].dimension
        self.n = len(vector_columns)

    @property
    def vector_columns(self):
        return self._vector_columns

    @vector_columns.setter
    def vector_columns(self, vector_columns):
        """
        Checks that all vectors of the vector list are from class Vectors and
        the same dimension
        """
        dims = set()
        for vector in vector_columns:
            if not isinstance(vector, Vector):
                raise ValueError("All columns should be of class Vector")
            dims.add(vector.dimension)
        if len(dims) != 1:
            raise ValueError("All vector columns should have the same dimension")
        self._vector_columns = vector_columns

    def __mul__(self, vector):
        if not isinstance(vector, Vector) and not vector.dimension == self.n:
            raise ValueError("Cannot perform multiplication!")

        result = Vector([0] * self.m)

        for vector, weight in zip(self.vector_columns, vector.components):
            result = result + vector * weight
        return result

    def __repr__(self):

        repr = []
        for col in range(self.m):
            line = []
            for vector in self.vector_columns:
                line.append(str(vector.components[col]))
            line = ', '.join(line)
            repr.append(line)
        repr = '\n'.join(repr)
        return f"Matrix ( \n{repr}\n)"
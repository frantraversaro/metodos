from source.vector_class import Vector

class Matrix:
    def __init__(self, vector_columns: list):
        self.vector_columns = vector_columns
        # Completar con lo que sea necesario


    @property
    def vector_columns(self):
        return self._vector_columns

    @vector_columns.setter
    def vector_columns(self, vector_columns):
        # Completar
        # Comprobar que todos los vectores de la lista de vectores son de la clase Vector y tienen la misma dimensión
        self._vector_columns = vector_columns

    def __mul__(self, vector):
        # Completar
        pass

    def __repr__(self):
        # Completar
        pass

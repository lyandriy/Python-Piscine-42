class Vector:
    def __init__(self, values=None):
        self.values = []
        self.shape = (0, 0)
        if isinstance(values, list):
            if isinstance(values[0][0], float) or isinstance(values[0][0], list):
                self.values = values
                self.shape = (len(self.values), len(self.values[0]))
            else:
                raise ValueError("ERROR")
        elif isinstance(values, int):
            for x in range(values):
                self.values.append([float(x)])
            self.shape = (len(self.values), 1)
        elif isinstance(values, tuple):
            if len(values) != 2 or not isinstance(values[0], int) or not isinstance(values[1], int) or values[0] > values[1]:
                raise ValueError("ERROR")
            else:
                x = values[0]
                while x < values[1]:
                    self.values.append([float(x)])
                    x += 1
                self.shape = (len(self.values), 1)
        else:
            raise ValueError("ERROR")
    
    
    # __add__  __radd__ add & radd : only vectors of same shape.
    def __add__(self, other):
        if isinstance(other, Vector) and self.shape == other.shape:
            if self.shape[0] == 1:#es una lista
                vector = []
                for i in range(self.shape[1]):
                     vector.append(self.values[0][i] + other.values[0][i])
                return Vector(vector)
            else:
                vector = []
                for i in range(len(self.values)):
                    vector.append([(self.values[i][0] + other.values[i][0])])
                return Vector(vector)
        else:
            raise ValueError("ERROR")
        
    def __radd__(self, other):
        return self.__add__(other)

    #__sub__ __rsub__ sub & rsub: only vectors of same shape.
    def __sub__(self, other):
        if isinstance(other, Vector) and self.shape == other.shape:
            if self.shape[0] == 1:
                vector = []
                for i in range(self.shape[1]):
                     vector.append(self.values[0][i] - other.values[0][i])
                return Vector(vector)
            else:
                vector = []
                for i in range(len(self.values)):
                    vector.append([(self.values[i][0] - other.values[i][0])])
                return Vector(vector)
        else:
            raise ValueError("ERROR")
        
    def __rsub__(self, other):
        return self.__sub__(other)
    
    #__mul__ __rmul__ mul & rmul: only scalars (to perform multiplication of Vector by a scalar).   
    def __mul__(self, scalar):
        if isinstance(scalar, (int, float)):
            new_vector = []
            if self.shape[0] == 1:
                new_vector.append([self.values[0][i] * scalar for i in range(self.shape[1])])
                return Vector(new_vector)
            else:
                return Vector([[self.values[i][0] * scalar] for i in range(self.shape[0])])
        else:
            raise ValueError("ERROR")
    
    def __rmul__(self, scalar):
        return self.__mul__(scalar)
    
    #__truediv__ truediv : only with scalars (to perform division of Vector by a scalar).
    #__rtruediv__ rtruediv : raises an NotImplementedError with the message "Division of a scalar by a Vector is not defined here."
    
    def __truediv__(self, scalar):
        if isinstance(scalar, (int, float)):
            if scalar == 0 or scalar == 0.0:
                raise ZeroDivisionError("Cannot be divided by zero.")
            new_vector = []
            if self.shape[0] == 1:
                new_vector.append([self.values[0][i] / scalar for i in range(self.shape[1])])
            else:
                new_vector.append([[self.values[i][0] / scalar] for i in range(self.shape[0])])
            return Vector(new_vector)
        else:
            raise ValueError("ERROR")
    
    def __rtruediv__(self, scalar):
        raise NotImplementedError ("Division of a scalar by a Vector is not defined here.")
    
    #__str__ __repr__  must be identical, i.e we expect that print(vector) and vector within python interpretor behave the same, see correspondi
    def __repr__(self):
        return f"{self.values}"
    
    def __str__(self):
        return f"Vector({self.values})"

    def __len__(self):
        return len(self.values)

    def __getitem__(self, index):
        return self.values[index]

    def dot(self, other):
        print(self)
        print(other)
        if isinstance(other, Vector) and self.shape == other.shape:
            if self.shape[0] == 1:#es una lista
                return sum(self.values[0][i] * other.values[0][i] for i in range(self.shape[1]))
            else:#varias listas
                return sum(self.values[i][0] * other.values[i][0] for i in range(len(self.values)))
        else:
            raise ValueError("ERROR")

    
    def T(self):
        new_values = []
        if self.shape[0] == 1:#una [[1., 2., 3.]]
            for x in self.values[0]:
                new_values.append([x])
        if self.shape[1] == 1:#varias [[0.0], [1.0], [2.0], [3.0]]
            for x in self.values:
                new_values.append(x)
        return Vector(new_values)
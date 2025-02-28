class Vector:
    def __init__(self, values=None):
        self.values = []
        self.shape = (0, 0)
        if isinstance(values, list):
            if isinstance(values[0], float):
                self.values = values
                self.shape = (len(self.values), len(self.values[0]))
            elif isinstance(values[0], list):
                print("HOLAAAAA")
                self.values = values
                self.shape = (len(self.values), len(self.values[0]))
            else:
                print("Error")
        elif isinstance(values, int):
            for x in range(values):
                self.values.append([float(x)])
            self.shape = (len(self.values), 1)
        elif isinstance(values, tuple):
            if len(values) != 2 or not isinstance(values[0], int) or not isinstance(values[1], int) or values[0] > values[1]:
                print("Error")
            else:
                x = values[0]
                while x <= values[1]:
                    self.values.append([float(x)])
                    x += 1
                self.shape = (len(self.values), 1)
        else:
            print("Error")

    def dot(self, other):
        if isinstance(other, Vector) and self.shape == other.shape:
            if self.shape[0] == 1:#es una lista
                sum(self.values[0][i] * other.values[0][i] for i in range(len(self.shape[1])))
            else:#varias listas
                sum(self.values[i][0] * other.values[i][0] for i in range(len(self.values)))
        else:
            print("Error")

    
    def T(self):
        new_values = []
        if self.shape[0] == 1:#una [[1., 2., 3.]]
            for x in self.values[0]:
                new_values.append([x])
        if self.shape[1] == 1:#varias [[0.0], [1.0], [2.0], [3.0]]
            new_list = []
            for x in self.values[0]:
                new_list.append(x[0])
            new_values.append(new_list)
        return new_values
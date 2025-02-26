class Vector:
    def __init__(self, values=None):
        self.values = []
        self.shape = (0, 0)
        if isinstance(values, list):
            if isinstance(values[0], int):
                
            elif isinstance(value[0], list):
            self.value = value
            self.shape = (len(self.value), len(self.value[0]))
        elif isinstance(value, int):
            for x in range(value):
                self.value.append([float(x)])
            self.shape = (len(self.value), 1)
        elif isinstance(value, tuple):
            if len(value) != 2 or not isinstance(value[0], int) or not isinstance(value[1], int) or value[0] > value[1]:
                print("Error")
            else:
                x = value[0]
                while x <= value[1]:
                    self.value.append([float(x)])
                    x += 1
                self.shape = (len(self.value), 1)
        else:
            print("Error")

    def dot():

    
    def T():

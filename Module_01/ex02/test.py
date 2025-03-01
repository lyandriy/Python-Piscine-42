from vector import Vector

if __name__ == "__main__":
    
    v1 = Vector([[0.0], [1.0], [2.0], [3.0]])
    v2 = v1 * 5
    print(v2)
    
    v1 = Vector([[0.0, 1.0, 2.0, 3.0]])
    v2 = v1 * 5
    print(v2)
    
    v2 = v1 / 2.0
    print(v2)
    
    #v1 / 0.0
    
    #2.0 / v1
    
    print(Vector([[0.0], [1.0], [2.0], [3.0]]).shape)
    
    print(Vector([[0.0], [1.0], [2.0], [3.0]]).values)
    
    print(Vector([[0.0, 1.0, 2.0, 3.0]]).shape)
    
    print(Vector([[0.0, 1.0, 2.0, 3.0]]).values)
    
    v1 = Vector([[0.0], [1.0], [2.0], [3.0]])
    print(v1.shape)
    
    print(v1.T())
    
    print(v1.T().shape)
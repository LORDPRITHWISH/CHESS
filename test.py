from brains import move


ta=[[ 5,  4,  3,  20,  9, -3,  4,  5],
    [ 1,  1,  1,  -1, -1, -1,  1,  1], 
    [-1,  0, -1,   0,  0,  0,  0,  0], 
    [ 0,  0,  0,   0,  0,  0,  0,  0], 
    [ 0,  0,  0,   0,  9,  0,  0,  0], 
    [ 0,  0,  0,   0,  0,  0,  0,  0], 
    [-1, -1, -1,  -1, -1, -1, -1, -1], 
    [-5, -4, -3, -20, -9, -3, -4,  1]]    


# print(posible(4,4,ta))
print(move(1,ta))
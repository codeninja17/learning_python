import numpy as np

rows = 10
cols = 10

array_2d = np.zeros((rows, cols))

print(array_2d)

array_2d[1, 3:10] = 20 
print(array_2d[1, 10:1001])

print(max(-256, -255))
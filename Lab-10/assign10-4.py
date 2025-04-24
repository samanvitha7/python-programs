"""Take N (N >= 10) random 2-dimensional points represented in cartesian coordinate space. Store 
them in a numpy array. Convert them to polar coordinates."""

import numpy as np
import math
def polar(arr):
    angle=math.degrees(math.atan(arr[1]/arr[0]))
    arr=np.square(arr)
    magnitude=math.sqrt(np.sum(arr))
    polar_cordinates=(magnitude,angle)
    print(polar_cordinates)

n = int(input("N : "))
coordinates = np.array([list(map(int, input(f"Point {i+1}: ").split())) for i in range(n)])
for point in coordinates:
    polar(point)
"""Consider a 3-D co-ordinate space. Input 10 3-D points. Find the nearest neighbour for each of the points in your 3-D space
 and store them in a list. The final output is a list with each consisting of a point and its nearest neighbour. [Hint: 
 Use distance between two points formula]"""

import math

list = []  # List to store the coordinates
final = []  # List to store the final result

# Input coordinates
for i in range(10):
    print("Enter the coordinate:")
    x = int(input("Enter the x coordinate: "))
    y = int(input("Enter the y coordinate: "))
    z = int(input("Enter the z coordinate: "))
    coordinates = (x, y, z)
    list.append(coordinates)

# Find nearest neighbors
for i in range(len(list)):
    min_distance = float('inf')
    nearest = None
    for j in range(len(list)):
        if i != j:  # Ensure the point is not compared with itself
            distance = math.sqrt(
                (list[i][0] - list[j][0])**2 +
                (list[i][1] - list[j][1])**2 +
                (list[i][2] - list[j][2])**2
            )
            if distance < min_distance:
                min_distance = distance
                nearest = list[j]

    # Append the result as a tuple (current_point, nearest_neighbor)
    final.append((list[i], nearest))

# Display the results
print("\nClosest Neighbors:")
for current, neighbor in final:
    print(f"Point {current} has nearest neighbor {neighbor}")

    


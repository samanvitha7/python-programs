"""
Create a class for representing any 2-D point or vector. The methods inside this class include its magnitude and its rotation
 with respect to the X-axis. Using the objects define functions for calculating the distance between two vectors, dot product, 
 cross product of two vectors. Extend the 2-D vectors into 3-D using the concept of inheritance. Update the methods according
   to 3-D."""

import math

class Point2D:
    def __init__(self, x=0, y=0):
        self.x = x
        self.y = y

    def magnitude(self):
        return math.sqrt(self.x**2 + self.y**2)
    
    def angle_with_x_axis(self):
        return math.atan2(self.y, self.x)
    
    def __repr__(self):
        return f"Point2D({self.x}, {self.y})"

class Vector2D(Point2D):
    def __init__(self, x=0, y=0):
        super().__init__(x, y)
    
    def distance(self, other):
        return math.sqrt((self.x - other.x)**2 + (self.y - other.y)**2)
    
    def dot_product(self, other):
        return self.x * other.x + self.y * other.y
    
    def cross_product(self, other):
        return self.x * other.y - self.y * other.x
    
    def __repr__(self):
        return f"Vector2D({self.x}, {self.y})"

class Vector3D(Vector2D):
    def __init__(self, x=0, y=0, z=0):
        super().__init__(x, y)
        self.z = z
    
    def magnitude(self):
        return math.sqrt(self.x**2 + self.y**2 + self.z**2)
    
    def dot_product(self, other):
        return self.x * other.x + self.y * other.y + self.z * other.z
    
    def cross_product(self, other):
        return Vector3D(
            self.y * other.z - self.z * other.y,
            self.z * other.x - self.x * other.z,
            self.x * other.y - self.y * other.x
        )
    
    def distance(self, other):
        return math.sqrt((self.x - other.x)**2 + (self.y - other.y)**2 + (self.z - other.z)**2)
    
    def __repr__(self):
        return f"Vector3D({self.x}, {self.y}, {self.z})"


v1 = Vector2D(3, 4)
v2 = Vector2D(1, 2)
print("Magnitude of v1:", v1.magnitude())
print("Distance between v1 and v2:", v1.distance(v2))
print("Dot product of v1 and v2:", v1.dot_product(v2))
print("Cross product of v1 and v2:", v1.cross_product(v2))

v3d_1 = Vector3D(1, 2, 3)
v3d_2 = Vector3D(4, 5, 6)
print("Dot product of v3d_1 and v3d_2:", v3d_1.dot_product(v3d_2))
print("Cross product of v3d_1 and v3d_2:", v3d_1.cross_product(v3d_2))

# Python Program to find Diameter, Circumference, and Area Of a Circle
import math

def find_Diameter(radius):
    return 2 * radius

def find_Area(radius):
    return math.pi * radius * radius

r = float(input(' Please Enter the radius of a circle: '))

diameter = find_Diameter(r)
area = find_Area(r)

print("\n Diameter Of a Circle = %.2f" %diameter)
print(" Area Of a Circle = %.2f" %area)
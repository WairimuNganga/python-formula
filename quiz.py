# Class Circle
# A Circle instance accepts attribute radius (r)
# It has a method area that returns the area (A) of the circle using the formula A=πr2
# It has a method to calculate circumference (c) using the formula C=2πr

# Class Square
# A Square instance accepts the attribute side (a)
# It has method area that returns the area (A) of the square using the formula A=a2
# It has a method to calculate the perimeter (P) of the square using the formula P=4a

# Class Rectangle
# A Rectangle instance accepts two sides of a rectangle (w,l)
# It has method to calculate the area (A) of the rectangle using the formula A=wl
# It has a method to calculate the perimeter (P) of the rectangle using the formula P=2(l+w)

# Class Sphere
# A Sphere Instance accepts the radius of the sphere (r)
# It has a method to calculate the surface area (A) using the formula A=4πr2
# It has a method to calculate the volume (V) of the sphere using the formula V = 4/3(πr3)



class Circle:
    def __init__(self,radius):
        self.radius = radius
    def area_of_circle(self):
        area = 3.142 * self.radius * self.radius
        return area
    def circumference_of_cicle(self):
        circumference =  2*3.142*self.radius
        return circumference

class Square:
    def __init__(self,side):
        self.side = side
    def area_of_square(self):
        area = self.side**2
        return area
    def perimeter_of_square(self):
        perimeter = self.side * 4
        return perimeter

class Rectangle:
    def __init__(self,width,length):
        self.width = width
        self.length = length
    def area_of_rectangle(self):
        area = self.length * self.width
        return area
    def perimeter_of_rectangle(self):
        perimeter = 2*(self.length + self.width)
        return perimeter

class Sphere:
    def __init__(self,radius):
        self.radius = radius
    def area_of_sphere(self):
        area = 4 * 3.142 * self.radius**2
        return area
    def volume_of_sphere(self):
        volume = 4/3*(3.142 * self.radius**3)
        return volume

import math

def calculate_circle_area(radius = 0):
    """
    A function that asks the user for the radius and calculates the area of а circle
    :param radius:
    :return area of а circle:
    """
    radius = input("Please Type radius of circle ")
    try:
        circle_area = math.pi * float(radius)
        print(f'Circle area is {circle_area} with radius {radius}')
    except ValueError:
        print("Oops!  Radius was no valid number.  Try again...")
        calculate_circle_area()


# calculate_circle_area()


class Rectangle:
    """
    class that represents a rectangle
    """
    def __init__(self, width, height):
        self.width = width
        self.height = height

    def area(self):
        return self.width * self.height

    def perimeter(self):
        return (self.width + self.height) * 2

    def is_square(self):
        if self.width == self.height:
            return True
        else:
            return False

    def resize(self, new_width, new_height):
        self.width = new_width
        self.height = new_height


rectangle = Rectangle(10,30)
print(f'rectangle area is: {rectangle.area()}')
print(f'rectangle perimeter is: {rectangle.perimeter()}')
print(f'rectangle is square: {rectangle.is_square()}')
rectangle.resize(15,25)
print(f'after resize: rectangle width = {rectangle.width}, rectangle height = {rectangle.height}')


class Rectangle:

    def __init__(self,length,width):
        self.length = length
        self.width=width

    def calculate_Area(self):
        return (self.length * self.width)

    def calculate_perimeter(self):
        return 2*(self.length + self.width)


class Square(Rectangle):

    def __init__(self,side):
        super().__init__(side,side)
    def calculate_perimeter(self):
        return (self.length*4)


rectangle1 = Rectangle(5, 10)

# Calculate the area and perimeter of the rectangle
area1 = rectangle1.calculate_Area()
perimeter1 = rectangle1.calculate_perimeter()
print(f"Rectangle 1 area: {area1}")
print(f"Rectangle 1 perimeter: {perimeter1}")

# Create a Square object
square1 = Square(5)

# Calculate the area and perimeter of the square
area2 = square1.calculate_Area()
perimeter2 = square1.calculate_perimeter()
print(f"Square 1 area: {area2}")
print(f"Square 1 perimeter: {perimeter2}")
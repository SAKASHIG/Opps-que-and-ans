class Shape:
    def __init__(self,color):
        self.color=color

    def set_color(self,new_color):
        return self.color

    def get_color(self):
        return self.color

class Rectangle(Shape):

    def __init__(self,length,width):
        self.length=length
        self.width=width

    def calculate_Area(self):
        return (self.length * self.width)

    def calculate_perimeter(self):
        return 2*(self.length + self.width)


sh = Shape("Burgundy")
sh.set_color("Maroon")
print("New_COLOR:-",sh.get_color())

print("-----------------------------------------------------")
rec = Rectangle(10,10)
print("Area:--",rec.calculate_Area())
print("Perimenter:--",rec.calculate_perimeter())
class Rectangle:
    def __init__(self, x, y, width, height ):
        self.x = x
        self.y = y
        self.width = width
        self.height = height
    def __str__(self):
        return f"Rectangle: {self.x},{self.y},{self.width},{self.height}"
    def area(self):
        return self.width * self.height
result = Rectangle(5,10,50,100)
print (result)
print("Площадь круга:", result.area())
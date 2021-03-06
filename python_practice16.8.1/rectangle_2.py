from rectangle import Rectangle, Square, Circle
# создаем 2 прямоугольника
rect_1 = Rectangle(3,4)
rect_2 = Rectangle(12,5)
#вывод площади наших двух прямоугольников
print(rect_1.get_area())
print(rect_2.get_area())

square_1 = Square(5)
square_2 = Square(10)
print(square_1.get_area_square())
print(square_2.get_area_square())

circle_1 = Circle(5)
circle_2 = Circle(10)

print(circle_1.area_circle())
print(circle_2.area_circle())

figures = [ rect_1,rect_2,square_1,square_2,circle_1,circle_2]
for figure in figures:
    if isinstance(figure,Square):
        print("площадь квадрата =" ,figure.get_area_square())

    elif isinstance(figure,Circle):
        print("площадь круга = ",figure.area_circle())
    else:
        print(" площадь прямоугольника = ",figure.get_area())
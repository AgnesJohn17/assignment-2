from rectangle import Rectangle

rectangle_1= Rectangle()
rectangle_1._width= 2.54
rectangle_1._height= 3.7

rectangle_2= Rectangle()
rectangle_2._width= 4.1
rectangle_2._height= 5.6

rectangle_1.description()
rectangle_2.description()

print( rectangle_1.getArea()+ rectangle_2.getArea())




class Rectangle:
    _width= 0.0
    _height= 0.0
    
    def __init__(self,width,height):
        self._width= width
        self._height= height
        
    def getWidth(self):
        return self._width
    
    def getHeight(self):
        return self._height
    
    def description(self):
        self._width=round(self._width)
        self._height=round(self._height)
        print(f"This rectangle has a width of {self._width}and a height{self._height}")
    
    def isSquare(self):
        if (self._width==self._height):
            return True
        else:
            return False
    
    def getPerimeter(self):
        return 2*(self._width+self._height)
    
    def getArea(self):
        return self._width*self._height
    
    
            
         
    
        
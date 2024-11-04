import random

class Dice:
    
    number=1
    
    def __init__(self):
        pass
    
    def getNumber(self):
        return self.number
    
    def setNumber(self,newValue):
        self.number = newValue
        
    def roll(self):
        randomNum = random.randit(1,6)
        self.number = randomNum
        return randomNum
        
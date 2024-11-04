


class Player:
    
    _id = 0
    _dice = Dice()
    
    def __intit__(Self,newId):
        self._id = newId
        
    def rollDice(self):
        return self._dice.roll()
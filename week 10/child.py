from neighbour import Neighbour


class Child:
    _numberofCandies= 0
    _costume= ""
    
    def __init__(self,_costume, _numberofCandies):
        self._numberofCandies= _numberofCandies
        self._costume= _costume
        
        
    def askForCandy(self,neighbour):
        candies=neighbour.givecandy()
        

    def eatCandies(self, amount: int):
        if amount <= self._numberOfCandies:
            self._numberOfCandies -= amount
            print(f"The child ate {amount} candies and now has {self._numberOfCandies} left.")
        else:
            print("Not enough candies to eat that amount.")
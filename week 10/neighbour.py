
            
            
class Neighbour:
    _numberOfCandies=0
    _maximum=3
    
    def __init__(self, numberOfCandies, maximum):
        self._numberOfCandies = numberOfCandies
        self.maximum = maximum

    def addMoreCandies(self, numberofCandies):
        self._numberOfCandies += numberofCandies
        
    def giveCandy(self):
        if self._numberOfCandies >=self._maximum:
            self._numberOfCandies -=self._maximum
            return self._maximum
            
        else:
            print("Neighbour is out of candies.")
            return 0

n1= Neighbour(10,2)
print(n1._numberOfCandies)
n1.addMoreCandies(5)
print(n1._numberOfCandies)
n1.giveCandy()
print(n1._numberOfCandies)
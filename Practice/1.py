class Student:
    def __init__(self,name,age,is_enrolled):
        self.name=name
        self.age=age
        self.is_enrolled=is_enrolled
        
    def __str__(self):
        return f"Name:{self.name}, Age:{self.age}, Enrolled:{self.is_enrolled}"
    
Boggies= Student('agnes',18,'yes')
print(Boggies)
class Plant:
    def __init__(self, name, start_height, daily_growth_rate):
        self.name = name
        self.height = start_height
        self.daily_growth_rate = daily_growth_rate
    
    def display_information(self):
        print(f"{self.name} is {self.height} cm tall and has a daily growth rate of {self.daily_growth_rate} cm per day.")
    
    def grow(self, days):
        for _ in range(days):
            self.height += self.daily_growth_rate
    
    def is_taller(self, other_plant):
        return self.height > other_plant.height




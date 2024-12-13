class Toy:
    def __init__(self, name, category, description):
        self.name = name
        self.category = category
        self.description = description

    def __str__(self):
        return f"{self.name} ({self.category}): {self.description}"

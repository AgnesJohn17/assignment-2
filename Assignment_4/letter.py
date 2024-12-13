class Letter:
    def __init__(self, letter_id, full_name, toys):
        self.letter_id = letter_id
        self.full_name = full_name
        self.toys = toys

    def __str__(self):
        toy_names = ", ".join([str(toy) for toy in self.toys])
        return f"Letter ID: {self.letter_id}, Name: {self.full_name}, Toys: {toy_names}"

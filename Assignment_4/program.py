import json
import csv
from letter import Letter
from toy import Toy

class Program:
    def __init__(self):
        self.letters = []

    def run(self):
        print("Welcome to Santa's Software Helper!")
        self.load_letters()
        self.menu()

    def load_letters(self):
        try:
            with open("Letters.json", "r") as file:
                data = json.load(file)
                for item in data:
                    toys = [Toy(t["name"], t["category"], t["description"]) for t in item["toys"]]
                    letter = Letter(item["id"], item["full_name"], toys)
                    self.letters.append(letter)
                print("Letters loaded successfully.")
        except FileNotFoundError:
            print("Error: Letters.json file not found.")

    def export_children_list(self):
        if not self.letters:
            print("No letters to export.")
            return

        with open("ChildrenListTemplate.csv", mode="w", newline="") as file:
            writer = csv.writer(file)
            writer.writerow(["Letter ID", "Full Name", "Nice"])
            for letter in self.letters:
                writer.writerow([letter.id, letter.full_name, ""])

        print("Children list exported.")

    def import_children_data(self):
        try:
            with open("ChildrenListTemplate.csv", mode="r") as file:
                reader = csv.reader(file)
                next(reader)  # Skip header row
                for row in reader:
                    letter = next((l for l in self.letters if l.id == row[0]), None)
                    if letter:
                        letter.approved = True if row[2].lower() == "nice" else False
            self.save_letter_data()
            print("Children data updated.")
        except FileNotFoundError:
            print("Error: ChildrenList.csv file not found.")

    def export_toy_manufacturing_data(self):
        if not self.letters:
            print("No letters to export.")
            return

        with open("ChildrenListTemplate.csv.csv", mode="w", newline="") as file:
            writer = csv.writer(file)
            writer.writerow(["Name", "Category", "Description"])
            for letter in self.letters:
                for toy in letter.toys:
                    writer.writerow([toy.name, toy.category, toy.description])

        print("Toy manufacturing data exported.")

    def save_letter_data(self):
        try:
            data = [{
                "id": letter.id,
                "full_name": letter.full_name,
                "toys": [{"name": toy.name, "category": toy.category, "description": toy.description} for toy in letter.toys],
                "approved": letter.approved
            } for letter in self.letters]
            with open("Letters.json", "w") as file:
                json.dump(data, file, indent=4)
            print("Letter data saved.")
        except FileNotFoundError:
            print("Error: Unable to save letter data.")

    def menu(self):
        while True:
            print("\n1. View Letters\n2. Export Children List\n3. Import Naught/Nice Data\n4. Export Toy Manufacturing Data\n5. Save Letter Data\n6. Exit")
            choice = input("Choose an option: ")

            if choice == "1":
                self.view_letters()
            elif choice == "2":
                self.export_children_list()
            elif choice == "3":
                self.import_children_data()
            elif choice == "4":
                self.export_toy_manufacturing_data()
            elif choice == "5":
                self.save_letter_data()
            elif choice == "6":
                print("Goodbye!")
                break
            else:
                print("Invalid choice. Try again.")

    def view_letters(self):
        if not self.letters:
            print("No letters available.")
            return

        for letter in self.letters:
            print(letter)

if __name__ == "__main__":
    Program().run()

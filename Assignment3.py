class Shape:
    def __init__(self, color):
        self.color = color

    def get_description(self):
        return f"A {self.color} shape."


class Circle(Shape):
    def __init__(self, color, radius):
        super().__init__(color)
        self.radius = radius

    def get_area(self):
        return 3.14 * self.radius * self.radius

    def get_circumference(self):
        return 2 * 3.14 * self.radius

    def get_description(self):
        return f"A {self.color} circle with radius {self.radius}."


class Rectangle(Shape):
    def __init__(self, color, length, width):
        super().__init__(color)
        self.length = length
        self.width = width

    def get_area(self):
        return self.length * self.width

    def get_perimeter(self):
        return 2 * (self.length + self.width)

    def get_description(self):
        return f"A {self.color} rectangle of length {self.length} and width {self.width}."


class Triangle(Shape):
    def __init__(self, color, base, height):
        super().__init__(color)
        self.base = base
        self.height = height

    def get_area(self):
        return 0.5 * self.base * self.height

    def get_description(self):
        return f"A {self.color} triangle with base {self.base} and height {self.height}."


class Square(Shape):
    def __init__(self, color, side):
        super().__init__(color)
        self.side = side

    def get_area(self):
        return self.side * self.side

    def get_perimeter(self):
        return 4 * self.side

    def get_description(self):
        return f"A {self.color} square with side {self.side}."


class Program:
    def __init__(self):
        self.shapes = []

    def run(self):
        print("Welcome to the Simple Shape Collection!")
        while True:
            print("\nChoose an option:")
            print("1. Add a shape to the collection")
            print("2. Remove a shape")
            print("3. Get information about a shape in the collection")
            print("4. Get information about the collection")
            print("5. Quit the program")
            choice = input("Enter your choice: ")

            if choice == "1":
                self.add_shape()
            elif choice == "2":
                self.remove_shape()
            elif choice == "3":
                self.view_shapes()
            elif choice == "4":
                self.show_stats()
            elif choice == "5":
                print("Goodbye!")
                break
            else:
                print("Invalid choice. Try again!")

    def add_shape(self):
        print("\nWhat shape do you want to add?")
        print("1. Circle")
        print("2. Rectangle")
        print("3. Triangle")
        print("4. Square")
        shape_type = input("Enter the number: ")

        color = input("Enter the color of the shape: ")

        if shape_type == "1":
            radius = float(input("Enter the radius of the circle: "))
            self.shapes.append(Circle(color, radius))
            print("Circle added!")
        elif shape_type == "2":
            length = float(input("Enter the length of the rectangle: "))
            width = float(input("Enter the width of the rectangle: "))
            self.shapes.append(Rectangle(color, length, width))
            print("Rectangle added!")
        elif shape_type == "3":
            base = float(input("Enter the base of the triangle: "))
            height = float(input("Enter the height of the triangle: "))
            self.shapes.append(Triangle(color, base, height))
            print("Triangle added!")
        elif shape_type == "4":
            side = float(input("Enter the side of the square: "))
            self.shapes.append(Square(color, side))
            print("Square added!")
        else:
            print("Invalid shape type!")

    def remove_shape(self):
        if not self.shapes:
            print("No shapes to remove.")
            return

        print("\nShapes in the collection:")
        for i, shape in enumerate(self.shapes, 1):
            print(f"{i}. {shape.get_description()}")
        choice = int(input("Enter the number of the shape to remove: "))

        if 1 <= choice <= len(self.shapes):
            removed = self.shapes.pop(choice - 1)
            print(f"Removed: {removed.get_description()}")
        else:
            print("Invalid choice!")

    def view_shapes(self):
        if not self.shapes:
            print("No shapes in the collection.")
            return

        print("\nShapes in the collection:")
        i = 1  # Start the index from 1
        for shape in self.shapes:
            print(f"{i}. {shape.get_description()}")
            i += 1  # Increment the index after each iteration


    def show_stats(self):
        print("\nCollection Statistics:")
        print(f"Total shapes in the collection: {len(self.shapes)}")
        total_area = sum(shape.get_area() for shape in self.shapes if hasattr(shape, "get_area"))
        print(f"Total combined area of shapes: {total_area:.2f}")


if __name__ == "__main__":
    Program().run()

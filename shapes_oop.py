class Shape:
    def __init__(self):
        pass

    def area(self):
        pass

    def perimeter(self):
        pass

    def __str__(self):
        pass


class Circle(Shape):
    def __init__(self, radius):
        self.radius = radius

    def area(self):
        return 3.14 * self.radius ** 2

    def perimeter(self):
        return 2 * 3.14 * self.radius

    def set_radius(self, radius):
        self.radius = radius

    def __str__(self):
        return f"Circle with radius {self.radius}"


class Square(Shape):
    def __init__(self, length):
        self.length = length

    def area(self):
        return self.length ** 2

    def perimeter(self):
        return 4 * self.length

    def __str__(self):
        return f"Square with length {self.length}"


class Rectangle(Shape):
    def __init__(self, length, width):
        self.length = length
        self.width = width

    def area(self):
        return self.length * self.width

    def perimeter(self):
        return 2 * (self.length + self.width)

    def __str__(self):
        return f"Rectangle with length {self.length} and width {self.width}"


class Cube(Shape):
    def __init__(self, length):
        self.length = length

    def area(self):
        return 6 * self.length ** 2

    def perimeter(self):
        return 12 * self.length

    def volume(self):
        return self.length ** 3

    def __str__(self):
        return f"Cube with length {self.length}"

def main():
    shapes = []  # lista przechowująca utworzone kształty

    while True:
        print("\nWhat shape do you want to create?")
        print("1. Circle")
        print("2. Square")
        print("3. Rectangle")
        print("4. Cube")
        print("5. Exit")

        choice = input("Enter your choice: ")

        if choice == "1":
            radius = float(input("Enter the radius of the circle: "))
            circle = Circle(radius)
            print(f"The area of the {circle} is {circle.area()}")
            print(f"The perimeter of the {circle} is {circle.perimeter()}")

        elif choice == "2":
            length = float(input("Enter the length of the square: "))
            square = Square(length)
            print(f"The area of the {square} is {square.area()}")
            print(f"The perimeter of the {square} is {square.perimeter()}")

        elif choice == "3":
            length = float(input("Enter the length of the rectangle: "))
            width = float(input("Enter the width of the rectangle: "))
            rectangle = Rectangle(length, width)
            print(f"The area of the {rectangle} is {rectangle.area()}")
            print(f"The perimeter of the {rectangle} is {rectangle.perimeter()}")

        elif choice == "4":
            length = float(input("Enter the length of the cube: "))
            cube = Cube(length)
            print(f"The surface area of the {cube} is {cube.area()}")
            print(f"The volume of the {cube} is {cube.volume()}")

        elif choice == "5":
            print("Goodbye!")
            break

        else:
            print("Invalid choice, please try again.")

main()

class InvalidData(Exception):
    pass

class Rectangle:
    def __init__(self,length,height):
        if length <= 0 or height <=0:
            raise InvalidData("Length and height must be positive")
        self.length = length
        self.height = height

    def area(self):
        return self.length * self.height

    def __str__(self):
        return f"Rectangle ({self.length} x {self.height})"

    def __repr__(self):
        return f"Rectangle ({self.length}, {self.height})"

class Cuboid(Rectangle):
    def __init__(self,length,height,width):
        super().__init__(length,height)
        if width <= 0:
            raise InvalidData("Width must be positive")
        self.width = width

    def area(self):
        return 2 * (self.length * self.height + self.length * self.width + self.height * self.width)

    def volume(self):
        return self.length * self.height * self.width

    def __str__(self):
        return f"Cuboid ({self.length} x {self.height} x {self.width})"

    def __repr__(self):
        return f"Cuboid({self.length}, {self.height}, {self.width})"


def read_data():
    shapes = []
    with open("input.txt") as file:
        for line in file:
            try:
                shape_data = [float(x) for x in line.strip().split()]
                if len(shape_data) == 2:
                    shape = Rectangle(shape_data[0], shape_data[1])
                elif len(shape_data) == 3:
                    shape = Cuboid(shape_data[0], shape_data[1], shape_data[2])
                else:
                    raise InvalidData("Invalid data format")
                shapes.append(shape)
            except ValueError:
                print(f"Invalid data format in line: {line}")
            except InvalidData as e:
                print(f"Invalid data in line: {line.strip()}, {e}")
    return shapes


def main():
    shapes = read_data()
    for shape in shapes:
        print(shape)
        print(f"Area: {shape.area()}")
        if isinstance(shape, Cuboid):
            print(f"Volume: {shape.volume()}")
        print()


if __name__ == "__main__":
    main()

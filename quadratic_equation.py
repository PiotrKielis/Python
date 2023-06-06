import math

class QuadraticEquation:
    def __init__(self, a, b, c):
        self._a = self._validate_nonzero(a, 'a')
        self._b = b
        self._c = c

    @property
    def a(self):
        return self._a

    @a.setter
    def a(self, value):
        self._a = self._validate_nonzero(value, 'a')

    @property
    def delta(self):
        return self._b**2 - 4*self._a*self._c

    def roots(self):
        delta = self.delta
        if delta > 0:
            x1 = (-self._b + math.sqrt(delta)) / (2*self._a)
            x2 = (-self._b - math.sqrt(delta)) / (2*self._a)
            return (x1, x2)
        elif delta == 0:
            x = -self._b / (2*self._a)
            return (x,)
        else:
            return ()

    def factored_form(self):
        if self.delta >= 0:
            return f"(x - {round(-self._b/(2*self._a) + math.sqrt(self.delta)/(2*self._a), 2)})" \
                   f"(x - {round(-self._b/(2*self._a) - math.sqrt(self.delta)/(2*self._a), 2)})"
        else:
            return 'Factored form does not exist'

    def __call__(self, x):
        return self._a*x**2 + self._b*x + self._c

    def __add__(self, other):
        if isinstance(other, QuadraticEquation):
            a = self._a + other._a
            b = self._b + other._b
            c = self._c + other._c
            return QuadraticEquation(a, b, c)
        else:
            raise TypeError("Unsupported operand type for +")

    def __sub__(self, other):
        if isinstance(other, QuadraticEquation):
            a = self._a - other._a
            b = self._b - other._b
            c = self._c - other._c
            return QuadraticEquation(a, b, c)
        else:
            raise TypeError("Unsupported operand type for -")

    def __mul__(self, scalar):
        if isinstance(scalar, (int, float)):
            a = self._a * scalar
            b = self._b * scalar
            c = self._c * scalar
            return QuadraticEquation(a, b, c)
        else:
            raise TypeError("Unsupported operand type for *")

    def __str__(self):
        return f"y = {self._a}x^2 + {self._b}x + {self._c}"

    def __repr__(self):
        return f"QuadraticEquation({self._a}, {self._b}, {self._c})"

    @staticmethod
    def _validate_nonzero(value, name):
        if value != 0:
            return value
        else:
            raise ValueError(f"{name} must be nonzero")


class Menu:
    def __init__(self):
        self.equation = None

    def display_menu(self):
        print("1. Create a quadratic equation")
        print("2. Calculate delta")
        print("3. Calculate roots")
        print("4. Display factored form")
        print("5. Evaluate equation for x")
        print("6. Add two equations")
        print("7. Subtract two equations")
        print("8. Multiply equation by scalar")
        print("9. Display equation")
        print("10. Display equation representation")
        print("0. Exit")

    def run(self):
        while True:
            self.display_menu()
            choice = input("Enter your choice: ")
            if choice == '1':
                self.create_equation()
            elif choice == '2':
                self.calculate_delta()
            elif choice == '3':
                self.calculate_roots()
            elif choice == '4':
                self.display_factored_form()
            elif choice == '5':
                self.evaluate_equation()
            elif choice == '6':
                self.add_equations()
            elif choice == '7':
                self.subtract_equations()
            elif choice == '8':
                self.multiply_by_scalar()
            elif choice == '9':
                self.display_equation()
            elif choice == '10':
                self.display_equation_representation()
            elif choice == '0':
                break
            else:
                print("Invalid choice. Please try again.")

    def create_equation(self):
        a = float(input("Enter coefficient a: "))
        b = float(input("Enter coefficient b: "))
        c = float(input("Enter coefficient c: "))
        try:
            self.equation = QuadraticEquation(a, b, c)
            print("Quadratic equation created successfully.")
        except ValueError as e:
            print(e)

    def calculate_delta(self):
        if self.equation is not None:
            delta = self.equation.delta
            print(f"Delta: {delta}")
        else:
            print("No equation created yet.")

    def calculate_roots(self):
        if self.equation is not None:
            roots = self.equation.roots()
            if len(roots) == 0:
                print("No roots")
            else:
                print("Roots:", roots)
        else:
            print("No equation created yet.")

    def display_factored_form(self):
        if self.equation is not None:
            factored_form = self.equation.factored_form()
            print("Factored form:", factored_form)
        else:
            print("No equation created yet.")

    def evaluate_equation(self):
        if self.equation is not None:
            x = float(input("Enter x: "))
            result = self.equation(x)
            print(f"Result: {result}")
        else:
            print("No equation created yet.")

    def add_equations(self):
        if self.equation is not None:
            equation2 = self._create_equation_from_user_input()
            if equation2 is not None:
                result = self.equation + equation2
                print("Result:", result)
        else:
            print("No equation created yet.")

    def subtract_equations(self):
        if self.equation is not None:
            equation2 = self._create_equation_from_user_input()
            if equation2 is not None:
                result = self.equation - equation2
                print("Result:", result)
        else:
            print("No equation created yet.")

    def multiply_by_scalar(self):
        if self.equation is not None:
            scalar = float(input("Enter scalar value: "))
            result = self.equation * scalar
            print("Result:", result)
        else:
            print("No equation created yet.")

    def display_equation(self):
        if self.equation is not None:
            print("Equation:", self.equation)
        else:
            print("No equation created yet.")

    def display_equation_representation(self):
        if self.equation is not None:
            print("Equation representation:", repr(self.equation))
        else:
            print("No equation created yet.")

    @staticmethod
    def _create_equation_from_user_input():
        a = float(input("Enter coefficient a: "))
        b = float(input("Enter coefficient b: "))
        c = float(input("Enter coefficient c: "))
        try:
            return QuadraticEquation(a, b, c)
        except ValueError as e:
            print(e)
            return None

menu = Menu()
menu.run()

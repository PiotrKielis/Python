class Pupil:
    def __init__(self, name, surname):
        self.name = name
        self.surname = surname
        self.marks = {}

    def complete_marks(self):
        subjects = ['math', 'english', 'history']
        for subject in subjects:
            while True:
                mark = input(f"Enter the mark for {subject}: ")
                try:
                    mark = float(mark)
                    if mark not in [1, 1.5, 2, 2.5, 3, 3.5, 4, 4.5, 5, 5.5, 6]:
                        raise ValueError
                    self.marks[subject] = mark
                    break
                except ValueError:
                    print("Invalid mark, please try again.")

    def print_marks(self):
        for subject, mark in self.marks.items():
            print(f"{subject}: {mark}")

    def mean(self):
        return sum(self.marks.values()) / len(self.marks)

    def __str__(self):
        return f"{self.name} {self.surname}, average mark: {self.mean()}"


class Student(Pupil):
    def __init__(self, name, surname):
        super().__init__(name, surname)
        self.weights = {}

    def complete_weights(self):
        for subject, mark in self.marks.items():
            while True:
                weight = input(f"Enter the weight for {subject}: ")
                try:
                    weight = float(weight)
                    if weight < 0 or weight > 1:
                        raise ValueError
                    self.weights[subject] = weight
                    break
                except ValueError:
                    print("Invalid weight, please try again.")

    def mean(self):
        weighted_sum = sum(mark * weight for mark, weight in zip(self.marks.values(), self.weights.values()))
        total_weight = sum(self.weights.values())
        return weighted_sum / total_weight

    def __str__(self):
        return super().__str__()


# Create objects
pupil = Pupil("John", "Doe")
pupil.complete_marks()

student = Student("Jane", "Doe")
student.marks = pupil.marks.copy()
student.complete_weights()

# Print results
print("Pupil:")
pupil.print_marks()
print(pupil)

print("Student:")
student.print_marks()
print(student)

class Person:
    def __init__(self):
        self._name = None
        self._surname = None
        self._age = None

    @property
    def name(self):
        return self._name

    @name.setter
    def name(self, value):
        if len(value) >= 3:
            self._name = value
        else:
            print("Name should have at least 3 characters")

    @property
    def surname(self):
        return self._surname

    @surname.setter
    def surname(self, value):
        if len(value) >= 3:
            self._surname = value
        else:
            print("Surname should have at least 3 characters")

    @property
    def age(self):
        return self._age

    @age.setter
    def age(self, value):
        if isinstance(value, int) and 0 <= value <= 130:
            self._age = value
        else:
            print("Age should be an integer between 0 and 130")

    def __str__(self):
        return f"{self.name} {self.surname}, age: {self.age}"


class Student(Person):
    def __init__(self):
        super().__init__()
        self._field_of_study = None
        self._student_book = {}

    @property
    def field_of_study(self):
        return self._field_of_study

    @field_of_study.setter
    def field_of_study(self, value):
        self._field_of_study = value
    @property
    def student_book(self):
        return self._student_book

    def add_grade(self, subject, grade):
        self._student_book[subject] = grade

    def __str__(self):
        return f"{super().__str__()}, field of study: {self.field_of_study}, grades: {self.student_book}"


class Employee(Person):
    def __init__(self):
        super().__init__()
        self._job_title = None
        self._skills = []

    @property
    def job_title(self):
        return self._job_title

    @job_title.setter
    def job_title(self, value):
        self._job_title = value

    @property
    def skills(self):
        return self._skills

    def add_skill(self, skill):
        self._skills.append(skill)

    def __str__(self):
        return f"{super().__str__()}, job title: {self.job_title}, skills: {', '.join(self.skills)}"


# przykładowe użycie klas
person = Person()
person.name = "Jan"
person.surname = "Kowalski"
person.age = 35
print(person)

student = Student()
student.name = "Anna"
student.surname = "Nowak"
student.age = 22
student.field_of_study = "Computer Science"
student.add_grade("Math", 4)
student.add_grade("Programming", 5)
print(student)

employee = Employee()
employee.name = "John"
employee.surname = "Smith"
employee.age = 45
employee.job_title = "Software Developer"
employee.add_skill("Python")
employee.add_skill("Java")
print(employee)

my_student = {
    'name': 'Paul',
    'grades': [70, 88, 90, 99],
    'average': None
}


def average(student):
    return sum(student['grades']) / len(student['grades'])


# print(average(my_student))


class Student:
    def __init__(self, new_name, new_grade):
        self.name = new_name
        self.grades = new_grade

    def average(self):
        return sum(self.grades) / len(self.grades)

    def print_info(self):
        print(f'<<{self.name}>> by {self.grades} and average of {self.average()}')


student_one = Student('Marty', [70, 156, 1, 99])
student_two = Student('Jose', [70, 88, 322, 200])

# print(student_one.average())
# print(Student.average(student_one))
# student_one.print_info()
# student_two.print_info()


class Movie:
    def __init__(self, name, year):
        self.name = name
        self.year = year


matrix = Movie('Matrix', 1999)

# print(matrix.name)

movies = ['Matrix', 'Nemo']
# print(movies.__class__)
# print(len(movies))

class Garage:
    def __init__(self):
        self.cars = []

    def __len__(self):
        return len(self.cars)

    def __getitem__(self, item):
        return self.cars[item]

    def __setitem__(self, key, value):
        self.cars[key] = value

    def __repr__(self):
        return f'<Garage {self.cars}'

    def __str__(self):
        return f'Garage with {len(self)} cars.'

# ford = Garage()
# print(ford.cars)
# ford.cars.append('Ford')
# ford.cars.append('Fiesta')
# print(ford.cars)
# print(len(ford))
#
# print(ford[0])
# print(ford)
# ford[0] = 'Sierra'
# print(ford[0])
# print(ford)
#
#
# for car in ford:
#     print(car)

class Student:
    def __init__(self, name, school):
        self.name = name
        self.school = school
        self.marks = []

    def average(self):
        return sum(self.marks) / len(self.marks)

class WorkingStudent(Student):
    def __init__(self, name, school, salary):
        super().__init__(name, school)
        self.salary = salary

    @property
    def weekly_salary(self):
        return self.salary * 37.5

rolf = WorkingStudent('Rolf', 'MIT', 15.50)

rolf.marks.append(78)
rolf.marks.append(99)
print(rolf.weekly_salary)
print(rolf)
print(rolf.average())

class FixedFloat:
    def __init__(self, amount):
        self.amount = amount

    def __repr__(self):
        return f'FixedFloat {self.amount:.2f}'

    @classmethod
    def from_sum(cls, value1, value2):
        return cls(value1 + value2)

number = FixedFloat(18.5533)
new_number = FixedFloat.from_sum(19.575, 0.789)
print(number)
print(new_number)

class Euro(FixedFloat):
    def __init__(self, amount):
        super().__init__(amount)
        self.symbol = 'E'

    def __repr__(self):
        return f'Euro {self.symbol}{self.amount:.2f}'

money = Euro(18.786)
print(money)
money = Euro.from_sum(16.758, 9.999)
print(money)


class Person:
    def __init__(self, name):
        self.name = name

    @classmethod
    def greet_friend(cls, friend_name):
        return f'Hey there, {friend_name}!'


mark = Person('Mark')
print(Person.greet_friend('Paul'))
print(mark)


class Person:
    decade = 10
    def __init__(self, name, age):
        self.name = name
        self.age = age

    def __str__(self):
        return f"person{self.__dict__}"


class Student(Person):
    def __init__(self, grade, name, age):
        Person.__init__(self, name, age)
        self.grade = grade

    def __str__(self):
        return f"student{self.__dict__}"


class Teacher(Person):

    def __init__(self, name, age, field):
        super().__init__(name, age)
        self.field = field

    def __str__(self):
        return f"teacher{self.__dict__}"


p1 = Person('John', 10)
p1.height = 190
p1.decade = 20

p2 = Person('mamad', 32)

s1 = Student(age=10, name='Alex', grade=10)
Student.decade = 20
s2 = Student(age=15, name='Alexi', grade=12)

t1 = Teacher(name='John', age=20, field='math')
Person.decade = 25
s3 = Student(age=16, name='bagher', grade=15)
p3 = Person('mark', 20)

print(p1, p1.decade)
print(p2, p2.decade)
print(p3, p3.decade)
print(s1, s1.decade)
print(s2, s2.decade)
print(s3, s3.decade)
print(t1, t1.decade)

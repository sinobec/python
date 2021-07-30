class Student:
    age = 0
    className = ''

    def __init__(self, age, name):
        self.age = age
        self.className = name
    def __str__(self):
        return f'[age={self.age}, class name={self.className}]'
std = Student(8, 'Third')
print(std)

#print(f'Student: {std}\nHis/her age is {std.age} yrs and the class name is {std.className}.')
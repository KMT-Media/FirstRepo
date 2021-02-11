# CLASS AND OBJECT RELATED

class ExampleClass:
    class_attribute = 0
    class_attr = []
    def __init__(self, instance_attribute):
        self.instance_attribute = instance_attribute

foo = ExampleClass(1)
bar = ExampleClass(2)

# explain the differenct between class attibute and instance attribute

# print instance attribute of the object foo
# 1
print(foo.instance_attribute)

# print instance attribute of the object bar
# 2
print(bar.instance_attribute)

# print class attribute of ExampleClass as a property of that class itself
# 0 
print(ExampleClass.class_attribute)

# print class attribute as property of the objects foo,bar
print(foo.class_attribute)
# 0
print(bar.class_attribute)
# 0

# try to print instance attribute as class property
# print(ExampleClass.instance_attribure)
# Attribute error

# modify class attribute as a class property
foo.class_attribute = 5
print(foo.class_attribute)

# print class attribute as property of bar
print(bar.class_attribute)
# 0

# -----------
# # print class_attr as property of foo
# print(foo.class_attr)

# # modify class_attr as a property foo
# foo.class_attr.append(0)

# print(foo.class_attr)

# # print class attribte as a property of bar
# print(bar.class_attr)

# when we mutate class attributes in objects like list, its not always the case

# -----------
# to avoid this problem attach your new list
foo.class_attr = list('example')
print(foo.class_attr)

# print class attribute as bar property
print(bar.class_attr)

# other same example
class Service:
    data = []

    def __init__(self, other_data):
        self.other_data = other_data

s1 = Service(['a','b'])
s2 = Service(['a','b'])

# s1.data.append(1) # []

# print(s1.data)

# print(s2.data) # [1]


# s2.data.append(2) # [1,2]

# print(s1.data) # [1,2]

# print(s2.data) # [1,2]

# avoid this problem
s1.data = list('12')
print(s1.data)
s2.data = list('34')
print(s2.data)


# cases to use class attributes
# storing constants
class Circle(object):
    pi = 3.14159

    def __init__(self, radius):
        self.radius = radius

    def area(self):
        return Circle.pi * self.radius * self.radius

print(Circle.pi)
## 3.14159

c = Circle(10)
print(c.pi)
## 3.14159

print(c.area())
## 314.159


# defining default values

class MyClass(object):
    limit = 10

    def __init__(self):
        self.data = []

    def item(self, i):
        return self.data[i]

    def add(self, e):
        if len(self.data) >= self.limit:
            raise Exception("Too many elements")
        return self.data.append(e)

MyClass.limit
## 10

foo1 = MyClass()
foo1.limit = 50
## foo can now hold 50 elements—other instances can hold 10

# show inheritance with simpe example
# base class
class User:
    # constructor
    def __init__(self, email, key):
        self.email = email
        self.key = key

    def info(self):
        return f'Email {self.email} - Key {self.key}'
# class premiere inherits class user
class Premiere(User):
    def __init__(self, email, key, paypall):
        super().__init__(email, key)
        self.paypall = paypall

user1 = Premiere('Kidus@email.com', 1234, 'Kidus@paypall.com')
user1.info()
print(user1.info())


# updating methods using inheritance
# base class
class Person:
    # constructor
    def __init__(self, name, idnum):
        self.name = name
        self.idnum = idnum

    # display person info
    def display(self):
        return f'Name {self.name}, ID {self.idnum}'

    ## check if person is employee
    def isEmployee(self):
        return False


# sub class
class Employee(Person):
    # sub class constructor
    def __init__(self, name, idnum, salary):
        self.salary = salaryt
        super().__init__(name, idnum)

    # update display info
    def display(self):
        return f'Name {self.name}, ID {self.idnum}, salary {self.salary}'

    ## update membership
    def isEmployee(self):
        return True

emp = Person('kidus', 1917)
print(emp.display())

emp = Employee('kidus',1917,200_000)
print(emp.display())
__author__ = '1002475'

class Person:
    def __init__(self, name, phone=None):
        self.name = name
        self.phone = phone

    def display(self):
        return '<Person %s %s>' % (self.name, self.phone)
    def __repr__(self):
        return '<Person %s %s>' % (self.name, self.phone)


class Employee(Person):
    def __init__(self, name, phone, position, salary):
        Person.__init__(self, name, phone)
        self.position = position
        self.salary = salary

    def __repr__(self):
        s = Person.__repr__(self)
        return s + ' <Employee %s %s>' % (self.position, self.salary)


print '...program start'

m1 = Employee('jon', 5564,'A', 200)
print m1
m2 = Employee('kim', 8546,'B', 300)
print m2
m3 = Person('Hon','0100')
print m3
print m1.name, m1.position
print m2.name, m2.position
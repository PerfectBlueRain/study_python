__author__ = 'torres'
#-*- coding: utf-8-*-

class Person:
    name = 'none'  # public class variable
    sex = 'none'
                   # needed to be blank!
    def __init__(self, name, sex):
        self.name = name
        self.sex = sex

    def __repr__(self):
        return '<Person name : %s, sex :%s>' % (self.name, self.sex)


class Customer(Person, object):
    __id = 0         # private class variable
    __pay = 0
    def __init__(self, _name, _sex, _id, _purchase_list, _purchase_num, _purchase_price):
        Person.__init__(self, _name, _sex)
        self.__id = _id
        self.purchase = Purchase(_purchase_list, _purchase_num, _purchase_price)

    def __init__(self, person, _id, _purchase_list, _purchase_num, _purchase_price): # constructor overloading
        Person.__init__(self, person.name, person.sex)  # using object into constructor
        self.__id = _id
        self.purchase = Purchase(_purchase_list, _purchase_num, _purchase_price)

    def __repr__(self):
        person = Person.__repr__(self)
        purchase = Purchase.__repr__(self.purchase) # self.purchase!!
        return person + '<Customer id : %s >' % self.__id + purchase

    def get_pay(self):
        self.__pay = self.purchase.price()
        return self.__pay
    pay = property(get_pay)

    def get_id(self):
        return self.__id
    def set_id(self, _id):
        self.__id = _id
    id = property(get_id, set_id)  # object 상속


class Purchase:
    _purchase_list = 'none'  # protected class variable
    _purchase_num = 0
    _purchase_price = 0

    __slots__ = [_purchase_list, _purchase_num, _purchase_price]

    def __init__(self):
        self._purchase_list = 'none'
        self._purchase_num = 0
        self._purchase_price = 0

    def __init__(self, _purchase_list, _purchase_num, _purchase_price):
        self._purchase_list = _purchase_list
        self._purchase_num = _purchase_num
        self._purchase_price = _purchase_price

    def __repr__(self):
        return '<Purchase _purchase_list : %s, _purchase_num : %d, _purchase_price : %d>' % \
               (self._purchase_list, self._purchase_num, self._purchase_price)

    def price(self):
        return self._purchase_num * self._purchase_price


person1 = Person('woo', 'm')
person2 = Person('kim', 'w')
print person1
print person2

customer1 = Customer(person1, 1, 'banana', 5, 1000)
print customer1
customer1.id = 2
print customer1

print 'the result : ' + str(customer1.pay)  # int to string : str(int)




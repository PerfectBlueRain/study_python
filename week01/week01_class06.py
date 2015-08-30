__author__ = '1002475'

class Test(object):

    # !!!! setter/getter !!!!
    def __init__(self):
        self.__degree = 0

    def get_degree(self): #degree getter
        return self.__degree

    def set_degree(self, d): # degree setter
        self.__degree = d % 360

    degree = property(get_degree, set_degree)

    __slots__= ['name', 'phone', '__degree']

    def __call__(self):
        print "call called"



#test1 = Test()
#test1()
#test1.a = "Torres" # AttributeError: 'Test' object has no attribute 'a'
#test1.name = "Torres"

test2 = Test()
test2.degree = 10
print test2.degree
test2.degree = 350
print test2.degree
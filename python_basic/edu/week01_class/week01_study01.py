__author__ = '1002475'


class MyString :
    def __init__(self, str):
        self.str = str

    def __add__(self, str):
        # return self.str + str
        return self.str.join(str)
    def __sub__(self, str):
        self.str.find(str)

    def __coerce__(self, x):
        return self.str, x


m1 = MyString("test")
m2 = MyString("test")
print m1+m2
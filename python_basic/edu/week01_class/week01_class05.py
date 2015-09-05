__author__ = '1002475'

# 5) opeartor overloading


# __coerce__ : 두 수치(numeric) 인수를 공통 유형으로 변환하여 터플로 돌려준다.

class MyString:
    def __init__(self, str):
        self.str = str
    def __rdiv__(self, sep):    # using '/' char : override
        print '..starting split.. using :(', sep, ')'
        return self.str.split(sep)   # using split() in string
    def __div__(self, sep):    # using '/' char : override
        print '..starting split.. using :(', sep, ')'
        return self.str.split(sep)   # using split() in string

class MyNum:
    def __init__(self, n):
        self.n = n
    def __coerce__(self, y):
        return self.n, y


m = MyString("abefs.fesbfhj.sefbh")
print m / "."
print m / "b"
print "." / m  # TypeError -> so __rdiv__

a = MyNum(10)
print a + 20
print a * 30
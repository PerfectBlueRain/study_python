__author__ = '1002475'

#-*- coding: utf-8-*-
# 3)
class Var:
    c_mem = 100
    def f(self):
        self.i_mem = 200
    def g(self):
        print self.i_mem
        print self.c_mem


print Var.c_mem
v1 = Var()
v1.f()
print v1.c_mem
v2 = Var()
print v2.c_mem
v1.c_mem = 50
print v1.c_mem
print v2.c_mem
print Var.c_mem

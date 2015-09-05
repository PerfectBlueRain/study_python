__author__ = '1002475'
#-*- coding: utf-8-*-

# 변수
a = 37

# 함수
def foo():
    print("I am foo and a is %s" %a)
def bar():
    print("I am bar and I am calling foo %s")
    foo()

# 클래스
class Spam(object):
    def grok(self):
        print("I am spam.grok")



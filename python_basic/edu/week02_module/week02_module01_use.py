__author__ = '1002475'
#-*- coding: utf-8-*-

############################################
#  다른 파일에서 모듈을 사용하는
############################################

#import week02_module01_spam as spam # Loads and executes the module 'spam'
from python_study.python_basic.edu.week02_module.week02_module01_spam import bar #as spam
def foo():
    print("I am different foo")
bar()

x = spam.a # Accesses a member of module 'spam'
spam.foo() # Call a function in module 'spam'
s = spam.Spam() # Create an instance of spam.Spam() s.grok()


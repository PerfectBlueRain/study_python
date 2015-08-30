__author__ = '1002475'
# -*- coding: utf-8 -*-

class Animal:
    def cry(self):
        print '...'

class Dog(Animal):
    def cry(self):
        print 'bark bark '

class Duck(Animal):
    def cry(self):cd
        print 'duck duck'

class Fish(Animal):
    pass


for each in (Dog(), Duck(), Fish()):  # (Dog(), Duck(), Fish()) => tuple / each => object
   each.cry()
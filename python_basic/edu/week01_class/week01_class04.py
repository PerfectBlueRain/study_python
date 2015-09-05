__author__ = '1002475'

# 4) destructor
# __init__, __del__
# using time

from time import *
class Life:
    def __init__(self):
        self.birth = ctime()
        print 'Birthday', self.birth

    def __del__(self):
        print 'Deathday', ctime()

    
mylife = Life()
print 'sleeping for 3 sec'
sleep(3)

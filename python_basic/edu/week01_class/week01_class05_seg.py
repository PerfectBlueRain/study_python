__author__ = '1002475'

# types module
# map

import types

class Square:
    def __init__(self, end):
        self.end = end
    def __len__(self):
        return self.end
    def __contains__(self, key):
        return 0 <= key < self.end
    #def __getitem__(self, key):
    #    if key < 0 or self.end <= key:
    #        raise IndexError,key
    #    return key * key
    def __getitem__(self, key):
        if type(key) == type(0): # indexing
            if key < 0 or self.end <= key: raise IndexError, key
            return key * key
        elif type(key) == types.SliceType: # import types : slicing
            start = key.start or 0
            if key.stop > self.end: stop = self.end
            else: stop = key.stop
            step = key.step or 1
            return map(self.__getitem__, range(start, stop, step))   # map : type


s1 = Square(10)
print len(s1)
print 5 in s1 # s1.__contains__(5)
print s1[1] # s1.__getitem__(1)
print list(s1)
print tuple(s1)
print len(s1)

s = Square(10)
print s[4] #indexing
print s[1:5] #slicing
print s[1:10:2] # tab 2
print [1, 9, 25, 49, 81]
print s[:] #full
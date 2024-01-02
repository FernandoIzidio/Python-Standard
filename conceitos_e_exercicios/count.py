"""
Count é um iterator sem fim

"""
from itertools import count

c1 = count()
c2 = range(10)
c3 = []

print(hasattr(c1, '__iter__'))
print(hasattr(c1, '__next__'))
print(hasattr(c2, '__iter__'))
print(hasattr(c2, '__next__'))
print(hasattr(c2, '__iter__'))
print(hasattr(c2, '__next__'))

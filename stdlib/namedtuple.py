'''
https://docs.python.org/3/library/collections.html#namedtuple-factory-function-for-tuples-with-named-fields


'''

import collections
import sys

# print(*(i for i in dir(collections) if not i.startswith("_")), sep = "\n")

Point = collections.namedtuple('Point', ['x', 'y'])  # Returns a new tuple subclass named Point
print(Point)

p = Point(11, y=22)
print(p, hash(p), sys.getsizeof(p))
print(p[0:2], p.x, p.y)
print(*(i for i in dir(p) if not i.startswith("_")), sep = "\n")

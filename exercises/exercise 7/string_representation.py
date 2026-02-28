

import copy

class Point:
    def __init__(self, x, y):
        self._x = x
        self._y = y

    def __str__(self):
        return f'point({self._x}, {self._y})'

p = Point(1, 2)
print(p)
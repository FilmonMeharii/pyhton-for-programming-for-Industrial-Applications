

import copy

class Point:
    def __init__(self, x, y):
        self._x = x
        self._y = y
    def __str__(self):
        return f'point({self._x}, {self._y})'
    
    def move(self, dx, dy):
        self._x += dx
        self._y += dy
p = Point(3, 4)
print(p)
p.move(2, -1)
print(p)
        
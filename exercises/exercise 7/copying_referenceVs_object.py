import copy

class Point:
    def __init__(self, x, y):
        self._x = x
        self._y = y
    
    def __str__(self):
        return f"Point({self._x}, {self._y})"
    
    def move(self, delta_x, delta_y):
        self._x += delta_x
        self._y += delta_y

# Task 1: Reference copy
p = Point(6, 2)
q = p
print("Reference copy:")
print(p is q)  # True
q.move(1, 1)
print(f"p: {p}")  # Point(7, 3)
print(f"q: {q}")  # Point(7, 3)
print()

# Task 2: Shallow copy
p = Point(3, 7)
q = copy.copy(p)
print("Shallow copy:")
print(p is q)  # False
q.move(5, 5)
print(f"p: {p}")  # Point(3, 7)
print(f"q: {q}")  # Point(8, 12)
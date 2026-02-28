


class Point:
    def __init__(self, x, y):
        self._x = x
        self._y = y
    
    def __str__(self):
        return f"Point({self._x}, {self._y})"
    
    def move(self, delta_x, delta_y):
        self._x += delta_x
        self._y += delta_y
    
    def get_coords(self):
        return (self._x, self._y)  # Return as tuple

# Test:
p = Point(3, 4)
print(p.get_coords())  # (3, 4)
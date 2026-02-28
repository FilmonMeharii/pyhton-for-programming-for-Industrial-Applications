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
    
    def get_coords(self):
        return (self._x, self._y)

class Character:
    def __init__(self, name):
        self._name = name
        self._position = Point(0, 0)
    
    def rename(self, new_name):
        self._name = new_name
    
    def step_forward(self, step):
        self._position.move(step, 0)
    
    def __str__(self):
        return f'Character: {self._name} on position {self._position.get_coords()}'

# Task 1: Shallow copy
hero = Character('Python Man')
evil_twin = copy.copy(hero)

print("Shallow copy:")
print(hero is evil_twin)  # False
hero.step_forward(5)
print(hero)        # Character: Python Man on position (5, 0)
print(evil_twin)   # Character: Python Man on position (5, 0) - changed too!
print()

# Task 2: Deep copy
hero = Character('Python Man')
evil_twin = copy.deepcopy(hero)

print("Deep copy:")
hero.rename('Super Python')
hero.step_forward(10)
print(hero)        # Character: Super Python on position (10, 0)
print(evil_twin)   # Character: Python Man on position (0, 0) - unchanged!
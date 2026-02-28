
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

class Player(Character):
    def __init__(self, name, battle_cry):
        super().__init__(name)
        self._battle_cry = battle_cry
    
    def cry(self):
        print(self._battle_cry)
    
    def __str__(self):
        return f'Player: {self._name} on position {self._position.get_coords()}'

# Test both classes:
monster = Character('Shrek')
priest = Player('Priest', 'Wololo!')

print(monster)  # Character: Shrek on position (0, 0)
print(priest)   # Player: Priest on position (0, 0) - different format!

priest.cry()    # Wololo!
priest.step_forward(2)
print(priest)   # Player: Priest on position (2, 0)
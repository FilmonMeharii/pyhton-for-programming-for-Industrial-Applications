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

# Test:
hero = Player('Aragorn', 'For Gondor!')
print(hero)        # From Character class
hero.cry()         # From Player class
hero.step_forward(3)  # From Character class
print(hero)


# A class definition starts with the keyword class followed by the name of the class - capitalized by convention
class Pet:
    # The constructor: called by Python on object creation, the self parameter refers to the object being created
    def __init__(self, name, sound):
        # Define and initialize instance variables
        self._name = name
        self._sound = sound

    # Functions in a class are called methods
    def talk(self):
        # Methods can access instance variables
        print(f'{self._sound}. My name is {self._name}.')


# The class Dog inherits the class Pet, a Dog is a specialized Pet
class Dog(Pet):
    # The constructor can have a different set of parameters
    def __init__(self, name, sound, breed=None):
        # Call the constructor of the parent class explicitly
        super().__init__(name, sound)
        
        # Additional instance variables can be defined
        self._breed = breed
    
    # The child class implements its own version of the method - polymorphism
    def talk(self):
        # If no breed was given
        if self._breed is not None:
            print(f'{self._sound}. I am a {self._breed} and my name is {self._name}.')
        else:        
            print(f'{self._sound}. I am a dog and my name is {self._name}.')
    
    # The child class can define its own methods
    def bark(self):
        print(f'Wooooof! {self._sound}')

# Run the code below only if the module is run as a script (i.e. not imported)
if __name__ == '__main__':
    # Create an object of the Pet class
    cat = Pet('Lizzie', 'Meow')
    cat.talk()
    
    # Create an object of the Dog class
    labradoodle = Dog('Doodie', 'Woof', 'labradoodle')
    labradoodle.talk()

    # Create a different object of the Dog class
    dog = Dog('Fido', 'WOOF')
    dog.talk()
    dog.bark()

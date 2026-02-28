

import copy

class SortedList:
    #Constructor: Called on object creation
    def __init__(self):
        #Define and initialize a list: Composition - an object of the class *has a* list
        self._L = []

        #Restrict access to the data
    def add(self, item):
        #Add the item to the list
        self._L.append(item)
        #keep the list sorted
        self._L.sort()

        #Define a magic method that is used by Pyhon when printing an object of the class
    def __str__(self):
        #return a string representation of the list
        return str(self._L)
    
# Run the code below only if the module is run as a script (i.e. not imported)
if __name__ == '__main__':
# Create an instance of the class
    sl = SortedList()
    
    # Add some items
    sl.add(5)
    sl.add(2)

    # Print the list
    print(sl)       

    # Make a (shallow) copy of the list
    sl2 = copy.copy(sl)
    
    # Add an element to the copy
    sl2.add(1)
        
    # Add an element to the original
    sl.add(3)
        
    # Print the two objects
    print(sl)
    print(sl2)
    print()

    # We note that the elements have been added to *both* lists
    # The list itself has not been copied, only the reference
    print(sl._L is sl2._L)
        
    # Make a new attempt
    sl3 = copy.deepcopy(sl)
    # Add elements
    sl.add(13)
    sl2.add(42)
    sl3.add(90)
        
    # Print the new copy
    print(sl3)
    # This time, the elements added to the original (and the shallow copy) were *not* added to the deep copy

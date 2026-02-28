from datetime import date, datetime

class Extinguisher:
    def __init__(self, extinguisher_type, manufacturing_date):
        self._type = extinguisher_type.lower()
        self._manufacturing_date = datetime.strptime(manufacturing_date, '%Y-%m-%d').date()
    
    def has_expired(self):
        today = date.today()
        
        # Determine lifetime based on type
        if self._type == 'water':
            lifetime = 12
        elif self._type == 'powder':
            lifetime = 10
        elif self._type == 'foam':
            lifetime = 5
        else:
            return False  # Unknown type
        
        # Calculate expiration date
        expiration_year = self._manufacturing_date.year + lifetime
        expiration_date = date(expiration_year, 
                               self._manufacturing_date.month, 
                               self._manufacturing_date.day)
        
        return today > expiration_date
    
    def get_type(self):
        return self._type


if __name__ == '__main__':
    extinguisher_type = input("Type? ")
    manufacturing_date = input("Manufacturing date? ")
    
    extinguisher = Extinguisher(extinguisher_type, manufacturing_date)
    
    if extinguisher.has_expired():
        print("Expired")
    else:
        print("Not expired")
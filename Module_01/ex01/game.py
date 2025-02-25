class GotCharacter:
    def __init__(self, first_name):
        self.first_name = first_name
        self.is_alive = True
        
class Stark(GotCharacter):
    def __init__(self, first_name=None, is_alive=True):
        super().__init__(first_name=first_name, is_alive=is_alive)
        self.family_name = "Stark"
        self.house_words = "Winter is Coming"
        
class Lannister(GotCharacter):
    def __init__(self, first_name=None, is_alive=True):
        super().__init__(first_name=first_name, is_alive=is_alive)
        family_name = "Lannister"
        house_words = "Hear Me Roar!"

class Targaryen(GotCharacter):
    def __init__(self, first_name=None, is_alive=True):
        super().__init__(first_name=first_name, is_alive=is_alive)
        family_name = "Targaryen"
        house_words = "Fire and Blood"
    
class Baratheon(GotCharacter):
    def __init__(self, first_name=None, is_alive=True):
        super().__init__(first_name=first_name, is_alive=is_alive)
        family_name = "Baratheon"
        house_words = "Ours is the Fury"
    
class Greyjoy(GotCharacter):
    def __init__(self, first_name=None, is_alive=True):
        super().__init__(first_name=first_name, is_alive=is_alive)
        family_name = "Greyjoy"
        house_words = "We Do Not Sow"
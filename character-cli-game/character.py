#
#  PSP Assignment 2 - Provided module character.py (for part II).
#
#  class Character
#
#  DO NOT modify this file.
#


class Character:

    # The __init__ method initializes the data members/attributes of the Character class
    def __init__(self, name='', secret_identity='', is_hero=True, no_battles=0, no_won=0, no_lost=0,
                       no_drawn=0, health=100):
        self.__name = name
        self.__secret_identity = secret_identity
        self.__is_hero = is_hero
        self.__no_battles = no_battles
        self.__no_won = no_won
        self.__no_lost = no_lost
        self.__no_drawn = no_drawn
        self.__health = health
        

    def set_name(self, name):
        self.__name = name
        
    def get_name(self):
        return self.__name

    def set_secret_identity(self, secret_identity):
        self.__secret_identity = secret_identity
        
    def get_secret_identity(self):
        return self.__secret_identity

    def set_is_hero(self, hero):
        self.__is_hero = hero

    def get_is_hero(self):
        return self.__is_hero

    def set_no_battles(self, no_battles):
        self.__no_battles = no_battles

    def get_no_battles(self):
        return self.__no_battles

    def increment_no_battles(self, battle=1):
        self.__no_battles += battle

    def set_no_won(self, won):
        self.__no_won = won

    def get_no_won(self):
        return self.__no_won

    def increment_no_won(self, won=1):
        self.__no_won += won

    def set_no_lost(self, lost):
        self.__no_lost = lost

    def get_no_lost(self):
        return self.__no_lost

    def increment_no_lost(self, lost=1):
        self.__no_lost += lost

    def set_no_drawn(self, drawn):
        self.__no_drawn = drawn

    def get_no_drawn(self):
        return self.__no_drawn

    def increment_no_drawn(self, drawn=1):
        self.__no_drawn += drawn

    def set_health(self, health):
        self.__health = health

    def get_health(self):
        return self.__health

    def update_health(self, damage=0):
        self.__health -= damage
        if self.__health < 0:
            self.__health = 0

    # The __str__ method returns a string representation of the character object
    def __str__(self):
        string  = format(self.__name, '25s') 
        string += format(self.__no_battles, '3d')  
        string += format(self.__no_won, '3d')  
        string += format(self.__no_lost, '3d')  
        string += format(self.__no_drawn, '3d') 
        string += format(self.__health, '8d')   
        return string

    # The __eq__ method allows for a test for equality (is equal to) on name i.e. == operator.
    def __eq__(self, name):
        if self.__name == name:
            return True
        elif self.__name != name:
            return False
        return NotImplemented
     
    
        

    

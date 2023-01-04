class Restaurant():
    """A class representing a restaurant"""

    def __init__(self, name, cuisine_type):
        """Initialize the restaurant"""
        self.name = name.title()
        self.cuisine_type= cuisine_type

    def describe_restaurant(self):
        """Display a summary of the restaurant."""
        msg = (f"{self.name} nasza restauracja podaje wspaniały {self.cuisine_type}.")
        print (f"\n{msg}")

    def open_restaurant(self):
        """Display a message that the restaurant is open."""
        msg =(f"{self.name} codziennie otwarta od 7:00-19:00!")
        print (f"\n{msg}")
class IceCreamStand(Restaurant):
    """Subclass for icecream stand"""
    def __init__ (self, name, cuisine_type = 'lody'):
        super(). __init__(name, cuisine_type)
        self.flavors = []
    
    def show_flavors (self):
        print (f" W naszym stanowisku z lodami mamy różne smaki.")
        for flavor in self.flavors:
            print (f"- {flavor.title()}")

icecream_stand = IceCreamStand('krasnolud')
icecream_stand.flavors = ['waniliowe','truskawkowe','czekoladowe']

icecream_stand.describe_restaurant()
icecream_stand.show_flavors()

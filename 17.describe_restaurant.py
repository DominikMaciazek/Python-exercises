class Restaurant():
    """A class representing a restaurant"""

    def __init__(self, name, cuisine_type):
        """Initialize the restaurant"""
        self.name = name.title()
        self.cuisine_type= cuisine_type

    def describe_restaurant(self):
        """Display a summary of the restaurant."""
        msg = (f"{self.name} nasza restauracja piecze wspaniały {self.cuisine_type}.")
        print (f"\n{msg}")
    def open_restaurant(self):
        """Display a message that the restaurant is open."""
        msg =(f"{self.name} codziennie otwarta od 7:00-19:00!")
        print (f"\n{msg}")

restaurant = Restaurant ('Chleboteka', 'chleb')


restaurant.describe_restaurant()
restaurant.open_restaurant ()

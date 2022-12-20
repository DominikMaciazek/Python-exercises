class User():
    """klasa przechowywująca dane o użytkowniku"""
    def __init__(self, first_name, last_name, nick_name, password):
        self.first_name = first_name.title()
        self.last_name = last_name.title()
        self.nick_name = nick_name
        self.password = password

    def describe_user(self):
        print (f"\n Oto nasz nowy użytkownik {self.first_name} {self.last_name}")
        print (f"Posiada on swój własny nick {self.nick_name} oraz hasło {self.password}")

    def greet_user(self):
        print (f"Witaj {self.first_name} {self.last_name}")

class Admin(User):
    def __init__ (self, first_name, last_name, nick_name, password):
        super().__init__ (first_name, last_name, nick_name, password,)
        self.privileges = []

    def show_privileges(self):
        print ('Nasz admin ma specjalne funkcje:')
        for privilege in self.privileges:
            print (f" {privilege}")

dominik = Admin ('Dominik','Maciazek', 'frodo','ooodeefr')

dominik.describe_user()

dominik.privileges = [
    '\n-może dodać post'
    '\n-może usunąć post'
    '\n-może zbanować użytkownika']

dominik.show_privileges()
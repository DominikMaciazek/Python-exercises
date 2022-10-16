def make_pizza (size,*toppings):
    """Wyświetla przygotowanie pizzy i dodatki"""
    print (f"Zamówiłeś pizzę w rozmiarze {size} z następującymi dodatkami:")
    for topping in toppings:
         print (f"- {topping}")


make_pizza ('55','pieczarki','ser','szpinak')

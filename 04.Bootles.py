def containers():
    num = float(input("How many bootles you have:"))
    bootle = float(input('Enter size your bootle:'))
    big = 0.25
    small = 0.10
    if bootle >= 1:
        print (f"It's your money $ {num * big}")
    else:
        print (f"It's your money $ {num* small}")


containers()

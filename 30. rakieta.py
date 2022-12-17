import random
x = random.randint (1,10)

import time
print ('Uwaga za chwile odliczanie')
time.sleep (1)
print ('4')
time.sleep (1)
print ('3')
time.sleep (1)
print ('2')
time.sleep (1)
print ('1')
time.sleep (1)
print ('START')
x = random.randint (1,5)
while True:
    y = input ('Zgadnij liczbę: ')
    if int(y) == x:
        print ('Doskonale')
        break
    if int(y) < x:
        print ('za mało')
    if int(y)> x:
        print ('za dużo')

numbers = [ 1,2,0,0,5,0,1,4,6,7,0,0,4,0,6,0]

def zero_place(numbers):
    for _ in range(numbers.count(0)):
        numbers.remove(0)
        numbers.append(0)


zero_place(numbers)
print (numbers)
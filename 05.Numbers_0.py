# Write a Python program to move all zero digits to end of a given list of numbers.


# first solution

numbers = [ 1,2,0,0,5,0,1,4,6,7,0,0,4,0,6,0]

def zero_place(numbers):
    for _ in range(numbers.count(0)):
        numbers.remove(0)
        numbers.append(0)


zero_place(numbers)
print (numbers)


#second solution

def zero_place2 (numbers):
    numbers.sort(key = lambda element:element is 0)

print (numbers)

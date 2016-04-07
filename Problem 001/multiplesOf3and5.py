# multiplesOf3and5.py Sums up all multiples of 3 and 5 below the number
# TODO: Funtion to sum up the multiples
def sumOfMultiples (target):
    Sum = 0
    for i in range(target):
        if not i % 3 or not i % 5:
            Sum = Sum + i
    print(Sum)

sumOfMultiples(1000)

# TODO: Ask for a target

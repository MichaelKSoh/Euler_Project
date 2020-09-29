targetNum = 100

def sumOfSquares(num):
    counter=0
    for i in range(1,num+1):
        counter += i**2
    return counter

print(sumOfSquares(targetNum))

def SquareOfSum(num):
    counter = 0
    for i in range(1,num+1):
        counter += i
    return (counter**2)

print(SquareOfSum(targetNum))

print((SquareOfSum(targetNum)) - (sumOfSquares(targetNum))) 
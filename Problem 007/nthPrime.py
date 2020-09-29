targetNum = 2

def primeTest(x):
    for i in range(2,x):
        if (x%i) == 0:
            return False
    else:
        return True

def nthPrime(x):
    counter=2
    num = 3
    while counter != x:
        num +=2
        if primeTest(num)==True:
            counter += 1

    return num

# print(primeTest(9))
print(nthPrime(10001))
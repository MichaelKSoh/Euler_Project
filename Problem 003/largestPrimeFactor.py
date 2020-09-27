## Finds the largest prime factor of a number
import math

InputNum = int(input("Enter the number: "))
target = int(math.sqrt(InputNum))
print(target)


def primeTest(x):
    for i in range(2,x):
        if (x%i) == 0:
            return False
    else:
        return True


for i in range(target,2,-1):
    if (InputNum % i) == 0:
        ## Then we know that i is a multiple
        if primeTest(i):
            print(i, "is the largest prime factor")
            break
        else:
            continue
    else:
        continue

## Got the answer right, but this was really hacky. Will need to revisit at a later time to clean up the code

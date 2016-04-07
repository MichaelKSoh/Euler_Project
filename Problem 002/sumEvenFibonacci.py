# sumEvenFibonacci.py
# script to all the even Fibonacci numbers under a target

initList = [1, 2]
while initList[-1] + initList[-2] < 4000000:
    initList.append(initList[-1] + initList[-2])

evenList = []

for i in initList:
    if not i % 2:
        evenList.append(i)

print(evenList)
print(sum(evenList))

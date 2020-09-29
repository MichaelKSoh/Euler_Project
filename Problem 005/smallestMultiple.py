def smallestMultiple(num):
    for i in range(2, 21):
        if (num%i) != 0:
            return False
    return True

num=2520

while smallestMultiple(num) == False:
    num += 2520
    print(num)

print(num, "is the smallest multiple")


def CheckPalindrome(string): 
    list1=[] 
    list1[:0]=string 
    list2=[]
    list2=list1.copy()
    list2.reverse()
    return list1 == list2


for i in range(999,900,-1):
    for j in range(999,1,-1):
        product = str(i*j)
        if CheckPalindrome(product):
            print(product, "is the largest palindrome product")
            break
        else:
            continue
            
print("No palindrome found")

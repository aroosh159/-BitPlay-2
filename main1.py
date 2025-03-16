def OddOccuring(arr):
    res = 0
    for element in arr:
        res = res ^ element
    return res

arr = []
n= int(input("enter your array sizes"))
while(n):
    num= int(input("enter number"))
    arr.append(num)
    n-=1
print("OddOccuring number is ",OddOccuring(arr))
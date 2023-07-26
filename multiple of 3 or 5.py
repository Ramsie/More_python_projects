def multi_3or5(n):
    sum=0
    for i in range(1,n):
        if i%3==0 or i%5==0:
            sum+=i
    return sum


m=int(input("enter value of n "))
print(multi_3or5(m))
def fibonacci(max):
    i=1
    fib_list = [1]
    sum_even=0
    while(i<max):
        fib_list.append(i)
        i=fib_list[-1]+fib_list[-2]
    for j in fib_list:
        if j%2==0:
            sum_even+=j
    return sum_even

m=int(input("enter max number"))
print(fibonacci(m))
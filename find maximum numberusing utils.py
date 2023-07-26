numbers=[]

n=int(input("number of numbers"))
for i in range(n):
    l=int(input())
    numbers.append(l)
import utils
maximum_number=utils.find_max(numbers)
print(maximum_number)


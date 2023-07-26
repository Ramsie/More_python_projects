numbers=[4,5,2,12,7,1,9]
largest=0
i=0
while(i<7):
    if numbers[i]>largest:
        largest=numbers[i]
    i+=1
print(largest)
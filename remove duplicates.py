list=[5,2,5,3,6,8]
list2=[]
for item in list:
    if not item in list2:
        list2.append(item)
print(list2)
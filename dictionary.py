dict={
    "1":"One",
    "2":"Two",
    "3":"three",
    "4":"four"
}
x=(input("pHONE"))
y=""
for item in x:
    z=dict.get(item)
    y+=z+" "
print(y)


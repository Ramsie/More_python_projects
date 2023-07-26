emojis={
    ":)":"😊",
":(":"😒"
}
input=input()
for item in input:
    words=input.split(' ')
print(words)
y=""
for ch in words:
    y+=emojis.get(ch,ch)+" "
print(y)
def emoji_converter(message):
    emojis={
        ":)":"😊",
    ":(":"😒"
    }
    for item in message:
        words=message.split(' ')
    y=""
    for ch in words:
        y+=emojis.get(ch,ch)+" "
    return y
user_message=input()
result=emoji_converter(user_message)
print(result)
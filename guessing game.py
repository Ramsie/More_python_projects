secret_number = 9
guess_count=1
guess_limit=4

while guess_count<guess_limit:
    x = int(input("Guess : "))
    guess_count+=1
    if x==secret_number:
        print("You win")
        break
else:
    print("you failed")

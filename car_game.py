started=False
while True:
    user_command=input(">")
    if user_command=="help" :
        print("""start-to start car
        stop-to sto car
        quit- to exit""")
    elif user_command=="start":
        if started:
            print( "car already started")
        else:
            started=True
            print("car is start")
    elif user_command=="stop":
        if not started:
            print("car is already stopped")
        else :
            started=False
            print ("car is stopped")
    elif user_command=="quit":
          break
    else:
        print("i don't understand")
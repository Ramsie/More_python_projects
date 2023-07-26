class Parent:
    def walk(self):
        print("walk")

    def talk(self):
        print("talk")


class Boy(Parent):
    def play(self):
        print("play hockey")


class Girl(Parent):
    def dance(self):
        print("belly dance")


raman=Girl()
raman.dance()
raman.talk()
raman.walk()

taj=Boy()
taj.play()
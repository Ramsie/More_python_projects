import random
class Dice:
    def roll(self):
        return random.randint(1,6)


dice1=Dice()
x=dice1.roll()
dice2=Dice()
y=dice2.roll()
print(f'({x},{y})')
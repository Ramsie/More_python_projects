class Point:
    def draw(self):
        print("draw")
    def move(self):
        print("move")


point1=Point()
point1.draw()
point1.move()
point1.x=10
print(point1.x)
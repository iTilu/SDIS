import turtle


class PythagorasTree:

    def __init__(self, size=200, posx=-100, posy=-200, angle=0, speed=0):
        self.t = turtle.Turtle()
        self.t.speed(speed)
        self.size = size
        self.startposx = posx
        self.startposy = posy
        self.startangle = angle

    def square(self, size, posx, posy, angle):
        self.t.penup()
        self.t.goto(posx, posy)
        self.t.seth(angle)
        self.t.pendown()
        for i in range(4):
            self.t.forward(size)
            self.t.right(90)

    def build_fractal(self, size, posx, posy, angle, depth, ratio=1 / 2 ** 0.5):
        if depth == 0:
            return

        self.t.pendown()
        self.square(size, posx, posy, angle)

        if depth > 1 and size > 1:
            childsize = size * ratio
            self.t.left(135)
            self.t.up()
            self.t.forward(childsize)
            self.t.right(90)
            self.build_fractal(childsize, self.t.xcor(), self.t.ycor(), angle + 45, depth - 1)

            self.t.seth(angle)
            self.t.up()
            self.t.goto(posx, posy)
            self.t.forward(size)
            self.t.left(135)
            self.t.forward(childsize)
            self.t.right(90)
            self.t.forward(childsize)
            self.build_fractal(childsize, self.t.xcor(), self.t.ycor(), angle - 45, depth - 1)

    def draw(self, depth):
        self.build_fractal(self.size, self.startposx, self.startposy, self.startangle, depth)


tree = PythagorasTree(200, -100, -200, 0)
tree.draw(7)
turtle.mainloop()

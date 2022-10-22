import turtle as t
import math


class Building1:

    def __init__(self, color, x, y):
        self.width = 50
        self.radius = 12
        self.length_arch = 15
        self.width_arch = 10
        self.color = color
        self.x = x
        self.y = y

    def draw(self):
        t.pencolor(self.color)
        t.setheading(0)
        t.penup()
        t.setpos(self.x, self.y)
        t.pendown()
        for i in range(2):
            # Draw outline of the building(rectangle)
            t.fd(self.width)
            t.lt(90)
            t.fd(self.width * 2)
            t.lt(90)
        t.lt(90)
        t.fd(self.width / 2)
        t.right(90)
        t.penup()
        t.fd(self.width / 10)
        t.pendown()

        self.draw_windows()
        self.draw_triangle()
        self.draw_arch()
        self.draw_decor()

    def draw_windows(self):
        for i in range(2):
            # small rectangle 40 by 70 for the grid windows
            t.fd(self.width - 10)
            t.lt(90)
            t.fd(self.width * 2 - 30)
            t.lt(90)
        t.lt(90)
        for i in range(7):
            # starting to make the grid windows (left to right)
            t.fd(self.width / 5)
            t.rt(90)
            t.fd(self.width - 10)
            t.bk(self.width - 10)
            t.lt(90)
        t.bk(self.width * 2 - 30)
        t.rt(self.width * 2 - 10)
        for i in range(8):
            # making the grid windows (up and down)
            t.fd(self.width / 10)
            t.lt(90)
            t.fd(self.width * 2 - 30)
            t.bk(self.width * 2 - 30)
            t.rt(90)
        t.penup()
        t.lt(90)
        t.forward(self.width * 1.5)
        t.pendown()

    def draw_triangle(self):
        for i in range(2):
            # making the very top tiny rectangle
            t.fd(self.width / 10)
            t.lt(90)
            t.fd(self.width - 10)
            t.lt(90)
        # make the top circle
        t.fd(self.width / 10)
        t.lt(90)
        t.fd(7.5)
        t.seth(90)
        t.circle(self.radius, 180)
        t.lt(90)
        t.fd(self.radius)
        t.lt(90)
        # making the top line on the tower
        t.penup()
        t.fd(self.radius)
        t.pendown()
        t.fd(self.width_arch)
        t.penup()
        t.bk(127)
        t.left(90)
        t.pendown()

    def draw_arch(self):
        # creating the left arch on the bottom
        t.fd(self.width - 30)
        t.rt(90)
        for i in range(2):
            t.fd(self.length_arch)
            t.rt(90)
            t.fd(self.width_arch)
            t.rt(90)
        # # creating middle arch on the bottom
        t.rt(90)
        t.fd(self.length_arch)
        for i in range(2):
            t.fd(self.width_arch)
            t.lt(90)
            t.fd(self.length_arch)
            t.lt(90)
        # # creating right arch on the bottom
        t.fd(self.length_arch)
        for i in range(2):
            t.fd(self.width_arch)
            t.lt(90)
            t.fd(self.length_arch)
            t.lt(90)

    def draw_decor(self):
        t.lt(90)
        t.fd(10)


class Building2:

    def __init__(self, color, x, y):
        self.width = 75
        self.color = color
        self.x = x
        self.y = y

    def draw(self):
        # dimensions - width:75      height:
        t.penup()
        t.goto(-45, -50)
        t.pendown()
        t.setheading(0)
        t.pencolor(self.color)

        self.draw_steps()
        self.draw_outline()
        self.draw_top()
        # self.draw_decor()

    def draw_steps(self):
        for i in range(2):
            # This is for the very bottom step of the building
            t.fd(55)
            t.lt(90)
            t.fd(3)
            t.lt(90)
        # This is for the second step for the building
        t.lt(90)
        t.fd(3)
        t.rt(90)
        t.fd(2.5)
        for i in range(2):
            t.fd(50)
            t.lt(90)
            t.fd(3)
            t.lt(90)

    def draw_outline(self):
        # starting the outline for the outside part of the building
        t.lt(90)
        t.fd(3)
        t.rt(90)
        t.fd(5)
        for i in range(3, 1, -1):
            t.setheading(90)
            t.fd(50 * (i * 0.25))
            t.setheading(30)
            t.fd(30 * (i * 0.25))
            t.setheading(-30)
            t.fd(30 * (i * 0.25))
            t.setheading(-90)
            t.fd(50 * (i * 0.25))
            t.setheading(180)
            t.fd(30 * math.sqrt(2) * (i * 0.25) + 1)

    def draw_top(self):
        #doing the top part of the building
        t.penup()
        t.rt(90)
        t.fd(45)
        t.pendown()
        t.fd(30)
        t.seth(30)
        t.fd(12)
        t.seth(-30)
        t.fd(12)
        t.seth(-90)
        t.fd(32)
        t.bk(37)
        t.seth(130)
        t.fd(16)
        t.seth(230)
        t.fd(22)
        t.seth(-90)
        t.penup()
        t.fd(75)
        t.pendown()
        t.lt(90)
        t.fd(10)
        #starting the inside decoration
    def draw_decor(self):
        t.lt(90)
        t.fd(10)
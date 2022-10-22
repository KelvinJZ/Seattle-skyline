import turtle as t


class Background:

    def __init__(self, color):
        self.color = color

    def draw_mountain(self, x, y):
        t.penup()
        t.setpos(x, y)
        t.pendown()
        t.fillcolor(self.color)
        t.begin_fill()
        angle = 45
        t.seth(angle)
        t.fd(100)
        t.rt(angle * 2)
        t.fd(100)
        t.rt(angle * 3)
        t.fd(140)
        t.end_fill()

    def draw_rock(self):
        t.fillcolor(self.color)
        t.begin_fill()
        t.circle(20)
        t.end_fill()



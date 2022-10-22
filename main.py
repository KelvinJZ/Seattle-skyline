import turtle as t
import random
from background import *
from buildings import *

t.speed(99)


#---Frame---
def draw_frame():
    t.penup()
    t.goto(-200, 200)
    t.pendown()
    t.color('gold')
    t.pensize(20)
    for i in range(2):
        t.fd(400)
        t.rt(90)
        t.fd(300)
        t.rt(90)


draw_frame()

# ---Painting---
t.pensize(1)

random_x = [random.randint(-180, 100) for i in range(5)]
random_y = [random.randint(-30, 60) for i in range(5)]

background = Background("blue")
background.draw_mountain(random_x[0], random_y[0])
background.draw_mountain(random_x[1], random_y[1])
background.draw_rock()

building1_1 = Building1("green", random_x[2], random_y[2])
building1_1.draw()

building1_2 = Building1("orange", random_x[3], random_y[3])
building1_2.draw()

building2_1 = Building2("red", random_x[4], random_y[4])
building2_1.draw()


#---Label---
def draw_label():
    t.penup()
    t.goto(-80, -120)
    t.pendown()
    t.pencolor('darkgrey')
    t.setheading(0)
    for i in range(2):
        t.fd(160)
        t.rt(90)
        t.fd(100)
        t.rt(90)

    t.penup()
    t.goto(-75, -150)
    t.pendown()
    t.pencolor('black')
    t.write('Seattle Skyline', font=("Helvetica", 10, "bold"))
    t.penup()
    t.rt(90)
    t.fd(15)
    t.pendown()
    t.write('python, 1986', font=("Helvetica", 8, 'italic'))
    t.penup()
    t.fd(15)
    t.pendown()
    t.write('color on code', font=("Helvetica", 8, 'normal'))
    t.penup()
    t.fd(30)
    t.pendown()

    price = random.getrandbits(40)
    t.write(f'${price}', font=("Helvetica", 12, 'italic', 'bold'))


draw_label()
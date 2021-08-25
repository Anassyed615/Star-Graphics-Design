## Amazing Star Design Using Python Turtle

## Python Graphics

import turtle

col = ('red','green','cyan','yellow','blue','white')

t = turtle.Turtle()
s = turtle.Screen()
s.bgcolor('black')
t.speed(15)

for i in range(150):
    t.color(col[i%6])
    t.forward(i*4)
    t.left(150)
    t.width(2)
import turtle as tao
from turtle import *

tao.bgcolor('black')
tao.speed(5)

begin_fill()
tao.color("#9c5c3d")
tao.circle(100)
end_fill()

tao.penup()
tao.left(90)
tao.forward(30)
tao.right(90)
tao.pendown()

begin_fill()
tao.color("#5e3019")
tao.circle(50)
end_fill()

tao.penup()
tao.right(90)
tao.forward(30)
tao.left(150)
tao.forward(180)
tao.right(90)
tao.pendown()

begin_fill()
tao.color('#9c5c3d')
tao.circle(50)
end_fill()

tao.penup()
tao.left(210)
tao.forward(198)
tao.right(180)
tao.pendown()

begin_fill()
tao.color('#9c5c3d')
tao.circle(50)
end_fill()

tao.penup()
tao.forward(80)
tao.pendown()

begin_fill()
tao.color('black')
tao.circle(10)
end_fill()

tao.penup()
tao.forward(50)
tao.pendown()

begin_fill()
tao.color('black')
tao.circle(10)
end_fill()

tao.done()
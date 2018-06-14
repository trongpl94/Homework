from turtle import *
color = ['red','blue','brown','yellow','grey']
shape("turtle")
def square():
        pencolor(color[1])#lay mau cam
        for i in range(0, 4):
                forward(100)
                left(90)
        left(60)#quay goc 60 do de ve tam giac
def triangle_pentagon():
        pencolor(color[0])#lay mau xanh
        for j in range(0, 2):
                forward(100)
                right(120)
        right(108)# quay goc 108 do de ve ngu giac
        pencolor(color[3])
        for k in range(0, 4):
                forward(100)
                left(72)
        left(120)# quay goc 120 do de ve luc giac
def hexagon():
        pencolor(color[4])#lay mau do
        for e in range(0, 6):
                forward(100)
                right(60)
square()
triangle_pentagon()
hexagon()

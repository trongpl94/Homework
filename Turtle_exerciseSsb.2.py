from turtle import * #Long
shape("turtle")
color1 = ['red','blue','brown','yellow','grey']
for j in range(0, 5):
 for i in range(0, 2):
     color(color1[j])
     begin_fill()
     forward(50)
     left(90)
     forward(100)
     left(90)
     end_fill()
 forward(50)


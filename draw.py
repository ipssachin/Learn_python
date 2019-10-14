#lets draw something

import turtle   #imported turtle library in the program/script
tin = turtle    #assigned turtle class to tin variable
tin.shape('turtle') #shape is a function of turtle class which takes argument and
                    #and shape pointer accordingly
# tin.forward(50)
# tin.left(45)
# tin.penup()
# tin.forward(100)
# tin.pendown()
# tin.circle(40)

#print octogon

for i in range(0,5):
    tin.fillcolor('green')
    tin.begin_fill()
    tin.forward(50)
    tin.left(45)
    tin.forward(50)
    tin.left(45)
    tin.end_fill()

#print square
tin.left(90)
tin.penup()
tin.forward(250)
tin.pendown()
for i in range(0,5):
    tin.forward(50)
    tin.left(90)
    # tin.forward(50)
    # tin.left(45)

#draw triangle

tin.penup()
tin.left(180)
tin.forward(50)
tin.pendown()

tin.forward(50)
tin.right(90)
tin.forward(50)
tin.right(135)
tin.forward(70)
#
#
#print cicle
tin.left(190)
tin.penup()
tin.forward(250)
tin.pendown()
tin.fillcolor('red')
tin.begin_fill()
tin.circle(50)
tin.end_fill()
#
# for i in range(0,10):
#     tin.circle(50)
#     tin.left(45)
#
# #print straight lines
# tin.right(190)
# tin.left(90)
# tin.penup()
# tin.forward(50)
# tin.pendown()
# tin.forward(50)
# tin.penup()
# tin.forward(50)
# tin.pendown()
# tin.penup()
# tin.forward(50)
# tin.pendown()
# tin.penup()
# tin.forward(50)
# tin.pendown()
# tin.penup()
# tin.forward(50)
# tin.pendown()
# tin.penup()
# tin.forward(50)
# tin.pendown()
#

input()

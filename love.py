import turtle

al = turtle.Turtle()

turtle.Screen().bgcolor('Yellow')
turtle.pensize(4)
al.speed (30)

def drawcurve():
    for i in range(200):
        al.right(1)
        al.forward(1)

def txt():
    al.up()
    al.setpos(-68,88)
    al.down()
    al.color('white')
    al.write ("Aku Cinta Kamu", font=("Verdana",12,"bold"))

al.color('red')
al.begin_fill()
al.left(140)
al.forward(111.65)
drawcurve()
al.left(120)
drawcurve()
al.forward(111.65)
al.end_fill()
al.penup()
al.goto(77,-40)
al.pendown()
al.hideturtle()
txt()
turtle.done()


import turtle
turtle.bgcolor("black")
t = turtle.Pen()
colors = ["red", "yellow", "blue", "green", "purple", "orange"]
sides = eval(input("Enter a number of sides between 2 and 6: "))
for x in range(360):
    t.pencolor(colors[x%sides])
    t.forward(x * 3/sides + x)
    t.left(360/sides + 1)
    t.width(x*sides/200)
    t.left(90)


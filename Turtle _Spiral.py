import turtle

screen = turtle.Screen()
screen.bgcolor("black")
screen.title("turtle spiral")

pen = turtle.Turtle()
pen.speed(0)
pen.width(2)

colors = ["purple", "blue", "green", "yellow", "orange", "red"]

for i in range(250):
    pen.color(colors[i % 6])
    pen.forward(i * 2)
    pen.right(59)

screen.exitonclick()


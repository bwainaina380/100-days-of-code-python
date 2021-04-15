from turtle import Turtle, Screen

timmy = Turtle()
screen = Screen()

def go_forwards():
    timmy.forward(10)

screen.listen()
screen.onkey(key="space", fun=go_forwards)
screen.exitonclick()
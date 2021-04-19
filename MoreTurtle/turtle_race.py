from turtle import Turtle, Screen
from random import randint

has_race_started = False
screen = Screen()
screen.setup(width=500, height=400)
player_bet = screen.textinput(title="Which turtle do you bet on?", prompt="Enter your turtle: ")
turtle_colors = ["orange", "red", "green", "yellow", "purple", "blue"]

every_turtle = []

y_positions = [-70, -40, -10, 20, 50, 80]

for turtle in range(0, 6):
    tabby = Turtle(shape="turtle")
    tabby.color(turtle_colors[turtle])
    tabby.penup()
    tabby.goto(x=-230, y=y_positions[turtle])
    every_turtle.append(tabby)

if player_bet:
    has_race_started = True

while has_race_started:
    for turtle in every_turtle:
        if turtle.xcor() > 230:
            has_race_started = False
            winning_color = turtle.pencolor()
            if winning_color == player_bet:
                print(f"You won. The {winning_color} is the winner")
            else:
                print(f"You lost. The {winning_color} is the winner.")
        distance = randint(0, 10)
        turtle.forward(distance)

screen.exitonclick()

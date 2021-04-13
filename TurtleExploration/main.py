from turtle import Turtle, Screen

def create_turtle():
    turtle_tom = Turtle()
    turtle_tom.shape("turtle")
    turtle_tom.color("orange")
    return turtle_tom

def draw_shapes(num_sides, turtle_instance):
    for side in range(1, num_sides):
        turtle_instance.forward(30)
        angle = int(360/num_sides)
        turtle_instance.setheading(angle)

draw_shapes(10, create_turtle())

screen = Screen()
screen.exitonclick()
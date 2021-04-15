from turtle import Turtle, Screen

class EtchASketch:
    def __init__(self):
        self.turtle = Turtle()
        self.screen = Screen()
        self.screen.listen()
        self.screen.onkey(key="w", fun=self.go_forward)
        self.screen.onkey(key="s", fun=self.go_backward)
        self.screen.onkey(key="a", fun=self.go_counter_clockwise)
        self.screen.onkey(key="d", fun=self.go_clockwise)
        self.screen.exitonclick()

    def go_forward(self):
        self.turtle.forward(10)

    def go_backward(self):
        self.turtle.backward(10)

    def go_counter_clockwise(self):
        self.turtle.left(20)

    def go_clockwise(self):
        self.turtle.right(20)

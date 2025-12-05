from turtle import Turtle

class Ball(Turtle):
    def __init__(self):
        super().__init__()
        self.shape("circle")
        self.color("blue")
        self.penup()
        self.x_move = 10
        self.y_move = 10

    def move(self):
        new_y = self.ycor()
        new_y += self.y_move
        new_x = self.xcor()
        new_x += self.x_move
        self.goto(new_x, new_y)
    def bounce_y(self):
        self.y_move *= -1

    def bounce_x(self):
         self.x_move *= -1

    def reset_ball(self):
        self.goto(0, 0)

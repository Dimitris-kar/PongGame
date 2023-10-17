from turtle import Turtle


class Paddle(Turtle):

    def __init__(self, x_pos):
        super().__init__()
        self.shape("square")
        self.penup()
        self.color("silver")
        self.shapesize(stretch_wid=5, stretch_len=1)
        self.setpos(x_pos, y=0)

    def move_up(self):
        new_y = self.ycor() + 20
        self.goto(self.xcor(), y=new_y)

    def move_down(self):
        new_y = self.ycor() - 20
        self.goto(self.xcor(), y=new_y)

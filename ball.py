from turtle import Turtle

class Ball(Turtle):

    def __init__(self):
        super().__init__()
        self.shape("circle")
        self.color("white")
        self.penup()
        self.turtlesize(stretch_wid=1, stretch_len=1)
        self.goto(0, -360)
        self.x_move = 10
        self.y_move = 10
        self.move_speed = 0.05

    def move(self):
        new_x = self.xcor() + self.x_move
        new_y = self.ycor() + self.y_move
        self.goto(new_x,new_y)

    def bounce_y(self):
        self.y_move *= -1


    def bounce_x(self):
        self.x_move *= -1


    def increase_speed(self,speed_factor=1):
        self.move_speed *= speed_factor

    def reset_position(self,x=0):
        self.goto(x,-360)
        self.move_speed = 0.05
        self.bounce_y()

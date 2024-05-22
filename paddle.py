from turtle import Turtle
# PADDLE_POSITION = (0, 350)
# X_POS = 350
# Y_POS = 0
PADDLE_SIZE = [300, 20]
PADDLE_LIMITS = [-750,750]

class Paddle(Turtle):

    def __init__(self, position):
        super().__init__()
        self.y_pos = position[1]
        self.shape("square")
        self.color("DeepSkyBlue")
        self.penup()
        self.turtlesize(stretch_len=15,stretch_wid=1)
        self.goto(position)

    def move_right(self):
        if self.xcor() < PADDLE_LIMITS[1]:
            new_x = self.xcor()+150
            self.goto(new_x, self.y_pos)
        else:
            pass

    def move_left(self):
        if self.xcor() > PADDLE_LIMITS[0]:
            new_x = self.xcor()-150
            self.goto(new_x, self.y_pos)
        else:
            pass

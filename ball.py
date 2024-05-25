from turtle import Turtle

class Ball(Turtle):
    """A class representing a ball in a game."""

    def __init__(self):
        """Initialize the Ball object."""
        super().__init__()  # Initialize the Turtle superclass
        self.shape("circle")  # Set the shape of the ball to a circle
        self.color("white")  # Set the color of the ball to white
        self.penup()  # Lift the pen to avoid drawing lines
        self.turtlesize(stretch_wid=1, stretch_len=1)  # Set the size of the ball
        self.goto(0, -360)  # Initial position of the ball
        self.x_move = 10  # Initial horizontal movement speed
        self.y_move = 10  # Initial vertical movement speed
        self.move_speed = 0.05  # Initial movement speed

    def move(self):
        """Move the ball based on its current x_move and y_move speeds."""
        new_x = self.xcor() + self.x_move  # Calculate new x-coordinate
        new_y = self.ycor() + self.y_move  # Calculate new y-coordinate
        self.goto(new_x, new_y)  # Move the ball to the new coordinates

    def bounce_y(self):
        """Reverse the vertical movement direction of the ball."""
        self.y_move *= -1  # Multiply y_move by -1 to reverse direction

    def bounce_x(self):
        """Reverse the horizontal movement direction of the ball."""
        self.x_move *= -1  # Multiply x_move by -1 to reverse direction

    def increase_speed(self, speed_factor=1):
        """Increase the movement speed of the ball by a factor."""
        self.move_speed *= speed_factor  # Multiply move_speed by the factor

    def reset_position(self, x=0):
        """Reset the position of the ball and its movement speed."""
        self.goto(x, -345)  # Reset ball position to specified x-coordinate and y-coordinate
        self.move_speed = 0.05  # Reset movement speed
        self.bounce_y()  # Reverse vertical movement direction

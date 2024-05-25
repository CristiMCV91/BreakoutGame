from turtle import Turtle  # Import the Turtle class from the turtle module

# Constants defining the paddle properties and limits
PADDLE_SIZE = [300, 20]  # Size of the paddle [width, height]
PADDLE_LIMITS = [-750, 750]  # Movement limits for the paddle along the x-axis

class Paddle(Turtle):
    """
    Class representing a paddle in a game, derived from Turtle.

    Attributes:
        y_pos (int): The y-coordinate position of the paddle.
    """

    def __init__(self, position):
        """
        Initialize the Paddle object.

        Args:
            position (tuple): Starting position (x, y) of the paddle.
        """
        super().__init__()  # Initialize the Turtle superclass
        self.y_pos = position[1]  # Set the y-coordinate position of the paddle
        self.shape("square")  # Set the shape of the paddle to square
        self.color("DeepSkyBlue")  # Set the color of the paddle
        self.penup()  # Lift the pen to prevent drawing lines
        self.turtlesize(stretch_len=15, stretch_wid=1)  # Stretch the turtle shape
        self.goto(position)  # Move the paddle to the specified position

    def move_right(self):
        """Move the paddle to the right within defined limits."""
        if self.xcor() < PADDLE_LIMITS[1]:  # Check if paddle is within right limit
            new_x = self.xcor() + 150  # Calculate new x-coordinate for the paddle
            self.goto(new_x, self.y_pos)  # Move the paddle to the new position
        else:
            pass  # Do nothing if already at the right limit

    def move_left(self):
        """Move the paddle to the left within defined limits."""
        if self.xcor() > PADDLE_LIMITS[0]:  # Check if paddle is within left limit
            new_x = self.xcor() - 150  # Calculate new x-coordinate for the paddle
            self.goto(new_x, self.y_pos)  # Move the paddle to the new position
        else:
            pass  # Do nothing if already at the left limit

from turtle import Turtle


class Scoreboard(Turtle):
    """
    A class representing the scoreboard for the game.

    Attributes:
        life (str): Representation of remaining lives.
        score (int): Current score in the game.
        speed (int): Speed percentage of game elements.
        level (int): Current level of the game.
        end_game (bool): Flag indicating if the game has ended.
        sound (str): Representation of sound status.
    """

    def __init__(self):
        """
        Initializes the Scoreboard object with default values.
        """
        super().__init__()  # Initializes the Turtle superclass
        self.color("black")  # Sets the color of the scoreboard text
        self.penup()  # Lifts the pen to prevent drawing lines
        self.hideturtle()  # Hides the turtle icon
        self.life = "⭐⭐⭐"  # Represents initial lives as stars
        self.score = 0  # Initializes score to zero
        self.speed = 100  # Initializes speed percentage
        self.level = 1  # Initializes game level to 1
        self.end_game = False  # Flag to indicate if the game is ongoing
        self.sound_status()  # Updates sound status in the scoreboard
        self.speed_update()  # Updates speed percentage in the scoreboard
        self.update_scoreboard()  # Updates the entire scoreboard layout

    def update_scoreboard(self):
        """
        Updates all elements of the scoreboard display.
        """
        self.clear()  # Clears previous scoreboard text
        # Writes life indicator
        self.goto(-870, 405)
        self.write("Life:", align="left", font=("Courier", 24, "bold"))
        self.goto(-770, 407)
        self.write(self.life, align="left", font=("Courier", 20, "bold"))
        # Writes level and score
        self.goto(0, 405)
        self.write(f"Level: {self.level} | Score: {self.score}", align="center", font=("Courier", 24, "bold"))
        # Writes speed percentage
        self.goto(650, 405)
        self.write(f"Speed: {self.speed}%", align="left", font=("Courier", 24, "bold"))
        # Writes game control keys and sound status
        self.goto(-870, -440)
        self.write("[P] Pause | [M] Mute |", align="left", font=("Courier", 20, "bold"))
        self.goto(820, -446)
        self.write(self.sound, align="left", font=("Courier", 32, "bold"))

    def decrease_life(self):
        """
        Decreases the life indicator and updates the scoreboard.
        """
        self.life = self.life[:-1]  # Decrements life representation
        self.update_scoreboard()  # Updates scoreboard display
        if len(self.life) == 0:  # Checks if no lives left
            self.game_over()  # Initiates game over process

    def game_over(self):
        """
        Updates scoreboard to indicate game over and sets end_game flag.
        """
        self.life = "Game over!"  # Updates life indicator to indicate game over
        self.update_scoreboard()  # Updates scoreboard display
        self.end_game = True  # Sets end_game flag to True

    def reset_score(self):
        """
        Resets all scoreboard values to default and updates display.
        """
        self.life = "⭐⭐⭐"  # Resets life indicator
        self.score = 0  # Resets score to zero
        self.speed = 100  # Resets speed percentage
        self.level = 1  # Resets level to 1
        self.update_scoreboard()  # Updates scoreboard display
        self.end_game = False  # Resets end_game flag

    def speed_update(self, speed=0.05):
        """
        Updates the speed percentage based on a given speed factor.

        Args:
            speed (float): Speed factor to calculate the new speed percentage.
        """
        speed_percent = (0.05 / speed) * 100  # Calculates new speed percentage
        self.speed = int(speed_percent)  # Updates speed attribute
        self.update_scoreboard()  # Updates scoreboard display

    def score_update(self, points):
        """
        Updates the score by adding given points and updates the scoreboard.

        Args:
            points (int): Points to add to the current score.
        """
        self.score += points  # Adds points to the score
        self.update_scoreboard()  # Updates scoreboard display

    def level_up(self):
        """
        Increases the game level by one and updates the scoreboard.
        """
        self.level += 1  # Increments game level
        self.update_scoreboard()  # Updates scoreboard display

    def sound_status(self, sound=True):
        """
        Updates the sound status representation based on the given sound flag.

        Args:
            sound (bool): Flag indicating if sound is on (True) or off (False).
        """
        if sound:
            self.sound = "🔊"  # Updates sound representation to indicate sound on
        elif not sound:
            self.sound = "🔈"  # Updates sound representation to indicate sound off
        self.update_scoreboard()  # Updates scoreboard display


class InfoArea(Turtle):
    """
    A class representing the information area surrounding the game board.
    """

    def __init__(self):
        """
        Initializes the InfoArea object with graphical settings.
        """
        super().__init__()  # Initializes the Turtle superclass
        self.hideturtle()  # Hides the turtle icon
        self.speed("fastest")  # Sets the drawing speed to fastest

        # Draws the header area
        self.penup()
        self.goto(-1000, 400)
        self.pendown()
        self.color("azure3")
        self.begin_fill()
        for _ in range(2):
            self.forward(2000)
            self.left(90)
            self.forward(50)
            self.left(90)
        self.end_fill()

        # Draws the footer area
        self.penup()
        self.goto(-1000, -400)
        self.pendown()
        self.color("azure3")
        self.begin_fill()
        for _ in range(2):
            self.forward(2000)
            self.right(90)
            self.forward(50)
            self.right(90)
        self.end_fill()


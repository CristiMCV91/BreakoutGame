import random
from turtle import Turtle
import math

class BricksWall:
    """Class representing a wall of bricks in a game."""

    def __init__(self, level):
        """Initialize the BricksWall object based on the specified level."""
        self.create_wall_lvl(level)

    def create_wall_lvl(self, lvl=1):
        """Create the wall of bricks based on the specified level."""
        if lvl == 1:
            self.create_wall_lvl1()
        elif lvl == 2:
            self.create_wall_lvl2()
        elif lvl == 3:
            self.create_wall_lvl3()

    # Create wall for ---------------------------- level 1
    def create_wall_lvl1(self, start_position=[-836, 250], rows=4):
        """Create a specific layout for level 1 bricks."""
        self.bricks = []  # Initialize an empty list for bricks
        self.brick_size = [5, 2]  # Set the default size of the bricks

        columns = 16
        for r in range(0, rows):
            if r % 2 == 0:
                position = start_position[:]
                position[1] -= 50 * r
                for i in range(0, columns):
                    self.add_brick(position)
                    position[0] += 111
            elif r % 2 == 1:
                position = start_position[:]
                position[0] += 55
                position[1] -= 50 * r
                for i in range(0, columns - 1):
                    self.add_brick(position=position, size=self.brick_size)
                    position[0] += 111
        self.color_bricks_lvl1()  # Color the bricks for level 1

    # END ---------------------------------------- level 1

    # Create wall for ---------------------------- level 2
    def create_wall_lvl2(self, start_position=[0, 100], radius=200):
        """Create a specific layout for level 2 bricks."""
        self.bricks = []  # Initialize an empty list for bricks
        self.brick_size = [2.5, 2.5]  # Set the default size of the bricks

        points = 12
        angle = 0
        for i in range(0, points):
            x = int(radius * math.cos(math.radians(angle)))
            y = int(radius * math.sin(math.radians(angle)))
            position = [x + start_position[0], y + start_position[1]]
            self.add_brick(position=position, rotation=angle + 90, size=self.brick_size)
            angle += 360 / points

        start_position[0] = -570

        for i in range(0, points + 1):
            x = int(radius * math.cos(math.radians(angle)))
            y = int(radius * math.sin(math.radians(angle)))
            position = [x + start_position[0], y + start_position[1]]
            self.add_brick(position=position, rotation=angle + 90, size=self.brick_size)
            angle += 360 / points

        start_position[0] = +570

        for i in range(0, points + 1):
            x = int(radius * math.cos(math.radians(angle)))
            y = int(radius * math.sin(math.radians(angle)))
            position = [x + start_position[0], y + start_position[1]]
            self.add_brick(position=position, rotation=angle + 90, size=self.brick_size)
            angle += 360 / points

        self.color_random_bricks()  # Randomly color the bricks for level 2

    # END ---------------------------------------- level 2

    # Create wall for ---------------------------- level 3
    def create_wall_lvl3(self, start_position=[0, 100], radius=225):
        """Create a specific layout for level 3 bricks."""
        self.bricks = []  # Initialize an empty list for bricks

        self.brick_size = [3, 3]  # Set the default size of the bricks

        points = 12
        angle = 0
        for i in range(0, points):
            if i in [0, 3, 6, 9]:
                pass
            else:
                x = int(radius * math.cos(math.radians(angle)))
                y = int(radius * math.sin(math.radians(angle)))
                position = [x + start_position[0], y + start_position[1]]
                self.add_brick(position=position, rotation=angle + 60, size=self.brick_size, shape="triangle")
            angle += 360 / points

        start_position[0] = -485

        for i in range(0, points):
            if i in [5, 6, 7]:
                pass
            else:
                x = int(radius * math.cos(math.radians(angle)))
                y = int(radius * math.sin(math.radians(angle)))
                position = [x + start_position[0], y + start_position[1]]
                self.add_brick(position=position, rotation=angle + 60, size=self.brick_size, shape="triangle")

            angle += 360 / points

        start_position[0] = +485

        for i in range(0, points):
            if i in [0, 1, 11]:
                pass
            else:
                x = int(radius * math.cos(math.radians(angle)))
                y = int(radius * math.sin(math.radians(angle)))
                position = [x + start_position[0], y + start_position[1]]
                self.add_brick(position=position, rotation=angle + 60, size=self.brick_size, shape="triangle")

            angle += 360 / points

        self.color_random_bricks()  # Randomly color the bricks for level 3

    # END ---------------------------------------- level 3

    def add_brick(self, position=(0, 0), rotation=0, shape="square", size=[5, 2]):
        """Add a brick to the wall."""
        brick = Turtle(shape)
        brick.color("white")
        brick.penup()
        brick.turtlesize(stretch_len=size[0], stretch_wid=size[1])
        brick.goto(position)
        brick.setheading(rotation)
        self.bricks.append(brick)  # Append the newly created brick to the bricks list

    def color_bricks_lvl1(self):
        """Color the bricks for level 1 with specific colors."""
        for i in range(0, len(self.bricks)):
            if i in range(0, 16):
                self.bricks[i].color("DarkRed")
            elif i in range(16, 31):
                self.bricks[i].color("DarkOrange")
            elif i in range(31, 47):
                self.bricks[i].color("DarkGoldenrod1")
            elif i in range(47, 62):
                self.bricks[i].color("chartreuse4")

    def color_random_bricks(self):
        """Color the bricks randomly."""
        colors = [
            "red", "green", "blue", "yellow", "orange", "purple", "pink", "black",
            "white", "brown", "gray", "cyan", "magenta", "lime", "turquoise",
            "gold", "violet", "indigo", "coral", "salmon", "khaki", "lavender",
            "maroon", "navy", "olive", "teal", "orchid", "plum", "sienna", "tan"
        ]
        for i in range(0, len(self.bricks)):
            color_brick = random.choice(colors)
            self.bricks[i].color(color_brick)

    def reset(self, level=1):
        """Reset the wall of bricks to the specified level."""
        while len(self.bricks) > 0:
            for brick in self.bricks:
                brick.reset()  # Reset each brick
                self.bricks.remove(brick)  # Remove the brick from the list
        self.create_wall_lvl(level)  # Recreate the wall based on the specified level

    def remove_brick(self, brick):
        """Remove a specific brick from the wall."""
        index = self.bricks.index(brick)  # Get the index of the brick
        del self.bricks[index]  # Delete the brick from the list

    def get_brick_size(self, brick):
        """Get the size of a specific brick."""
        return brick._stretch_wid, brick._stretch_len  # Return the width and length of the brick

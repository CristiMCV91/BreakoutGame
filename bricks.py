from turtle import Turtle

STARTING_POSITION = [-836, 250]
SPACE= 10
WALL_ROWS = 4

class BricksWall:

    def __init__(self):
        self.bricks = []
        self.create_wall()
        self.color_bricks()

    def create_wall(self, start_position=STARTING_POSITION, rows=WALL_ROWS):
        colomns = 16
        for r in range(0, rows):
            if r%2 == 0:
                position = start_position[:]
                position[1] -= 50 * r
                for i in range(0, colomns):
                    self.add_brick(position)
                    position[0] += 111

            elif r%2 ==1:
                position = start_position[:]
                position[0] += 55
                position[1] -= 50 * r
                for i in range(0, colomns-1):
                    self.add_brick(position)
                    position[0] += 111


    def add_brick(self, position=(0,0)):
        brick = Turtle("square")
        brick.color("white")
        brick.penup()
        brick.turtlesize(stretch_len=5, stretch_wid=2)
        brick.goto(position)
        self.bricks.append(brick)

    def color_bricks(self):
        for i in range(0,len(self.bricks)):
            if i in range(0,16):
                self.bricks[i].color("DarkRed")
            elif i in range(16,31):
                self.bricks[i].color("DarkOrange")
            elif i in range(31,47):
                self.bricks[i].color("DarkGoldenrod1")
            elif i in range(47,62):
                self.bricks[i].color("chartreuse4")



    def reset(self):
        self.create_wall()

    def remove_brick(self, brick):
        index = self.bricks.index(brick)
        del self.bricks[index]

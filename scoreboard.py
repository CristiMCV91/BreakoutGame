from turtle import Turtle

class Scoreboard(Turtle):

    def __init__(self):
        super().__init__()
        self.color("black")
        self.penup()
        self.hideturtle()
        self.life = "⭐⭐⭐⭐⭐"
        self.score = 0
        self.speed = 100
        self.level = 1
        self.end_game = False
        self.speed_update()
        self.update_scoreboard()


    def update_scoreboard(self):
        self.clear()
        self.goto(-870, 405)
        self.write("Life:", align="left", font=("Courier", 24, "bold"))
        self.goto(-770, 407)
        self.write(self.life, align="left", font=("Courier", 20, "bold"))
        self.goto(0, 405)
        self.write(f"Level: {self.level} | Score: {self.score}", align="center", font=("Courier", 24, "bold"))
        self.goto(650, 405)
        self.write(f"Speed: {self.speed}%", align="left", font=("Courier", 24, "bold"))

    def decrease_life(self):
        self.life = self.life[:-1]
        self.update_scoreboard()
        if len(self.life) == 0:
            self.game_over()

    def game_over(self):
        self.life = "Game over!"
        self.update_scoreboard()
        self.end_game = True

    def reset_score(self):
        self.life = "⭐⭐⭐⭐⭐"
        self.update_scoreboard()
        self.end_game = False

    def speed_update(self, speed=0.05):
        speed_percent = (0.05/speed)*100
        self.speed = int(speed_percent)
        self.update_scoreboard()

    def score_update(self, points):
        self.score += points
        self.update_scoreboard()

    def level_up(self):
        self.level +=1
        self.update_scoreboard()

class InfoArea(Turtle):
    def __init__(self):
        super().__init__()
        self.hideturtle()
        self.speed("fastest")

        # Header
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

        # Footer
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





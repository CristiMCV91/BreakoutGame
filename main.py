# Import necessary modules
from turtle import Screen
from sound import SoundManager
from paddle import Paddle
from ball import Ball
from scoreboard import Scoreboard, InfoArea
from bricks import BricksWall
import time

# Set up the screen
screen = Screen()
screen.bgcolor("black")
screen.setup(width=1800, height=900)
screen.title("Breakout Game")
screen.tracer(0)  # Turn off automatic screen updates

# Initialize game objects
player = Paddle((0, -370))
ball = Ball()
info_area = InfoArea()
scoreboard = Scoreboard()
wall = BricksWall(scoreboard.level)  # Initialize wall of bricks
sound = SoundManager()
speed = 0.1  # Initial speed of the ball

screen.listen()  # Start listening for keyboard events

# Function to toggle game pause state
def game_pause():
    global game_is_paused
    game_is_paused = not game_is_paused

# Function to toggle sound on/off
def sound_change():
    global sound_is_on
    sound_is_on = not sound_is_on
    scoreboard.sound_status(sound_is_on)

# Set up key bindings for player movement, pause, and sound toggle
screen.onkeypress(fun=player.move_left, key="Left")
screen.onkeypress(fun=player.move_right, key="Right")
screen.onkeypress(fun=game_pause, key="p")
screen.onkeypress(fun=sound_change, key="m")

# Initialize game state variables
game_is_on = True
game_is_paused = False
sound_is_on = True

# Main game loop
while game_is_on:
    if game_is_paused:
        screen.update()  # Update the screen to show changes
        time.sleep(0.1)  # Pause for a short time
        continue  # Skip the rest of the loop and restart

    screen.update()  # Update the screen to show changes
    time.sleep(ball.move_speed)  # Pause between each frame update

    # Move the ball and update player color
    ball.move()
    player.color("DeepSkyBlue")

    # Detect collision with bricks
    for brick in wall.bricks:
        if (ball.xcor() in range(brick.xcor() - 50, brick.xcor() + 50)) and (ball.ycor() in range(brick.ycor() - 50, brick.ycor() + 50)):
            if sound_is_on:
                sound.play_sound(sound.block_hit)
            wall.remove_brick(brick)
            brick.reset()
            ball.bounce_y()
            scoreboard.score_update(10)
            print(wall.brick_size)  # Debugging statement

    # Level up when all bricks are destroyed
    if len(wall.bricks) == 0:
        scoreboard.level_up()
        if scoreboard.level > 3:
            scoreboard.level = 1  # Reset level after reaching max
        if sound_is_on:
            sound.play_sound(sound.level_complete)
        wall.reset(level=scoreboard.level)  # Reset bricks for the next level
        ball.reset_position(player.xcor())  # Reset ball position

    # Detect collision with top wall
    if ball.ycor() > 388:
        if sound_is_on:
            sound.play_sound(sound.wall_hit)
        ball.bounce_y()

    # Detect collision with side walls
    if ball.xcor() < -888 or ball.xcor() > 888:
        if sound_is_on:
            sound.play_sound(sound.wall_hit)
        ball.bounce_x()

    # Detect collision with paddles
    if (ball.xcor() in range(player.xcor() - 150, player.xcor() + 150)) and (ball.ycor() < -350):
        player.color("DarkBlue")
        if sound_is_on:
            sound.play_sound(sound.ball_tap)
        ball.bounce_y()
        ball.increase_speed(speed_factor=0.95)
        scoreboard.speed_update(speed=ball.move_speed)

    # Check if the ball misses the paddle
    if ball.ycor() < -380:
        scoreboard.decrease_life()
        if sound_is_on:
            sound.play_sound(sound.dead)
        ball.reset_position(player.xcor())
        scoreboard.speed_update(speed=ball.move_speed)

    # Check if the game is over
    if scoreboard.end_game:
        player.color("DarkBlue")
        print("Game over")
        ball.reset_position(player.xcor())
        if sound_is_on:
            sound.play_sound(sound.game_over)
        time.sleep(4)  # Pause before resetting the game
        scoreboard.reset_score()
        scoreboard.speed_update(speed=ball.move_speed)
        wall.reset()

# Exit the game when the player clicks on the screen
screen.exitonclick()

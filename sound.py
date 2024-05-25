from pygame import init, mixer, quit

class SoundManager:
    """
    A class to manage game sounds using Pygame library.

    Attributes:
        block_hit (pygame.mixer.Sound): Sound for block hit.
        ball_tap (pygame.mixer.Sound): Sound for ball tap.
        wall_hit (pygame.mixer.Sound): Sound for wall hit.
        dead (pygame.mixer.Sound): Sound for game over due to losing all lives.
        level_complete (pygame.mixer.Sound): Sound for completing a game level.
        game_over (pygame.mixer.Sound): Sound for game over.

    Methods:
        __init__(): Initializes Pygame and loads all sound files.
        load_sound(file_path): Loads a sound file from the specified file path.
        play_sound(sound): Plays the provided sound.
        stop(): Quits the Pygame mixer and the Pygame itself.
    """

    def __init__(self):
        """
        Initializes the SoundManager with Pygame and loads all necessary sound files.
        """
        init()  # Initializes Pygame modules
        mixer.init()  # Initializes Pygame mixer for sound playback

        # Load all sound files into respective attributes
        self.block_hit = self.load_sound("sounds/electronic-retro-block-hit-2185.wav")
        self.ball_tap = self.load_sound("sounds/game-ball-tap-2073.wav")
        self.wall_hit = self.load_sound("sounds/ball-bouncing-in-the-ground-2077.wav")
        self.dead = self.load_sound("sounds/dead-notification-272.wav")
        self.level_complete = self.load_sound("sounds/completion-of-a-level-2063.wav")
        self.game_over = self.load_sound("sounds/game-over-trombone-471.wav")

    def load_sound(self, file_path):
        """
        Loads a sound file from the specified file path using Pygame.mixer.

        Args:
            file_path (str): Path to the sound file.

        Returns:
            pygame.mixer.Sound: Loaded sound object.
        """
        return mixer.Sound(file_path)

    def play_sound(self, sound):
        """
        Plays the provided sound using Pygame.mixer.

        Args:
            sound (pygame.mixer.Sound): Sound object to be played.
        """
        sound.play()

    def stop(self):
        """
        Stops the Pygame mixer and quits Pygame itself.
        """
        mixer.quit()  # Stops Pygame mixer
        quit()  # Quits Pygame

class Settings():
    """Klasa przechowuje ustawienia gry"""

    def __init__(self, game):

        self.game = game
        # ustawienia ekranu
        self.line_y = 50

        self.caption = "Snake by W30Rotkiw06"
        self.screen_size_width = 544
        self.screen_size_height =  self.screen_size_width + self.line_y
        self.screen_size = (self.screen_size_width, self.screen_size_height)
        self.bg_color = (146, 227, 239)

        self.game_mode = "medium"
        

        # ustawienia węża
        self.set_deafult()
        self.snake_color = (0, 0, 0)
        self.apple_color = (0, 0, 0)

    def set_deafult(self):
        if self.game_mode == "easy":
            self.snake_speed = 0.15
            self.acceleration = 1.01
            print("E")
        elif self.game_mode == "medium":
            self.snake_speed = 0.13
            self.acceleration = 1.05
            print("M")
        else:
            self.snake_speed = 0.11
            self.acceleration = 1.1
        self.choosen = True
    
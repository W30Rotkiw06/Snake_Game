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
        

        self.set_deafult_settings()

    def set_deafult_settings(self):
        # ustawienia węża
        self.snake_speed = 0.4
        self.snake_color = (0, 0, 0)
        self.apple_color = (0, 0, 0)
        

class Settings():
    """Klasa przechowuje ustawienia gry"""

    def __init__(self):
        # ustawienia ekranu
        self.caption = "Snake by W30Rotkiw06"
        self.screen_size_width = 500
        self.screen_size_height = 550
        self.screen_size = (self.screen_size_width, self.screen_size_height)
        self.bg_color = (146, 227, 239)
        

        # ustawienia węża
        self.snake_speed = 0.3
        self.snake_color = (0, 0, 0)
        self.apple_color = (0, 0, 0)

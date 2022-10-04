import os
from time import sleep

class Settings():
    """Klasa przechowuje ustawienia gry"""

    def __init__(self, game):


        self.game = game
        # ustawienia ekranu
        self.line_y = 50
        os.system('cls')
        self.caption_extra = ""
        self.caption = f"Snake by W30Rotkiw06{self.caption_extra}"
        self.screen_size_width = 544
        self.screen_size_height =  self.screen_size_width + self.line_y
        self.screen_size = (self.screen_size_width, self.screen_size_height)
        self.bg_color = (146, 227, 239)

        self.game_mode = "MEDIUM"

        self.game.player = input("Podaj nazwę gracza: ").upper()
        print(f"Witaj, {self.game.player}!\nKliknij w okno, które właśnie się pojawiło i wybierz poziom trudności\nPOWODZENIA")
        sleep(0.1)
        

        # ustawienia węża
        self.set_deafult()
        self.snake_color = (0, 0, 0)
        self.apple_color = (0, 0, 0)

        # ustawienia przycisków
        self.button_x = 500
        self.text_color = (250, 250, 250)
        self.button_size = (100, 25)
        self.button_color = (0, 255, 0)
        self.button_color_clicked = (0, 200, 0)

    def set_deafult(self):
        self.caption_extra = f" | PLAYER: {self.game.player} | MODE: {self.game_mode}"
        self.caption = f"Snake by W30Rotkiw06{self.caption_extra}"
        if self.game_mode == "EASY":
            self.snake_speed = 0.15
            self.acceleration = 1.01
        elif self.game_mode == "MEDIUM":
            self.snake_speed = 0.13
            self.acceleration = 1.05
        else:
            self.snake_speed = 0.11
            self.acceleration = 1.1
        self.choosen = True
    
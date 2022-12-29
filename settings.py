import os
from time import sleep

class Settings():
    """Klasa przechowuje ustawienia gry"""

    def __init__(self, game):
        """Inicjalizacja ustawień gry"""

        self.game = game
        # ustawienia ekranu
        self.line_y = 50
        self.caption_extra = ""
        self.caption = f"Snake by W30Rotkiw06"
        self.screen_size_width = 544
        self.screen_size_height =  self.screen_size_width + self.line_y
        self.screen_size = (self.screen_size_width, self.screen_size_height)
        self.set_deafult_color_lib()

        self.game_mode = "MEDIUM"

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

        # ustawienia okna do wpisywania
        self.window_color = (200, 200, 200)


    def set_deafult(self):
        """Przywraca domyślne parametry prędkości i przyspieszenia dla wybranego poziomu trudności"""
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
        if self.game.player == " ": self.game.player = "Player" 
        self.is_wednesday()


    def is_wednesday(self):
        """mały easter egg na temat serialu Wednesday"""
        
        if self.game.player.title() == "Wednesday" or self.game.player.title() == "Sroda":
            
            self.game.player = "Wednesday"
            self.caption = "Hello, Wednesday Addams :-)"
            self.color_libary = [(0, 0, 0)]
            self.bg_color = (250, 250, 250)
            self.snake_color = self.apple_color = (0, 0, 0)

        else: self.set_deafult_color_lib()

    
    def set_deafult_color_lib(self):
        self.color_libary = [(193, 206, 120), (151, 82, 189), (245, 128, 187), (231, 161, 76), (125, 63, 73), (190, 171, 223), 
        (105, 145, 108), (111, 165, 178), (62, 137, 152), (120, 74, 198), (182, 128, 211), (137, 125, 154), (111, 218, 134), 
        (152, 117, 196), (232, 77, 125), (109, 96, 191), (163, 131, 248), (217, 117, 159), (218, 104, 122), (181, 75, 98),
        (70, 86, 100), (171, 168, 217), (113, 182, 55), (204, 200, 196), (150, 56, 142), (148, 131, 212), (196, 105, 119), 
        (149, 66, 79), (208, 173, 149), (164, 114, 242), (235, 174, 60), (78, 127, 219), (169, 117, 214), (128, 211, 186), 
        (91, 218, 71), (149, 99, 123), (234, 105, 211), (113, 215, 243), (133, 100, 128), (103, 202, 84), (157, 91, 183), 
        (105, 93, 190), (113, 145, 192), (232, 123, 127), (219, 58, 225), (63, 198, 104), (136, 65, 226), (132, 54, 138), 
        (127, 52, 131), (79, 162, 166), (222, 213, 55), (126, 125, 221), (113, 71, 154), (94, 132, 129), (147, 193, 213), 
        (218, 67, 87), (184, 80, 112), (67, 152, 164), (66, 227, 128), (124, 204, 238), (215, 59, 142), (206, 157, 158), 
        (204, 75, 197), (171, 68, 165), (144, 196, 217), (54, 64, 197), (223, 88, 201), (195, 135, 58), (108, 194, 226), 
        (54, 223, 95), (107, 69, 233), (58, 248, 105), (124, 201, 174), (117, 196, 200), (209, 106, 208), (96, 91, 195), 
        (95, 149, 178), (222, 76, 63), (66, 67, 245), (108, 183, 126), (59, 110, 118), (68, 155, 149), (84, 143, 62), 
        (225, 60, 241), (87, 161, 104), (96, 114, 160), (137, 70, 118), (169, 81, 57), (96, 51, 174), (52, 78, 164),  
        (180, 77, 217), (75, 229, 125), (51, 169, 198), (143, 120, 149), (203, 51, 145), (200, 51, 154)]

        self.bg_color = (146, 227, 239)
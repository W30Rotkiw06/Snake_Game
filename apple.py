from secrets import choice
import pygame
from random import randint

class Apple():
    """Klasa przeznaczona do zarządzania owocem (jabłkiem)"""

    def __init__(self, game):
        """Inicjalizacja jabłka"""
        self.settings = game.settings
        self.screen = game.screen
        self.game = game

        self.color_libary = [(193, 206, 120), (151, 82, 189), (245, 128, 187), (231, 161, 76), (125, 63, 73), (190, 171, 223), (105, 145, 108), (111, 165, 178), (62, 137, 152), (120, 74, 198), (182, 128, 211), (137, 125, 154), (111, 218, 134), (91, 218, 71), (149, 99, 123), (234, 105, 211), (113, 215, 243), (133, 100, 128), (103, 202, 84), (157, 91, 183), (105, 93, 190), (113, 145, 192), (232, 123, 127), (219, 58, 225), (63, 198, 104), (136, 65, 226), (132, 54, 138), (127, 52, 131), (79, 162, 166), (222, 213, 55), (126, 125, 221), (113, 71, 154), (94, 132, 129), (147, 193, 213), (70, 86, 100), (171, 168, 217), (113, 182, 55), (204, 200, 196), (150, 56, 142), (148, 131, 212), (196, 105, 119), (149, 66, 79), (208, 173, 149), (164, 114, 242), (235, 174, 60), (78, 127, 219), (169, 117, 214), (128, 211, 186), (95, 149, 178), (222, 76, 63), (66, 67, 245), (108, 183, 126), (59, 110, 118), (68, 155, 149), (84, 143, 62), (225, 60, 241), (87, 161, 104), (96, 114, 160), (137, 70, 118), (169, 81, 57), (96, 51, 174), (52, 78, 164), (218, 67, 87), (184, 80, 112), (67, 152, 164), (66, 227, 128), (124, 204, 238), (215, 59, 142), (206, 157, 158), (204, 75, 197), (171, 68, 165), (144, 196, 217), (54, 64, 197), (223, 88, 201), (195, 135, 58), (108, 194, 226), (54, 223, 95), (107, 69, 233), (58, 248, 105), (124, 201, 174), (117, 196, 200), (209, 106, 208), (96, 91, 195), (152, 117, 196), (232, 77, 125), (109, 96, 191), (163, 131, 248), (217, 117, 159), (218, 104, 122), (181, 75, 98), (180, 77, 217), (75, 229, 125), (51, 169, 198), (143, 120, 149), (203, 51, 145), (200, 51, 154)]

        self.rect = pygame.Rect(0, 0, 8, 8)

        self.new_apple()

    def new_apple(self):
        """Metoda przeznaczona do generowania nowego jabłka na ekranie"""
        self.rect.x = randint(40, self.settings.screen_size_width - 40)
        self.rect.y = randint(40 + self.settings.line_y, self.settings.screen_size_height - 40)
        self.settings.snake_speed /= self.settings.acceleration
        self.settings.apple_color = choice(self.color_libary)

    def blitme(self):
        """wyświetlanie jabłka w jego bierzącym położeniu"""
        if self.game.game_active:
            pygame.draw.rect(self.screen, self.settings.apple_color, self.rect)
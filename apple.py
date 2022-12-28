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

        
       
       
        self.rect = pygame.Rect(0, 0, 8, 8)

        self.new_apple()

    def new_apple(self):
        """Metoda przeznaczona do generowania nowego jabłka na ekranie"""
        self.rect.x = randint(40, self.settings.screen_size_width - 40) //8 *8 +3
        self.rect.y = randint(40 + self.settings.line_y, self.settings.screen_size_height - 40) //8 *8 + 3
        self.settings.snake_speed /= self.settings.acceleration
        self.settings.apple_color = choice(self.game.settings.color_libary)

    def blitme(self):
        """wyświetlanie jabłka w jego bierzącym położeniu"""
        if self.game.game_active:
            pygame.draw.rect(self.screen, self.settings.apple_color, self.rect)
import pygame
import time

class MyLittleSnake():
    """Klasa przeznaczona do zarządzania jednym członem węża"""

    def __init__(self, sn_game, x, y):
        """inicjalizacja węża i zarządzanie jego początkowym położeniem"""
        self.screen = sn_game.screen

        self.x = x
        self.y = y

        # wczytanie prostokąta
        self.rect = pygame.Rect(0, 0, 8, 8)
    


class MySnake(MyLittleSnake):
    """Klasa przeznaczona do zarządzania całym wężem"""

    def __init__(self, snake_game):
        self.game = snake_game
        self.my_long_snake = []
        self.settings = snake_game.settings
        self.screen = snake_game.screen
        self.snake_game = snake_game

        self.x = self.settings.screen_size_width //2
        self.y = self.settings.screen_size_height //2

        
        self.my_little_snake = super().__init__(self.snake_game, self.x, self.y)
        self.my_long_snake.insert(0, self.my_little_snake)


        self.coords = []
        self.head_coord = (self.x, self.y)

        # opcje wskazujące na poruszanie się statku
        self.moving_right = True
        self.moving_left = False
        self.moving_up = False
        self.moving_down = False
        self.apple = False
    
        

    def update(self):
        """Poruszanie się węża, jego rozrost"""
        if self.moving_right: self.x += 8 
        elif self.moving_left: self.x -= 8
        elif self.moving_down: self.y += 8
        elif self.moving_up: self.y -= 8

        
        self.head_coord = (self.x, self.y)
        self.coords.insert(0, self.head_coord)


        self.my_little_snake = MyLittleSnake(self.snake_game, self.x, self.y)
        self.my_long_snake.insert(0, self.my_little_snake)

        if self.apple == True:
            pass
        else:
            del self.my_long_snake[-1]
            if self.coords: del self.coords[-1]


        self.my_little_snake.rect.centerx = self.my_little_snake.x
        self.my_little_snake.rect.centery = self.my_little_snake.y
        

        self.apple = False
        time.sleep(self.settings.snake_speed)   

    def blitme(self):
        if self.game.game_active == True:
            for self.item in self.my_long_snake:
                pygame.draw.rect(self.item.screen, self.settings.snake_color, self.item.rect) 
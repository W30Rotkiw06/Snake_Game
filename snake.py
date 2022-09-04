import sys
import pygame

from settings import Settings
from my_long_snake import MySnake
from apple import Apple
from points import Points

class Snake():
    """Ogólna klasa przeznaczona do zarządzania elementami gry"""

    def __init__(self):
        """Inicjalizaja gry i utworzenie jej zasobów"""
        pygame.init()
        self.settings = Settings()

        pygame.display.set_caption(self.settings.caption)
        self.screen = pygame.display.set_mode(self.settings.screen_size)

        self.my_long_snake = MySnake(self)
        self.apple = Apple(self)
        self.game_active = True

        self.points = Points(self)

    def run_game(self):
        """rozpoczęcie pętli głównej gry"""
        while True:
            self.check_events()

            if self.game_active:
                self.my_long_snake.update()         
                self.collisions()
                self.is_dead()
                self.update_screen()
                
            self.update_screen()

    def collisions(self):
        collision = self.apple.rect.collidepoint(self.my_long_snake.x, self.my_long_snake.y)
        if collision:
            self.my_long_snake.apple = True
            self.settings.snake_color = self.settings.apple_color
            self.apple.new_apple()
            self.points.new_point()
    
    def check_events(self):
        """reakcja na zdarzenie generowane przez myszkę lub klawiaturę"""
        for event in pygame.event.get():
            if event.type == pygame.QUIT: sys.exit()
            elif event.type == pygame.KEYDOWN:
                if event.key == pygame.K_RIGHT and self.my_long_snake.moving_left == False:
                    self.my_long_snake.moving_left = False
                    self.my_long_snake.moving_right = True
                    self.my_long_snake.moving_up = False
                    self.my_long_snake.moving_down = False
                elif event.key == pygame.K_LEFT and self.my_long_snake.moving_right == False:
                    self.my_long_snake.moving_left = True
                    self.my_long_snake.moving_right = False
                    self.my_long_snake.moving_up = False
                    self.my_long_snake.moving_down = False
                elif event.key == pygame.K_UP and self.my_long_snake.moving_down == False:
                    self.my_long_snake.moving_left = False
                    self.my_long_snake.moving_right = False
                    self.my_long_snake.moving_up = True
                    self.my_long_snake.moving_down = False
                elif event.key == pygame.K_DOWN and self.my_long_snake.moving_up == False:
                    self.my_long_snake.moving_left = False
                    self.my_long_snake.moving_right = False
                    self.my_long_snake.moving_up = False
                    self.my_long_snake.moving_down = True
                elif event.key == pygame.K_q: sys.exit()


    def is_dead(self):
        """sprawdzanie czy wąż powinien być martwy, tzn czy nie wiechał w ścianę"""
        if self.my_long_snake.x <= 8 or self.my_long_snake.x >= self.settings.screen_size_width - 8: self.kill_yourself()
        elif self.my_long_snake.y <= self.settings.line_y + 8 or self.my_long_snake.y >= self.settings.screen_size_height - 6: self.kill_yourself()

    def kill_yourself(self):
        self.points.points = 0
        
        self.points.print_score = False

        del self.my_long_snake
        del self.apple
        self.game_active = False
    
    def update_screen(self):
        """uaktualnianie obrazów na ekranie i przejście do nowego ekranu"""
        self.screen.fill(self.settings.bg_color)
        try:
            self.apple.blitme()
            self.my_long_snake.blitme()
        except: pass
        self.points.show_score()

        pygame.display.flip() # wyświetlenie ostatnio zmodyfikowanego ekranu
    


if __name__ == "__main__":
    """utworzenie egzemplarza gry i jej uruchomienie"""
    snake = Snake()
    snake.run_game()
import sys
from time import sleep
import pygame

from settings import Settings
from my_long_snake import MySnake
from apple import Apple
from points import Points
from start import StartMenu

class Snake():
    """Ogólna klasa przeznaczona do zarządzania elementami gry"""

    def __init__(self):
        """Inicjalizaja gry i utworzenie jej zasobów"""
        pygame.init()
        self.settings = Settings(self)

        pygame.display.set_caption(self.settings.caption)
        self.screen = pygame.display.set_mode(self.settings.screen_size)

        self.my_long_snake = MySnake(self)
        self.apple = Apple(self)
        self.game_active = False

        self.points = Points(self)

        self.button_easy = StartMenu(self, "EASY", 0)
        self.button_medium = StartMenu(self, "MEDIUM", 1)
        self.button_hard = StartMenu(self, "HARD", 2)

    def run_game(self):
        """rozpoczęcie pętli głównej gry"""
        while True:
            self.check_events()

            if self.game_active:
                self.my_long_snake.update()         
                self.collisions()
                self.is_dead()
                
                
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
            elif event.type == pygame.KEYDOWN and self.game_active == True:
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
            elif event.type == pygame.MOUSEBUTTONDOWN:
                self.check_play_buttons(pygame.mouse.get_pos())



    def check_play_buttons(self, mouse_pos):
        """Sprawdza czy guzik został kliknięty"""
        if self.button_easy.rect.collidepoint(mouse_pos) and not self.game_active: self.settings.game_mode, self.settings.choosen = "easy", True
        elif self.button_medium.rect.collidepoint(mouse_pos) and not self.game_active: self.settings.game_mode, self.settings.choosen = "medium", True
        elif self.button_hard.rect.collidepoint(mouse_pos) and not self.game_active: self.settings.game_mode, self.settings.choosen = "hard", True
        
        self.game_active, self.settings.choosen = True, False
        self.settings.set_deafult()
        self.my_long_snake = MySnake(self)
        self.points = Points(self)
        

    def is_dead(self):
        """sprawdzanie czy wąż powinien być martwy, tzn czy nie wiechał w ścianę"""
        if self.game_active:
            if self.my_long_snake.x <= 0 or self.my_long_snake.x >= self.settings.screen_size_width: self.kill_yourself()
            elif self.my_long_snake.y <= self.settings.line_y or self.my_long_snake.y >= self.settings.screen_size_height- 8: self.kill_yourself()
            elif self.my_long_snake.head_coord in self.my_long_snake.coords[1:]: self.kill_yourself()

                        

    def kill_yourself(self,):
        """Procedura uśmiercania węża"""
        self.my_long_snake.moving_down, self.my_long_snake.moving_up, self.my_long_snake.moving_left, self.my_long_snake.moving_right = False, False, False, False
        sleep(1)
        self.game_active = False
        self.points.update_scoretable()
    

    def update_screen(self):
        """uaktualnianie obrazów na ekranie i przejście do nowego ekranu"""
        self.screen.fill(self.settings.bg_color)
        self.apple.blitme()
        if not self.game_active:
            self.button_easy.draw_button()
            self.button_medium.draw_button()
            self.button_hard.draw_button()
        else: self.points.show_score()
        self.my_long_snake.blitme()

        pygame.display.flip() # wyświetlenie ostatnio zmodyfikowanego ekranu
    


if __name__ == "__main__":
    """utworzenie egzemplarza gry i jej uruchomienie"""
    snake = Snake()
    snake.run_game()
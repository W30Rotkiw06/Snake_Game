import sys
from time import sleep
import pygame

from settings import Settings
from my_long_snake import MySnake
from apple import Apple
from points import Points
from button import Button
from text_input import InputText

class Snake():
    """Ogólna klasa przeznaczona do zarządzania elementami gry"""

    def __init__(self):
        """Inicjalizaja gry i utworzenie jej zasobów"""
        pygame.init()
        
        self.player = ""
        self.settings = Settings(self)

        pygame.display.set_caption(self.settings.caption)
        self.screen = pygame.display.set_mode(self.settings.screen_size)
        pygame.display.set_icon(pygame.image.load("icon.ico"))

        self.my_long_snake = MySnake(self)
        self.apple = Apple(self)
        self.enter_your_name = InputText(self, (0, 0), (300, 50))
        self.game_active = False

        self.points = Points(self)

        self.button_easy = Button(self, "EASY", -120, self.settings.line_y, self.settings.button_size, self.settings.button_color)
        self.button_medium = Button(self, "MEDIUM", 0, self.settings.line_y, self.settings.button_size, self.settings.button_color)
        self.button_hard = Button(self, "HARD", 120, self.settings.line_y, self.settings.button_size, self.settings.button_color)
        self.button_start = Button(self, "START", 0, self.settings.line_y + 50, ((self.settings.button_size[0] * 2, self.settings.button_size[1] * 2,)), (20, 38, 190))

        self.button_easy.button_clicked, self.button_medium.button_clicked, self.button_hard.button_clicked, = False, True, False



    def run_game(self):
        """rozpoczęcie pętli głównej gry"""
        while True:
            self.check_events()

            if self.game_active:
                self.collisions()
                self.my_long_snake.update()
                self.is_dead()
                
                
            self.update_screen()



    def collisions(self):
        """Sprawdza, czy wąż 'zjadł' jabłko """
        collision = False
        if self.apple.rect.x - 4 <= self.my_long_snake.head_coord[0] and self.apple.rect.x + 12 >= self.my_long_snake.head_coord[0]:
            if  self.apple.rect.y - 4 <= self.my_long_snake.head_coord[1] and self.apple.rect.y + 12 >= self.my_long_snake.head_coord[1]: collision = True
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
            elif event.type == pygame.KEYDOWN:
                
                
                if event.key == pygame.K_q: self.player += "Q"
                elif event.key == pygame.K_w and len(self.player) < 10: self.player += "W"
                elif event.key == pygame.K_e and len(self.player) < 10: self.player += "E"
                elif event.key == pygame.K_r and len(self.player) < 10: self.player += "R"
                elif event.key == pygame.K_t and len(self.player) < 10: self.player += "T"
                elif event.key == pygame.K_y and len(self.player) < 10: self.player += "Y"
                elif event.key == pygame.K_u and len(self.player) < 10: self.player += "U"
                elif event.key == pygame.K_i and len(self.player) < 10: self.player += "I"
                elif event.key == pygame.K_o and len(self.player) < 10: self.player += "O"
                elif event.key == pygame.K_p and len(self.player) < 10: self.player += "P"

                elif event.key == pygame.K_a and len(self.player) < 10: self.player += "A"
                elif event.key == pygame.K_s and len(self.player) < 10: self.player += "S"
                elif event.key == pygame.K_d and len(self.player) < 10: self.player += "D"
                elif event.key == pygame.K_f and len(self.player) < 10: self.player += "F"
                elif event.key == pygame.K_g and len(self.player) < 10: self.player += "G"
                elif event.key == pygame.K_h and len(self.player) < 10: self.player += "H"
                elif event.key == pygame.K_j and len(self.player) < 10: self.player += "J"
                elif event.key == pygame.K_k and len(self.player) < 10: self.player += "K"
                elif event.key == pygame.K_l and len(self.player) < 10: self.player += "L"

                elif event.key == pygame.K_z and len(self.player) < 10: self.player += "Z"
                elif event.key == pygame.K_x and len(self.player) < 10: self.player += "X"
                elif event.key == pygame.K_c and len(self.player) < 10: self.player += "C"
                elif event.key == pygame.K_v and len(self.player) < 10: self.player += "V"
                elif event.key == pygame.K_b and len(self.player) < 10: self.player += "B"
                elif event.key == pygame.K_n and len(self.player) < 10: self.player += "N"
                elif event.key == pygame.K_m and len(self.player) < 10: self.player += "M"

                elif event.key == pygame.K_BACKSPACE and len(self.player) > 0 or  len(self.player) > 10:
                    self.player_list = list(self.player)
                    self.player_list.pop(-1)
                    self.player = ""
                    for char in self.player_list:
                        self.player += char



    def check_play_buttons(self, mouse_pos):
        """Sprawdza czy oraz który guzik został kliknięty"""
        if self.button_easy.rect.collidepoint(mouse_pos) and not self.game_active:
            self.settings.game_mode = "EASY"
            self.settings.caption_extra = f" | PLAYER: {self.player} | MODE: {self.settings.game_mode}"
            self.settings.caption = f"Snake by W30Rotkiw06{self.settings.caption_extra}"
            self.button_easy.button_clicked, self.button_medium.button_clicked, self.button_hard.button_clicked, = True, False, False
            self.points = Points(self)

        elif self.button_medium.rect.collidepoint(mouse_pos) and not self.game_active:
            self.settings.game_mode = "MEDIUM"
            self.settings.caption_extra = f" | PLAYER: {self.player} | MODE: {self.settings.game_mode}"
            self.settings.caption = f"Snake by W30Rotkiw06{self.settings.caption_extra}"
            self.button_easy.button_clicked, self.button_medium.button_clicked, self.button_hard.button_clicked, = False, True, False
            self.points = Points(self)

        elif self.button_hard.rect.collidepoint(mouse_pos) and not self.game_active:
            self.settings.game_mode = "HARD"
            self.settings.caption_extra = f" | PLAYER: {self.player} | MODE: {self.settings.game_mode}"
            self.settings.caption = f"Snake by W30Rotkiw06{self.settings.caption_extra}"
            self.button_easy.button_clicked, self.button_medium.button_clicked, self.button_hard.button_clicked, = False, False, True
            self.points = Points(self)

        elif self.button_start.rect.collidepoint(mouse_pos) and not self.game_active:
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
        self.button_start.msg = "TRY AGAIN"
        self.points.update_scoretable()
    

    def update_screen(self):
        """uaktualnianie obrazów na ekranie i przejście do nowego ekranu"""
        pygame.display.set_caption(self.settings.caption)
        self.screen.fill(self.settings.bg_color)
        self.apple.blitme()


        if not self.game_active:
            self.enter_your_name.draw_window()
            self.button_easy.draw_button()
            self.button_medium.draw_button()
            self.button_hard.draw_button()
            self.button_start.draw_button()
            self.points.show_table()
        else: 
            self.points.show_score()
        self.my_long_snake.blitme()

        pygame.display.flip() # wyświetlenie ostatnio zmodyfikowanego ekranu
    


if __name__ == "__main__":
    """utworzenie egzemplarza gry i jej uruchomienie"""
    snake = Snake()
    snake.run_game()
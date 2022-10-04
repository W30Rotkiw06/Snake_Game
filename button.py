import pygame.font
import pygame
class Button():
    
    def __init__(self, game, msg, x, y, size, color):
        """Inicjalizacja przycisku i menu początkowego"""
        self.screen = game.screen
        self.game = game
        self.screen_rect = self.screen.get_rect()
        self.msg = msg
        self.settings = self.game.settings
        self.button_clicked = False

        # właściwości przycisku
        self.width, self.height = size[0], size[1]
        self.deafult_color = color
        self.button_color = color
        self.text_color = self.game.settings.text_color
        self.font = pygame.font.SysFont(None, 24)

        # utworzenie prostokątnego przycisku w wyznaczonym miejscu

        self.rect = pygame.Rect(0, 0, self.width, self.height)
        self.rect.center = self.screen_rect.center

        self.rect.x += x
        self.rect.y += y



    def prep_msg(self, msg):
        """Umieszczanie komunkatu w przycisku i komunikatu game over"""
        self.msg_image = self.font.render(msg, True, self.text_color, self.button_color)
        self.msg_image_rect = self.msg_image.get_rect()
        self.msg_image_rect.center = self.rect.center
    

    def draw_button(self):
        if self.button_clicked: self.button_color = self.settings.button_color_clicked
        else: self.button_color = self.deafult_color
        self.prep_msg(self.msg)
        self.screen.fill(self.settings.button_color_clicked, self.rect)
        self.screen.fill(self.button_color, self.rect)
        self.screen.blit(self.msg_image, self.msg_image_rect)
import pygame.font
import pygame
class StartMenu():
    
    def __init__(self, game):
        """Inicjalizacja przycisku i menu początkowego"""
        self.screen = game.screen
        self.game = game
        self.screen_rect = self.screen.get_rect()

        self.msg = "START"

        # właściwości przycisku
        self.width, self.height = 200, 50
        self.button_color = (0, 255, 0)
        self.text_color = (250, 250, 250)
        self.font = pygame.font.SysFont(None, 48)

        # utworzenie prostokątnego przycisku na środku ekranu
        self.rect = pygame.Rect(0, 0, self.width, self.height)
        self.rect.center = self.screen_rect.center


    def prep_msg(self, msg):
        """Umieszczanie komunkatu w przycisku i komunikatu game over"""
        self.msg_image = self.font.render(msg, True, self.text_color, self.button_color)
        self.msg_image_rect = self.msg_image.get_rect()
        self.msg_image_rect.center = self.rect.center
    

    def draw_button(self):
        self.prep_msg(self.msg)
        self.screen.fill(self.button_color, self.rect)
        self.screen.blit(self.msg_image, self.msg_image_rect)
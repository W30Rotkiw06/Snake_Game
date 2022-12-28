import pygame
import pygame.font

class InputText():
    """Klasa przeznaczona do zarządzania oknem do podania danych użytkownika"""
    
    def __init__(self, game, coords, size):
        # potrzebne klasy
        self.game = game
        self.screen = self.game.screen
        self.screen_rect = self.screen.get_rect()
        self.settings = game.settings

        # parametry okna
        self.width, self.height = size[0], size[1]
        self.window_color = self.settings.window_color
        self.window_text = (0, 0, 0)
        self.font = pygame.font.SysFont(None, 24)

        # utworzenie okna na wpisanie danych w wyznaczonym miejscu
        self.rect = pygame.Rect(coords, size)
        self.rect.center = self.screen_rect.center

    def prep_txt(self):
        """Umieszczanie komunkatu w przycisku i komunikatu game over"""
        if len(self.game.player) == 0: self.msg_image = self.font.render("What's your name?", True, (250, 250, 250), self.window_color)
        else: self.msg_image = self.font.render(self.game.player, True, self.window_text, self.window_color)
        self.msg_image_rect = self.msg_image.get_rect()
        self.msg_image_rect.center = self.rect.center

    def draw_window(self):
        self.prep_txt()
        self.screen.fill(self.window_color, self.rect)
        self.screen.blit(self.msg_image, self.msg_image_rect)

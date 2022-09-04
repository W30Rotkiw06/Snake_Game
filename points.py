import json
import pygame
import pygame.font


class Points():
    """Klasa przeznaczona do zarządzania paskiem punktów, i zapisywaniu 
    rekordu do pliku points.json"""

    def __init__(self, game):
        """Inicjalizacja i wczytanie aktualnego rekordu"""
        self.settings = game.settings
        self.apple = game.apple
        self.screen = game.screen
        self.print_score = True

        self.screen_rect = self.screen.get_rect()
        self.high_score = 0
        self.points = 0

        # ustawienia napisów
        self.text_color = (0, 0, 0)
        self.font = pygame.font.SysFont(None, 42)
        


        self.filename = "points.json"
        try:
            with open(self.filename,) as f:
                self.high_score = json.load(f)
        except:
            pass

    def is_new_high_score(self):
        """Sprawdza, czy aktualny wynik jest większy niż rekord,
        jeśli tak, to go nadpisuje"""
        if self.points > self.high_score:
            self.high_score = self.points
            with open(self.filename, "w") as f:
                json.dump(self.high_score, f)

    def new_point(self):
        self.points += 1
        self.is_new_high_score()

    def draw_line(self):
        pygame.draw.line(self.screen, (0,0,0), (0, self.settings.line_y), (self.settings.screen_size_height, self.settings.line_y))

    def prep_score(self):
        """Przekształcenie punktacji na wygenerowany obraz"""

        if self.print_score:
            self.score_image = self.font.render(f"YOUR SCORE: {str(self.points)}", True, self.text_color, self.settings.bg_color)
            self.high_score_image = self.font.render(f"HIGH SCORE: {str(self.high_score)}", True, self.text_color, self.settings.bg_color)

            # wyświetlanie punktacji w lewym górnym rogu ekranu
            self.score_rect = self.score_image.get_rect()
            self.score_rect.left = self.screen_rect.left + 10
            self.score_rect.top = 10

            # wyświetlanie najlepszego wyniku w prawym górnym rogu
            self.high_score_rect = self.high_score_image.get_rect()
            self.high_score_rect.right = self.screen_rect.right - 10
            self.high_score_rect.top = 10

        else: # wyświetlenie game over w górnym środku ekranu
            self.score_image = self.font.render("GAME OVER", True, self.text_color, self.settings.bg_color)
            self.score_rect = self.score_image.get_rect()
            self.score_rect.centerx = self.screen_rect.centerx
            self.score_rect.top = 10


    def show_score(self):
        self.draw_line()
        self.prep_score()
        self.screen.blit(self.score_image, self.score_rect)
        if self.print_score: self.screen.blit(self.high_score_image, self.high_score_rect)
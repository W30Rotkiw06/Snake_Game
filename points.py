from __future__ import barry_as_FLUFL
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

        self.new_player = True

        self.screen_rect = self.screen.get_rect()
        self.high_score = 0
        self.points = 0

        # ustawienia napisów
        self.text_color = (0, 0, 0)
        self.font = pygame.font.SysFont(None, 42)

        self.player = "PL3"
        

        # wczytywanie tabeli wyników z plkiku do zmiennej, ewentualne utworzenie zmiennej
        self.filename = f"points_{self.settings.game_mode}.json"
        try:
            with open(self.filename) as f:
                self.scores = json.load(f)
        except:
            self.scores = []
        
        # Ustalanie wartości rekordu
        if self.scores:
            for score in self.scores:
                if score[0] >= self.high_score: self.high_score = score[0]
        else: self.high_score = 0


        # Sprawdzanie czy zawodnik znajduje się już w tabeli
        self.player.upper()
        for item in self.scores:
            if self.player == item[1]: 
                self.new_player = False
                break


        

    def is_new_high_score(self):
        """Sprawdza, czy aktualny wynik jest większy niż rekord"""
        if self.points > self.high_score: self.high_score = self.points

    def new_point(self):
        """Dodaje punkt"""
        self.points += 1
        self.is_new_high_score()

        self.update_scoretable()


    def draw_line(self):
        pygame.draw.line(self.screen, (0,0,0), (0, self.settings.line_y), (self.settings.screen_size_height, self.settings.line_y))

    def prep_score(self):
        """Przekształcenie punktacji na wygenerowany obraz"""

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



    def show_score(self):
        self.draw_line()
        self.prep_score()
        self.screen.blit(self.score_image, self.score_rect)
        self.screen.blit(self.high_score_image, self.high_score_rect)

    def update_scoretable(self):
        """Uaktualnia tabelkę z wynikami"""

        # Dopisanie wyniku gracza do tabelki
        if self.scores == [] or self.new_player:
                self.scores.append((self.points, self.player))
                self.new_player = False
        else:
            i = 0

            for item in self.scores:
                if item[1] == self.player and item[0] < self.points:
                    del self.scores[i]
                    if i == 0:  
                        self.scores.insert(0, (self.points, self.player))
                        break
                    elif item[0] < self.points:
                        for j in range(len(self.scores)):
                            if self.points < self.scores[-j][0]:
                                self.scores.append((self.points, self.player))
                                break
                            elif self.points >= self.scores[j][0]:
                                self.scores.insert(j, (self.points, self.player))
                                break
                        break
                i += 1


        # wyświetlanie tabelki
        pos = 1
        print(self.scores)
        print("NR.\tPLAYER    \tSCORE")
        for score in self.scores: 
            print(f"{pos}\t{score[1]}\t{score[0]}") # score[1] to nazwa gracza, score[0] to wynik
            pos += 1

        
        with open(self.filename, "w") as f:
                json.dump(self.scores, f)
import json


class Points():
    """Klasa przeznaczona do zarządzania punktami i zapisywaniu 
    rekordu do pliku points.json"""

    def __init__(self, game):
        """Inicjalizacja i wczytanie aktualnego rekordu"""
        self.settings = game.settings
        self.apple = game.apple
        self.high_score = 0
        self.points = 0


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
            print(f"NEW RECORD: {self.points}")
            self.high_score = self.points
            with open(self.filename, "w") as f:
                json.dump(self.high_score, f)
        else: print(self.points)

    def new_point(self):
        self.points += 1
        self.is_new_high_score()
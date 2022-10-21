import json


class Importer:

    def __init__(self):
        self.tasks = None

    def read_tasks(self):
        # DONE odczytaj plik i zdekoduj treść tutaj
        with open('taski.json', 'r', encoding='utf-8') as f:
            self.tasks = json.load(f)

    def get_tasks(self):
        # DONE zwróć zdekodowane taski tutaj
        return self.tasks
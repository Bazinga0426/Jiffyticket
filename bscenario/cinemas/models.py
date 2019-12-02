from django.db import models
from abc import ABC, abstractmethod


#Abstract Factory Method Pattern
class CinemaDetail(ABC):
    """detail about cinema"""
    @abstractmethod
    def __init__(self, description):
        self._description = description


class FontCreator(CinemaDetail):
    def __init__(self, cinemadetail):
        self._cinmadetail = cinemadetail

    def add_style(self):
        return self._description


class BoldDecorator(FontCreator):

    def __init__(self, fontcinema):
        self._fontcinema = fontcinema

    def add_style(self):
        return f"<b>{self._fontcinema.add_style()}</b>"


class ItalicDecorator(FontCreator):

    def __init__(self, fontcinema):
        self._fontcinema = fontcinema

    def add_style(self):
        return f"<i>{self._fontcinema.add_style()}</i>"


detail = BoldDecorator(CinemaDetail('Beijing cinema is good.')).add_style()
print(detail)


from django.db import models


#decorator design pattern
class CinemaDetail:
    """detail about cinema"""

    def __init__(self, description):
        self._description = description

    def add_style(self):
        return self._description


class BoldDecorator(CinemaDetail):

    def __init__(self, cinemadetail):
        self._cinemadetail = cinemadetail

    def add_style(self):
        return f"<b>{self._cinemadetail.add_style()}</b>"


class ItalicDecorator(CinemaDetail):

    def __init__(self, cinemadetail):
        self._cinemadetail = cinemadetail

    def add_style(self):
        return f"<i>{self._cinemadetail.add_style()}</i>"


detail = BoldDecorator(CinemaDetail('Beijing cinema is good.')).add_style()
print(detail)


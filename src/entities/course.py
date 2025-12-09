from dataclasses import dataclass


@dataclass
class Course:
    """Sisältää kurssin tiedot

    Attributes:
        id: kurssin tunniste
        name: kurssin nimi
        credits: kurssin opintopistemäärä
        completed: onko kurssi suoritettu
    """
    id: int
    name: str
    credits: int
    completed: bool = False

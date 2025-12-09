from dataclasses import dataclass

@dataclass
class User:
    """Sisältää käyttäjän tiedot

    Attributes:
        id: käyttäjän tunniste
        username: käyttäjänimi
    """
    id: int
    username: str

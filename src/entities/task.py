from dataclasses import dataclass


@dataclass
class Task:
    """Sisältää luodun kurssin tiedot

    Attributes:
        id: tehtävän tunniste.
        content: tehtävän kuvaus
        deadline: tehtävän deadline
        course_id: kurssin tunniste, johon tehtävä kuuluu
        done: onko tehtävä suoritettu
    """

    id: int
    content: str
    deadline: str
    course_id: int
    done: bool


@dataclass
class NewTask:
    """sisältää luotavan tehtävän tiedot

    Attributes:
        content: Tehtävän kuvaus
        deadline: Tehtävän deadline
    """

    content: str
    deadline: str

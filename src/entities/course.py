from dataclasses import dataclass


@dataclass
class Course:
    name: str
    credits: int
    completed: bool = False

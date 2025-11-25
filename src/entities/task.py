from dataclasses import dataclass


@dataclass
class Task:
    content: str
    deadline: str
    course_id: int

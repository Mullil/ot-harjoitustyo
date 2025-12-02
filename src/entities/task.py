from dataclasses import dataclass


@dataclass
class Task:
    content: str
    deadline: str
    course_id: int
    done: bool

@dataclass
class NewTask:
    content: str
    deadline: str

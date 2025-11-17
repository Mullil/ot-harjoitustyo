

class Course:
    def __init__(self, name, credits, completed=False):
        self.name = name
        self.credits = credits
        self.completed = completed
        self.tasks = []
    
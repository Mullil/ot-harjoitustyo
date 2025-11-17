
class Task:
    def __init__(self, content, course_id, deadline=None):
        self.content = content
        self.deadline = deadline
        self.course_id = course_id
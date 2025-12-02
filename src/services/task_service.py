import sqlite3
from entities.task import Task

class TaskService:
    def add_tasks(self, tasks, course_id):
        conn = sqlite3.connect("app.db")
        cur = conn.cursor()
        for task in tasks:
            cur.execute(
                "INSERT INTO tasks (course_id, content, deadline) VALUES (?, ?, ?)",
                (course_id, task.content, task.deadline)
            )
        conn.commit()
        return True

    def get_course_tasks(self, course_id):
        conn = sqlite3.connect("app.db")
        cur = conn.cursor()
        result = cur.execute(
                "SELECT content, deadline, course_id, done FROM tasks WHERE id = ?", (course_id,)
                )
        return [Task(content=t[0], deadline=t[1], course_id=t[2], done=t[3]) for t in result]

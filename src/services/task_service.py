from entities.task import Task
from db_helper import get_conn

class TaskService:
    """Luokka, jonka avulla hallitaan kurssien tehtäviä tietokannassa

    Attributes:
        conn: yhteys tietokantaan
    """
    def __init__(self):
        """Luokan konstruktori, joka luo yhteyden tietokantaan
        """
        self.conn = get_conn()

    def add_tasks(self, tasks, course_id):
        """Lisää kurssille tehtäviä

        Args:
            tasks: lista tehtäviä
            course_id: kurssin tunniste

        Returns:
            True merkitsemään onnistunutta tehtävien lisäystä
        """
        cur = self.conn.cursor()
        for task in tasks:
            cur.execute(
                "INSERT INTO tasks (course_id, content, deadline) VALUES (?, ?, ?)",
                (course_id, task.content, task.deadline)
            )
        self.conn.commit()
        cur.close()
        return True

    def get_course_tasks(self, course_id):
        """Palauttaa kurssin tehtävät

        Args:
            course_id: kurssin tunniste

        Returns:
            tasks: lista kurssin tehtäviä
        """
        cur = self.conn.cursor()
        cur.execute(
                "SELECT id, content, deadline, course_id, done FROM tasks WHERE course_id = ?",
                (course_id,)
                )
        result = cur.fetchall()
        cur.close()
        tasks = [
            Task(id=t[0], content=t[1], deadline=t[2], course_id=t[3], done=t[4]) for t in result
        ]
        return tasks

    def complete_task(self, task_id):
        """Merkitsee kurssin tehtävän tehdyksi

        Args:
            task_id: tehtävän tunniste
        """
        cur = self.conn.cursor()
        cur.execute(
            "UPDATE tasks SET done = 1 WHERE id = ?", (task_id)
        )
        self.conn.commit()
        cur.close()

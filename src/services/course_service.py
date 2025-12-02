import sqlite3
from entities.course import Course


class CourseService:
    def get_current_courses(self, user_id):
        conn = sqlite3.connect("app.db")
        cur = conn.cursor()
        result = cur.execute(
            "SELECT id, name, credits FROM courses WHERE completed = 0 AND user_id = ?",
            (user_id,)
        )
        return [Course(c[0], c[1], c[2]) for c in result]

    def get_completed_courses(self, user_id):
        conn = sqlite3.connect("app.db")
        cur = conn.cursor()
        result = cur.execute(
            "SELECT id, name, credits, completed FROM courses WHERE completed = 1 AND user_id = ?",
            (user_id,)
        )
        return [Course(c[0], c[1], c[2], c[3]) for c in result]

    def create_course(self, user_id, name, course_credits):
        conn = sqlite3.connect("app.db")
        cur = conn.cursor()
        cur.execute(
            "INSERT INTO courses (user_id, name, credits) VALUES (?, ?, ?)",
            (user_id, name, course_credits)
        )
        conn.commit()
        course_id = cur.lastrowid
        return course_id

    def complete_course(self, course_id):
        conn = sqlite3.connect("app.db")
        cur = conn.cursor()
        cur.execute(
            "UPDATE courses SET completed 1 WHERE id = ?", (course_id)
        )
        return True

    def delete_course(self, course_id):
        conn = sqlite3.connect("app.db")
        cur = conn.cursor()
        cur.execute(
            "DELETE FROM courses WHERE id = ?",
            (course_id,)
        )
        return True

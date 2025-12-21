from entities.course import Course
from db_helper import get_conn, commit_and_close

class CourseService:
    """Luokka, jonka avulla hallitaan ja hetaan kurssien tietoja tietokannasta

    Attributes:
        conn: Yhteys tietokantaan
    """
    def __init__(self):
        """Luokan konstruktori, joka luo yhteyden tietokantaan
        
        Args:
            conn: Yhteys tietokantaan
        """
        self.conn = get_conn()

    def get_current_courses(self, user_id):
        """Hakee käyttäjän kurssit, joita ei ole vielä suoritettu

        Args:
            user_id: käyttäjän tunniste

        Returns:
            courses: Lista kursseja ja niiden tietoja
        """
        cur = self.conn.cursor()
        cur.execute(
            "SELECT id, name, credits FROM courses WHERE completed = 0 AND user_id = ?",
            (user_id,)
        )
        result = cur.fetchall()
        cur.close()
        courses = [Course(c[0], c[1], c[2]) for c in result]
        return courses

    def get_completed_courses(self, user_id):
        """Hakee käyttäjän kurssit, jotka on suoritettu

        Args:
            user_id: käyttäjän tunniste

        Returns:
            courses: Lista kursseja ja niiden tietoja
        """
        cur = self.conn.cursor()
        cur.execute(
            "SELECT id, name, credits, completed FROM courses WHERE completed = 1 AND user_id = ?",
            (user_id,)
        )
        result = cur.fetchall()
        cur.close()
        courses = [Course(c[0], c[1], c[2], c[3]) for c in result]
        return courses

    def create_course(self, user_id, name, course_credits):
        """Luo käyttäjälle kurssin annetuilla tiedoilla

        Args:
            user_id: käyttäjän tunniste
            name: kurssin nimi
            course_credits: kurssin opintopistemäärä

        Returns:
            course_id: kurssin tunniste
        """
        cur = self.conn.cursor()
        cur.execute(
            "INSERT INTO courses (user_id, name, credits) VALUES (?, ?, ?)",
            (user_id, name, course_credits)
        )
        self.conn.commit()
        course_id = cur.lastrowid
        cur.close()
        return course_id

    def complete_course(self, course_id):
        """ Merkitsee kurssin suoritetuksi

        Args:
            course_id: kurssin tunniste

        Returns:
            True merkitsemään onnistunutta operaatiota
        """
        cur = self.conn.cursor()
        cur.execute(
            "UPDATE courses SET completed = 1 WHERE id = ?", (course_id,)
        )
        commit_and_close(self.conn, cur)
        return True

    def delete_course(self, course_id):
        """Poistaa kurssin

        Args:
            course_id: kurssin tunniste

        Returns:
            True merkitsemään onnistunutta operaatiota
        """
        cur = self.conn.cursor()
        cur.execute(
            "DELETE FROM courses WHERE id = ?",
            (course_id,)
        )
        cur.execute(
            "DELETE FROM tasks WHERE course_id = ?",(course_id,))
        commit_and_close(self.conn, cur)
        return True

    def get_course(self, course_id):
        """Palauttaa yksittäisen kurssin tiedot

        Args:
            course_id: kurssin tunniste

        Returns:
            course: kurssin tiedot
        """
        cur = self.conn.cursor()
        cur.execute(
            "SELECT id, name, credits, completed FROM courses WHERE id = ?", (course_id,)
        )
        result = cur.fetchone()
        cur.close()
        course = Course(result[0], result[1], result[2], result[3])
        return course

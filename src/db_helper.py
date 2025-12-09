import sqlite3


def get_conn():
    """Alustaa yhteyden tietokantaan

    Returns:
        conn: yhteys tietokantaan
    """
    conn = sqlite3.connect("app.db")
    return conn

def drop_tables():
    """Poistaa tietokannan taulut
    """
    conn = get_conn()
    cur = conn.cursor()
    cur.execute("DROP TABLE IF EXISTS users")
    cur.execute("DROP TABLE IF EXISTS courses")
    cur.execute("DROP TABLE IF EXISTS tasks")
    conn.close()


def create_db():
    """Luo tietokannan
    """
    conn = get_conn()
    cur = conn.cursor()
    cur.execute("""CREATE TABLE IF NOT EXISTS users
                    (id INTEGER PRIMARY KEY AUTOINCREMENT,
                    username TEXT NOT NULL,
                    password TEXT NOT NULL)
                 """)
    cur.execute("""CREATE TABLE IF NOT EXISTS courses
                    (id INTEGER PRIMARY KEY AUTOINCREMENT,
                    user_id INTEGER,
                    name TEXT NOT NULL,
                    credits INTEGER NOT NULL,
                    completed BOOLEAN DEFAULT 0,
                    FOREIGN KEY (user_id) REFERENCES users(id))""")
    cur.execute("""CREATE TABLE IF NOT EXISTS tasks
                    (id INTEGER PRIMARY KEY AUTOINCREMENT,
                    course_id INTEGER,
                    content TEXT NOT NULL,
                    deadline TEXT,
                    done BOOLEAN DEFAULT 0,
                    FOREIGN KEY (course_id) REFERENCES courses(id))""")
    conn.commit()
    conn.close()

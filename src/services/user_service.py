import sqlite3
from entities.user import User


class InvalidCredentialsError(Exception):
    pass


class InvalidPasswordError(Exception):
    pass


class UsernameExistsError(Exception):
    pass


class UserService:
    def __init__(self):
        self.current_user = None

    def get_users(self):
        conn = sqlite3.connect("app.db")
        cur = conn.cursor()
        result = cur.execute("SELECT username FROM users")
        return list(map(lambda x: x[0], result.fetchall()))

    def register(self, username, password, confirmation):
        if len(password) < 8:
            raise InvalidPasswordError("The password is too short")
        if username in self.get_users():
            raise UsernameExistsError("Username already exists")
        if password != confirmation:
            raise InvalidPasswordError("The passwords do not match")

        conn = sqlite3.connect("app.db")
        cur = conn.cursor()
        cur.execute(
            "INSERT INTO users (username, password) VALUES (?, ?)", (username, password))
        conn.commit()
        self.current_user = User(1, username) # 1 will be changed to a real id
        return True

    def login(self, username, password):
        conn = sqlite3.connect("app.db")
        cur = conn.cursor()
        result = cur.execute(
            """SELECT id, username FROM users WHERE username = ?
               AND password = ?""", (username, password))
        user = result.fetchone()
        if user is None:
            raise InvalidCredentialsError("Wrong password")
        user_id, username = user[0], user[1]
        self.current_user = User(user_id, username)
        return True


user_service = UserService()

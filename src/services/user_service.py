from entities.user import User
from db_helper import get_conn


class InvalidCredentialsError(Exception):
    pass


class InvalidPasswordError(Exception):
    pass


class UsernameExistsError(Exception):
    pass


class UserService:
    """Luokka, jonka avulla hallitaan käyttäjiin liittyviä tietoja

    Attributes:
        current_user: Järjestelmään kirjautunut käyttäjä
        conn: yhteys tietokantaan
    """
    def __init__(self):
        """Luokan kontruktori, joka alustaa käyttäjän statuksen ja yhteyden tietokantaan
        """
        self.current_user = None
        self.conn = get_conn()

    def get_users(self):
        """Palauttaa listan kaikista käyttäjistä

        Returns:
            users: lista käyttäjänimiä
        """
        cur = self.conn.cursor()
        result = cur.execute("SELECT username FROM users")
        users = list(map(lambda x: x[0], result.fetchall()))
        return users

    def register(self, username, password, confirmation):
        """Rekisteröi käyttäjän järjestelmään

        Args:
            username: käyttäjänimi
            password: salasana
            confirmation: Salasanan vahvistus

        Raises:
            InvalidPasswordError: Väärä salasana
            UsernameExistsError: Käyttäjänimi on jo olemassa
            InvalidPasswordError: Salasana ei ole kelvollinen

        Returns:
            True, jos rekisteröinti onnistui
        """
        if len(password) < 8:
            raise InvalidPasswordError("The password is too short")
        if username in self.get_users():
            raise UsernameExistsError("Username already exists")
        if password != confirmation:
            raise InvalidPasswordError("The passwords do not match")

        cur = self.conn.cursor()
        cur.execute(
            "INSERT INTO users (username, password) VALUES (?, ?)", (username, password))
        self.conn.commit()
        self.current_user = User(1, username) # 1 will be changed to a real id
        return True

    def login(self, username, password):
        """Kirjaa käyttäjän sisään

        Args:
            username: käyttäjänimi
            password: salasana

        Raises:
            InvalidCredentialsError: Väärä käyttäjänimi tai salasana

        Returns:
            True, jos kirjautuminen onnistui
        """
        cur = self.conn.cursor()
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

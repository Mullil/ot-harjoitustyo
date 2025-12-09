from ui.starting_view import StartingView
from ui.login_view import LoginView
from ui.register_view import RegisterView
from ui.index_view import IndexView
from ui.create_course_view import CreateCourseView
from ui.course_view import CourseView
from os import getenv


class UI:
    """Luokka, joka hallinnoi sovelluksen näkymiä

    Attributes:
        root: juuri
        current_view: näkymä, jossa ollaan
    """
    def __init__(self, root):
        """
        Alustaa UI-luokan ja asettaa juurielementin sekä nykyisen näkymän.

        Args:
            root: juuri
        """
        self.root = root
        self.current_view = None

    def start(self):
        """Näyttää aloitusnäkymän
        """

        if self.current_view:
            self.current_view.destroy()

        if getenv("DEV_ENV") == "True":
            self.show_index_view()
        else:
            self.current_view = StartingView(
                self.root, self.show_login_view, self.show_register_view)
            self.current_view.initialize_view()

    def show_register_view(self):
        """Näyttää rekisteröitymisnäkymän
        """

        if self.current_view:
            self.current_view.destroy()
        self.current_view = RegisterView(self.root, self.show_index_view)
        self.current_view.initialize_view()

    def show_login_view(self):
        """Näyttää kirjautumisnäkymän
        """

        if self.current_view:
            self.current_view.destroy()
        self.current_view = LoginView(self.root, self.show_index_view)
        self.current_view.initialize_view()

    def show_index_view(self):
        """Näyttää listan kursseista
        """

        if self.current_view:
            self.current_view.destroy()
        self.current_view = IndexView(
            self.root, self.show_create_course_view, self.start, self.show_course_view)
        self.current_view.initialize_view()

    def show_create_course_view(self):
        """Näyttää kurssien luomisnäkymän
        """

        if self.current_view:
            self.current_view.destroy()
        self.current_view = CreateCourseView(self.root, self.show_index_view)
        self.current_view.initialize_view()

    def show_course_view(self, course):
        """Näyttää yksittäisen kurssin tiedot

        Args:
            course: kurssi, jonka tiedot näytetään
        """
        if self.current_view:
            self.current_view.destroy()
        self.current_view = CourseView(self.root, self.show_index_view)
        self.current_view.initialize_view(course.id)
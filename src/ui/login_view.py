from tkinter import ttk
from services.user_service import UserService
from services.user_service import InvalidCredentialsError
from ui.common import create_button, create_entry


class LoginView:
    def __init__(self, root, login, back):
        self.root = root
        self.frame = None
        self.login = login
        self.back = back

    def destroy(self):
        self.frame.destroy()

    def initialize_view(self, message=None):
        self.frame = ttk.Frame(master=self.root)
        if message:
            error = ttk.Label(
                self.frame,
                text=message,
            )
            error.pack(padx=10, pady=10)

        self.username_entry = create_entry(frame=self.frame, text="Username")
        self.password_entry = create_entry(frame=self.frame, text="Password")

        create_button(frame=self.frame, text="Login", command=self.handle_login)
        create_button(frame=self.frame, text="Go back", command=self.handle_go_back)
        self.frame.pack()

    def handle_login(self):
        user_service = UserService()
        try:
            user_service.login(self.username_entry.get(),
                              self.password_entry.get())
            self.login(user_service.current_user)
        except(InvalidCredentialsError):
            self.destroy()
            self.initialize_view(message="Wrong username of password")

    def handle_go_back(self):
        self.back()

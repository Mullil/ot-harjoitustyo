from tkinter import ttk
from services.user_service import UserService


class LoginView:
    def __init__(self, root, login):
        self.root = root
        self.frame = None
        self.login = login

    def destroy(self):
        self.frame.destroy()

    def initialize_view(self):
        self.frame = ttk.Frame(master=self.root)

        username_label = ttk.Label(master=self.frame, text="Username")
        self.username_entry = ttk.Entry(master=self.frame)
        username_label.grid(padx=5, pady=5)
        self.username_entry.grid(padx=5, pady=5)
        password_label = ttk.Label(master=self.frame, text="Password")
        self.password_entry = ttk.Entry(master=self.frame)
        password_label.grid(padx=5, pady=5)
        self.password_entry.grid(padx=5, pady=5)

        login_button = ttk.Button(
            master=self.frame,
            text="Login",
            command=self.handle_login
        )
        login_button.grid(padx=5, pady=5)
        self.frame.pack()

    def handle_login(self):
        user_service = UserService()
        if user_service.login(self.username_entry.get(),
                              self.password_entry.get()
                              ):
            self.login()

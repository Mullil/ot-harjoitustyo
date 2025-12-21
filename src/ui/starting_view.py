from tkinter import ttk, constants
from ui.common import create_button


class StartingView:
    def __init__(self, root, login, register):
        self.root = root
        self.frame = None
        self.login = login
        self.register = register

    def pack(self):
        self.frame.pack(fill=constants.X)

    def destroy(self):
        self.frame.destroy()

    def initialize_view(self):
        self.frame = ttk.Frame(master=self.root)
        self.frame.pack(fill=constants.X)

        create_button(frame=self.frame, text="Login", command=self.login)
        create_button(frame=self.frame, text="Register", command=self.register)

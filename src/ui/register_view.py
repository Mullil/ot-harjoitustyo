from tkinter import ttk
from services.user_service import UserService


class RegisterView:
    def __init__(self, root, register):
        self.root = root
        self.frame = None
        self.register = register

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
        confirmation_label = ttk.Label(
            master=self.frame, text="Password confimation")
        self.confirmation_entry = ttk.Entry(master=self.frame)
        confirmation_label.grid(padx=5, pady=5)
        self.confirmation_entry.grid(padx=5, pady=5)

        register_button = ttk.Button(
            master=self.frame,
            text="Register",
            command=self.handle_register
        )
        register_button.grid(padx=5, pady=5)
        self.frame.pack()

    def handle_register(self):
        user_service = UserService()
        if user_service.register(self.username_entry.get(),
                                 self.password_entry.get(),
                                 self.confirmation_entry.get()):
            self.register()

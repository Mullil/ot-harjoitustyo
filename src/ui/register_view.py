from tkinter import ttk
from services.user_service import UserService
from ui.common import create_button, create_entry


class RegisterView:
    def __init__(self, root, register, back):
        self.root = root
        self.frame = None
        self.register = register
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
        self.confirmation_entry = create_entry(frame=self.frame, text="Password confirmation")

        create_button(frame=self.frame, text="Register", command=self.handle_register)
        create_button(frame=self.frame, text="Go back", command=self.handle_go_back)

        self.frame.pack()

    def handle_register(self):
        user_service = UserService()
        try:
            user_service.register(self.username_entry.get(),
                                 self.password_entry.get(),
                                 self.confirmation_entry.get())
            self.register(user_service.current_user)
        except Exception as e:
            self.destroy()
            self.initialize_view(message=e)

    def handle_go_back(self):
        self.back()

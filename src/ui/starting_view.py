from tkinter import ttk, constants

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

        login_button = ttk.Button(
            master=self.frame,
            text="Login",
            command=self.login
        )
        login_button.pack()

        register_button = ttk.Button(
            master=self.frame,
            text="Register",
            command=self.register
        )
        register_button.pack()
from tkinter import ttk

class LoginView:
    def __init__(self, root):
        self.root = root
        self.frame = None

    def destroy(self):
        self.frame.destroy()

    def initialize_view(self):
        self.frame = ttk.Frame(master=self.root)

        username_label = ttk.Label(master=self.frame, text="Username")
        username_entry = ttk.Entry(master=self.frame)
        username_label.grid(padx=5, pady=5)
        username_entry.grid(padx=5, pady=5)
        password_label = ttk.Label(master=self.frame, text="Password")
        password_entry = ttk.Entry(master=self.frame)
        password_label.grid(padx=5, pady=5)
        password_entry.grid(padx=5, pady=5)

        login_button = ttk.Button(
            master=self.frame,
            text="Login",
            command=print("a")
        )
        login_button.grid(padx=5, pady=5)
        self.frame.pack()
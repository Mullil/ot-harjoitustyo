from tkinter import ttk

class IndexView:
    def __init__(self, root):
        self.root = root
        self.frame = None

    def initialize_view(self):
        self.frame = ttk.Frame(master=self.root)
        self.frame.pack()
        header = ttk.Label(
            self.frame,
            text="My courses",
        )
        header.pack(padx=10, pady=10)
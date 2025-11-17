from ui.starting_view import StartingView
from ui.login_view import LoginView
from ui.register_view import RegisterView
from ui.index_view import IndexView

class UI:
    def __init__(self, root):
        self.root = root
        self.current_view = None

    def start(self):
        if self.current_view:
            self.current_view.destroy()
        
        self.current_view = StartingView(self.root, self.show_login_view, self.show_register_view)
        self.current_view.initialize_view()

    def show_register_view(self):
        if self.current_view:
            self.current_view.destroy()
        self.current_view = RegisterView(self.root, self.show_index_view)
        self.current_view.initialize_view()

    def show_login_view(self):
        if self.current_view:
            self.current_view.destroy()
        self.current_view = LoginView(self.root)
        self.current_view.initialize_view()

    def show_index_view(self):
        if self.current_view:
            self.current_view.destroy()
        self.current_view = IndexView(self.root)
        self.current_view.initialize_view()
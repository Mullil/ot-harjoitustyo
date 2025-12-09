from tkinter import Tk
from ui.ui import UI
import db_helper


def main():
    """Alustaa tietokannan ja käyttöliittymän
    """
    db_helper.drop_tables()
    db_helper.create_db()
    root = Tk()
    root.title("Study management app")
    view = UI(root)
    view.start()
    root.mainloop()


if __name__ == "__main__":
    main()

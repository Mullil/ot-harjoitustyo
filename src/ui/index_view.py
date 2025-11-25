import tkinter as tk
from tkinter import ttk
from services.course_service import CourseService


class IndexView:
    def __init__(self, root, show_create_course_view, show_starting_view):
        self.root = root
        self.frame = None
        self.show_create_course_view = show_create_course_view
        self.show_starting_view = show_starting_view

    def destroy(self):
        self.frame.destroy()

    def initialize_view(self):
        user_id = 1
        self.frame = ttk.Frame(master=self.root)
        self.frame.pack()
        logout_button = ttk.Button(
            master=self.frame,
            text="Log out",
            command=self.handleLogout
        )
        logout_button.pack(padx=5, pady=5)
        header = ttk.Label(
            self.frame,
            text="My courses",
        )
        header.pack(padx=10, pady=10)
        scrollbar = ttk.Scrollbar(self.frame)
        scrollbar.pack(side=tk.RIGHT, fill=tk.Y)
        listbox = tk.Listbox(self.frame, yscrollcommand=scrollbar.set)
        listbox.pack(fill=tk.BOTH, expand=True)
        scrollbar.config(command=listbox.yview)
        course_service = CourseService()
        courses = course_service.get_current_courses(user_id=user_id)
        total = 0
        for course in courses:
            total += course.credits
            listbox.insert(tk.END, f"{course.name}, {course.credits} cr")
        listbox.insert(tk.END, f"total credits: {total}")
        add_new_button = ttk.Button(
            master=self.frame,
            text="Add new course",
            command=self.handleAddNew
        )
        add_new_button.pack(padx=5, pady=5)

    def handleAddNew(self):
        self.show_create_course_view()

    def handleLogout(self):
        self.show_starting_view()

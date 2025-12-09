import tkinter as tk
from tkinter import ttk
from services.course_service import CourseService


class IndexView:
    def __init__(
            self, root,
            show_create_course_view,
            show_starting_view,
            show_course_view):
        self.root = root
        self.frame = None
        self.show_create_course_view = show_create_course_view
        self.show_starting_view = show_starting_view
        self.show_course_view = show_course_view

    def destroy(self):
        self.frame.destroy()

    def initialize_view(self):
        self.user_id = 1
        self.frame = ttk.Frame(master=self.root)
        self.frame.pack()
        logout_button = ttk.Button(
            master=self.frame,
            text="Log out",
            command=self.handle_logout
        )
        logout_button.pack(padx=5, pady=5)
        header = ttk.Label(
            self.frame,
            text="My courses",
        )
        header.pack(padx=10, pady=10)
        scrollbar = ttk.Scrollbar(self.frame)
        scrollbar.pack(side=tk.RIGHT, fill=tk.Y)
        self.listbox = tk.Listbox(self.frame, yscrollcommand=scrollbar.set)
        self.listbox.pack(fill=tk.BOTH, expand=True)
        scrollbar.config(command=self.listbox.yview)
        course_service = CourseService()
        self.courses = course_service.get_current_courses(user_id=self.user_id)
        total = 0
        for course in self.courses:
            total += course.credits
            self.listbox.insert(tk.END, f"{course.name}, {course.credits} cr")
        
        self.listbox.insert(tk.END, f"total credits: {total}")

        # Generoitu koodi alkaa
        self.listbox.bind("<<ListboxSelect>>", self.handle_select)
        # Generoitu koodi loppuu

        add_new_button = ttk.Button(
            master=self.frame,
            text="Add new course",
            command=self.handle_add_new
        )
        add_new_button.pack(padx=5, pady=5)

    def handle_add_new(self):
        self.show_create_course_view()

    def handle_logout(self):
        self.show_starting_view()

    # Generoitu koodi alkaa
    def handle_select(self, event):
        course_service = CourseService()
        self.courses = course_service.get_current_courses(user_id=self.user_id)
        selected = event.widget.curselection()
        idx = selected[0]
        course = self.courses[idx]
        self.show_course_view(course)
    # Generoitu koodi loppuu
import tkinter as tk
from tkinter import ttk
from services.course_service import CourseService
from ui.common import create_button, create_header


class IndexView:
    def __init__(
            self, root,
            show_create_course_view,
            show_starting_view,
            show_course_view,
            current_user):
        self.root = root
        self.frame = None
        self.show_create_course_view = show_create_course_view
        self.show_starting_view = show_starting_view
        self.show_course_view = show_course_view
        self.current_user = current_user

    def destroy(self):
        self.frame.destroy()

    def initialize_view(self):
        self.frame = ttk.Frame(master=self.root)
        self.frame.pack()

        create_button(frame=self.frame, text="Log out", command=self.handle_logout)
        create_header(frame=self.frame, text="My courses")

        self.course_service = CourseService()
        self.courses = self.course_service.get_current_courses(user_id=self.current_user.id)
        self.completed_courses = self.course_service.get_completed_courses(user_id=self.current_user.id)

        self.list_courses(self.courses, select=self.handle_select)

        create_button(frame=self.frame, text="Add new course", command=self.handle_add_new)
        create_header(frame=self.frame, text="Completed courses")

        self.list_courses(self.completed_courses, select=self.handle_select_completed)

    def list_courses(self, courses, select):
        # Generoitu koodi alkaa
        container = ttk.Frame(self.frame)
        container.pack(fill=tk.BOTH, expand=True)
        # Generoitu koodi loppuu

        scrollbar = ttk.Scrollbar(container)
        scrollbar.pack(side=tk.RIGHT, fill=tk.Y)
        listbox = tk.Listbox(container, yscrollcommand=scrollbar.set)
        listbox.pack(fill=tk.BOTH, expand=True)
        scrollbar.config(command=listbox.yview)
        total = 0
        for course in courses:
            total += course.credits
            listbox.insert(tk.END, f"{course.name}, {course.credits} cr")
        
        listbox.insert(tk.END, f"total credits: {total}")

        # Generoitu koodi alkaa
        listbox.bind("<<ListboxSelect>>", select)
        # Generoitu koodi loppuu

    def handle_add_new(self):
        self.show_create_course_view(self.current_user)

    def handle_logout(self):
        self.show_starting_view()

    # Generoitu koodi alkaa
    def handle_select(self, event):
        selected = event.widget.curselection()
        idx = selected[0]
        course = self.courses[idx]
        self.show_course_view(course, self.current_user)
    # Generoitu koodi loppuu

    def handle_select_completed(self, event):
        selected = event.widget.curselection()
        idx = selected[0]
        course = self.completed_courses[idx]
        self.show_course_view(course, self.current_user)
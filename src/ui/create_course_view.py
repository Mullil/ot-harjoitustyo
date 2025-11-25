import tkinter as tk
from tkinter import ttk
from services.course_service import CourseService


class CreateCourseView:
    def __init__(self, root, show_index_view):
        self.root = root
        self.frame = None
        self.show_index_view = show_index_view

    def destroy(self):
        self.frame.destroy()

    def initialize_view(self):
        self.frame = ttk.Frame(master=self.root)
        self.frame.pack()
        header = ttk.Label(
            self.frame,
            text="Create course",
        )
        header.pack(padx=10, pady=10)

        name_label = ttk.Label(master=self.frame, text="Course name")
        self.name_entry = ttk.Entry(master=self.frame)
        name_label.pack(padx=5, pady=5)
        self.name_entry.pack(padx=5, pady=5)

        credits_label = ttk.Label(master=self.frame, text="Credits")
        self.credits_entry = ttk.Entry(master=self.frame)
        credits_label.pack(padx=5, pady=5)
        self.credits_entry.pack(padx=5, pady=5)

        create_button = ttk.Button(
            master=self.frame,
            text="Add course",
            command=self.handle_create
        )
        create_button.pack(padx=5, pady=5)
        self.frame.pack()

    def handle_create(self):
        course_service = CourseService()
        course_service.create_course(
            1,
            self.name_entry.get(),
            self.credits_entry.get(),
        )
        self.show_index_view()

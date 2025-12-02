import tkinter as tk
from tkinter import ttk
from services.course_service import CourseService
from services.task_service import TaskService
from entities.task import NewTask


class CreateCourseView:
    def __init__(self, root, show_index_view):
        self.root = root
        self.frame = None
        self.show_index_view = show_index_view
        self.tasks = []

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

        task_header = ttk.Label(
            self.frame,
            text="Course tasks",
        )
        task_header.pack(padx=10, pady=10)

        task_label = ttk.Label(master=self.frame, text="Task description")
        self.task_entry = ttk.Entry(master=self.frame)
        task_label.pack(padx=5, pady=5)
        self.task_entry.pack(padx=5, pady=5)

        deadline_label = ttk.Label(master=self.frame, text="Task deadline")
        self.deadline_entry = ttk.Entry(master=self.frame)
        deadline_label.pack(padx=5, pady=5)
        self.deadline_entry.pack(padx=5, pady=5)

        # Generoitu koodi alkaa
        self.task_list = ttk.Treeview(
            master=self.frame,
            columns=("description", "deadline"),
            show="headings",
            height=5
        )
        self.task_list.heading("description", text="Description")
        self.task_list.heading("deadline", text="Deadline")
        self.task_list.pack(padx=5, pady=5)
        # Generoitu koodi päättyy

        task_button = ttk.Button(
            master=self.frame,
            text="Add task",
            command=self.add_task
        )
        task_button.pack(padx=5, pady=5)

        create_button = ttk.Button(
            master=self.frame,
            text="Add course",
            command=self.handle_create
        )
        create_button.pack(padx=5, pady=5)
        self.frame.pack()

    def handle_create(self):
        course_service = CourseService()
        task_service = TaskService()
        course_id = course_service.create_course(
            1,
            self.name_entry.get(),
            self.credits_entry.get(),
        )
        task_service.add_tasks(self.tasks, course_id)
        self.show_index_view()

    def add_task(self):
        task = NewTask(self.task_entry.get(), self.deadline_entry.get())
        self.tasks.append(task)
        self.task_entry.delete(0, tk.END)
        self.deadline_entry.delete(0, tk.END)
        # Generoitu koodi alkaa
        self.task_list.insert("", "end", values=(task.content, task.deadline))
        # Generoitu koodi päättyy

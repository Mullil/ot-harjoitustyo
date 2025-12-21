import tkinter as tk
from tkinter import ttk
from services.course_service import CourseService
from services.task_service import TaskService
from entities.task import NewTask
from ui.common import create_button, create_header, create_entry


class CreateCourseView:
    """Luokka, joka hallitsee kurssien  luomisnäkymää

    Attributes:
        root: juuri
        frame: runko
        show_index_view: funktio, joka näyttää kurssit listaavan näkymän
    """
    def __init__(self, root, show_index_view, current_user):
        """Luokan konstruktori

        Args:
            root: juuri
            show_index_view: funktio, joka näyttää kurssit listaavan näkymän
            current_user: kirjautunut käyttäjä
        """
        self.root = root
        self.frame = None
        self.show_index_view = show_index_view
        self.tasks = []
        self.current_user = current_user

    def destroy(self):
        """Poistaa luodun näkymän
        """
        self.frame.destroy()

    def initialize_view(self, error=None):
        """Luo näkymän kurssien luomiselle
        """
        self.frame = ttk.Frame(master=self.root)
        self.frame.pack()

        if error:
            message = ttk.Label(
                self.frame,
                text=error,
            )
            message.pack(padx=10, pady=10)

        create_button(frame=self.frame, text="Go back", command=lambda: self.show_index_view(self.current_user))
        create_header(frame=self.frame, text="Create course")

        self.name_entry = create_entry(frame=self.frame, text="Course name")
        self.credits_entry = create_entry(frame=self.frame, text="Credits")

        create_header(frame=self.frame, text="Course tasks")

        self.task_entry = create_entry(frame=self.frame, text="Task description")
        self.deadline_entry = create_entry(frame=self.frame, text="Task deadline")

        create_button(frame=self.frame, text="add task", command=self.add_task)
        create_button(frame=self.frame, text="Add course", command=self.handle_create)
        create_header(frame=self.frame, text="Added tasks")
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
        self.frame.pack()

    def handle_create(self):
        """Lisää tietokantaan kurssin annetuilla tiedoilla
        """
        course_service = CourseService()
        task_service = TaskService()
        try:
            cr = int(self.credits_entry.get())
            course_id = course_service.create_course(
                self.current_user.id,
                self.name_entry.get(),
                cr,
            )
            task_service.add_tasks(self.tasks, course_id)
            self.show_index_view(self.current_user)
        except:
            self.destroy()
            self.initialize_view(error="Invalid credits")

    def add_task(self):
        """Lisää kurssille lisättäväksi tehtävän
        """
        task = NewTask(self.task_entry.get(), self.deadline_entry.get())
        self.tasks.append(task)
        self.task_entry.delete(0, tk.END)
        self.deadline_entry.delete(0, tk.END)
        # Generoitu koodi alkaa
        self.task_list.insert("", "end", values=(task.content, task.deadline))
        # Generoitu koodi päättyy

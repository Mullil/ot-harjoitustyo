from services.task_service import TaskService
from services.course_service import CourseService
from tkinter import ttk

class CourseView:
    """Luokka, joka hallitsee yksittäisen kurssin näkymää

    Attributes:
        root: juuri
        frame: runko
        show_index_view: funktio, joka näyttää kurssit listaavan näkymän
    """
    def __init__(self, root, show_index_view):
        """Luokan konstruktori

        Args:
            root: juuri
            show_index_view: funktio, joka näyttää kurssit listaavan näkymän
        """
        self.root = root
        self.frame = None
        self.show_index_view = show_index_view
        self.course_service = CourseService()
    
    def destroy(self):
        """Poistaa luodun näkymän
        """
        self.frame.destroy()

    def initialize_view(self, course_id):
        """Luo näkymän kurssin tiedoista

        Args:
            course_id: näytettävän kurssin tunniste
        """
        self.course = self.course_service.get_course(course_id)
        tasks = TaskService().get_course_tasks(self.course.id)
        self.frame = ttk.Frame(master=self.root)
        self.frame.pack()
        back_button = ttk.Button(
            master=self.frame,
            text="Go back",
            command=self.show_index_view
        )
        back_button.pack(padx=5, pady=5)
        header = ttk.Label(
            self.frame,
            text=f"{self.course.name}, {self.course.credits} Cr",
        )
        header.pack(padx=10, pady=10)

        self.task_list = ttk.Treeview(
            master=self.frame,
            columns=("description", "deadline", "done"),
            show="headings",
            height=5
        )
        self.task_list.heading("description", text="Description")
        self.task_list.heading("deadline", text="Deadline")
        self.task_list.heading("done", text="Done")
        self.task_list.pack(padx=5, pady=5)
        
        for task in tasks:
            done = "False" if not task.done else "True"
            self.task_list.insert("", "end", iid=task.id, values=(task.content, task.deadline, done))
        self.task_list.bind("<<TreeviewSelect>>", self.handle_select)

        delete_button = ttk.Button(
            master=self.frame,
            text="Delete course",
            command=self.handle_delete
        )
        delete_button.pack(padx=5, pady=5)

    def handle_delete(self):
        """Poistaa kurssin
        """

        course_service = CourseService()
        course_service.delete_course(self.course.id)
        self.show_index_view()

    def handle_select(self, event):
        """Merkitsee valitun tehtävän tehdyksi

        Args:
            event: tapahtuma (ei käytetä)
        """
        task_service = TaskService()
        selected = self.task_list.selection()
        idx = selected[0]
        task_service.complete_task(idx)
        self.destroy()
        self.initialize_view(course_id=self.course.id)
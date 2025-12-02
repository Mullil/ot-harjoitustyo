from services.task_service import TaskService
from tkinter import ttk

class CourseView:
    def __init__(self, root, show_index_view):
        self.root = root
        self.frame = None
        self.show_index_view = show_index_view
    
    def destroy(self):
        self.frame.destroy()

    def initialize_view(self, course):
        tasks = TaskService().get_course_tasks(course.id)
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
            text=f"{course.name}, {course.credits} Cr",
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
            self.task_list.insert("", "end", values=(task.content, task.deadline, done))
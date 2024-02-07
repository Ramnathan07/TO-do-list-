import tkinter as tk
from tkinter import messagebox

class Todoapp(tk.Tk):
    def __init__(self):
        super().__init__()
        self.title("To-Do List App")
        self.geometry("400x300")

        self.tasks = []
        
        self.label_task = tk.Label(self, text="Task:")
        self.label_task.pack()

        self.input_field = tk.Entry(self)
        self.input_field.pack()

        self.add_button = tk.Button(self, text="Add Task", command=self.add_task)
        self.add_button.pack()

        self.delete_button = tk.Button(self, text="Delete Task", command=self.delete_task)
        self.delete_button.pack()
        self.delete_button['state'] = 'disabled'  # Initially disable delete button

        self.delete_all_button = tk.Button(self, text="Delete All Tasks", command=self.delete_all_tasks)
        self.delete_all_button.pack()

        self.task_list = tk.Listbox(self)
        self.task_list.pack()

        self.task_list.bind("<<ListboxSelect>>", self.task_selected)

    def add_task(self):
        task = self.input_field.get()
        if task:
            self.tasks.append(task)
            self.task_list.insert(tk.END, task)
            self.input_field.delete(0, tk.END)

    def delete_task(self):
        selected_index = self.task_list.curselection()
        if selected_index:
            selected_task = self.task_list.get(selected_index)
            self.tasks.remove(selected_task)
            self.task_list.delete(selected_index)
            self.delete_button['state'] = 'disabled'  # Disable the delete button after deleting the task

    def delete_all_tasks(self):
        self.tasks = []
        self.task_list.delete(0, tk.END)
        self.delete_button['state'] = 'disabled'  # Disable the delete button after deleting all tasks

    def task_selected(self, event):
        self.delete_button['state'] = 'normal'  # Enable the delete button when a task is selected


if __name__ == "__main__":
    app = Todoapp()
    app.mainloop()

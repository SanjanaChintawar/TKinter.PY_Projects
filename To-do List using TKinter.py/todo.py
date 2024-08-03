import tkinter as tk
from tkinter import filedialog, messagebox


class ToDoList(tk.Tk):
    def __init__(self):
        super().__init__()

        self.geometry("500x500")
        self.title("TO-DO List")

        self.create_gui()

    def create_gui(self):

        self.input_task = tk.Entry(self, width=30)
        self.input_task.pack(pady=20)

        self.add_button = tk.Button(text="Add Task", command=self.add_task, height=2)
        self.add_button.pack(pady=5)

        self.listbox = tk.Listbox(self, selectmode=tk.SINGLE,width=30)
        self.listbox.pack(pady=5)

        self.button_frame = tk.Frame(self)
        self.button_frame.pack(pady=5)

        self.edit_button = tk.Button(self.button_frame, text="Edit Task", command=self.edit_task,height=2)
        self.edit_button.grid(row=0, column=0, pady=5)

        self.delete_button = tk.Button(self.button_frame, text="Delete Task", command=self.delete_task,height=2)
        self.delete_button.grid(row=0, column=1, pady=5)

        self.done_button = tk.Button(self, text="Done", command=self.done_task,height=2)
        self.done_button.pack(pady=5)

        self.save_button = tk.Button(self, text="Save", command=self.save_task,height=2)
        self.save_button.pack(pady=5)

    def add_task(self):
        task = self.input_task.get()
        if task:
            self.listbox.insert(tk.END, task)
            self.input_task.delete(0, tk.END)

    def edit_task(self):
        task_index = self.listbox.curselection()
        if task_index:
            new_task = self.input_task.get()
            if new_task:
                self.listbox.delete(task_index)
                self.listbox.insert(task_index, new_task)
                self.input_task.delete(0, tk.END)

    def delete_task(self):
        task_index = self.listbox.curselection()
        if task_index:
            self.listbox.delete(task_index)

    def save_task(self):
        tasks= self.listbox.get(0, tk.END)
        file_path = filedialog.asksaveasfilename(defaultextension=".txt")
        if file_path:
            with open(file_path, 'w') as file:
                for task in tasks:
                    file.write(task + "\n")

    def done_task(self):
        task = self.listbox.curselection()
        if task:
            self.listbox.itemconfig(task, fg="green")

    def load_task(self):
        file_path = filedialog.askopenfilename(filetypes=[("Text files", "*.txt")])

        if file_path:
            with open(file_path, "r") as file:
                tasks = [line.strip() for line in file.readlines()]

                self.listbox.delete(0, tk.END)

                for task in tasks:
                    self.listbox.insert(tk.END, task)
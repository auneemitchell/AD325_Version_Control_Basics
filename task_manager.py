"""task_manager.py module provides the task manager class and functions."""

class TaskManager:
    """Class for the task manager functions."""

    def __init__(self):
        """Sets the task file name and loads the task."""
        self.task_file = 'tasks.txt'
        self.tasks = self.load_tasks()

    def load_tasks(self):
        """
        Tries to load the task file and returns a list
        consisting of each line in the file.
        """
        try:
            with open(self.task_file, 'r', encoding="utf-8") as file:
                return file.read().splitlines()
        except FileNotFoundError:
            return []

    def save_tasks(self):
        """Saves the tasks to the task file."""
        with open(self.task_file, 'w', encoding="utf-8") as file:
            for task in self.tasks:
                file.write(f"{task}\n")

    def add_task(self, task):
        """Adds the given task to the task list and saves it."""
        self.tasks.append(task)
        self.save_tasks()

    def view_tasks(self):
        """Displays the tasks in the task list."""
        for index, task in enumerate(self.tasks, start=1):
            print(f"Task {index}*** {task}")

    def delete_task(self, index):
        """Deletes the task at the specified index."""
        # Making sure index is in range
        if self.tasks:
            if 0 <= index < len(self.tasks):
                self.tasks.pop(index)
                self.save_tasks()
            else:
                print(f"Warning: provided task number {index + 1} does not exist.")
        else:
            print("Warning: no tasks found.")


    def complete_task(self, index):
        """Marks the task at the specified index as completed."""
        # Making sure index is in range
        if self.tasks:
            if 0 <= index < len(self.tasks):
                # Append " -- Complete" to end of task string at specified index
                self.tasks[index] += " - COMPLETED"
                self.save_tasks()
            else:
                print(f"Warning: provided task number {index + 1} does not exist.")
        else:
            print("Warning: no tasks found.")

 # for reversing the task list           
    def reverse_tasks(self):
        self.tasks.reverse()
        self.save_tasks()

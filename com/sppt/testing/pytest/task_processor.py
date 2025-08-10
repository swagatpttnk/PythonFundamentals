class TaskProcessor:
    def __init__(self):
        self._tasks = {}

    def process_task(self, task_name):
        if not isinstance(task_name, str) or not task_name.strip():
            raise ValueError("Task name cannot be empty.")
        if task_name in self._tasks and self._tasks[task_name]=="success":
            raise ValueError(f"Task '{task_name}' already processed.")
        else:
            self._tasks[task_name] = "success"
            return True

    def list_processed_tasks(self):
        return sorted(self._tasks)

    def get_processed_task_count(self):
        return len(self._tasks)

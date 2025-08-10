from com.sppt.testing.pytest.task_processor import TaskProcessor


class TaskManager:
    def __init__(self):
        self._tasks = []
        self._processed_tasks = []
        self._processor = TaskProcessor()

    def add_task(self, task_name):
        if not isinstance(task_name, str) or not task_name.strip():
            raise ValueError("Task name cannot be empty.")
        if task_name in self._tasks:
            raise ValueError(f"Task '{task_name}' already exists.")
        self._tasks.append(task_name)
        return True

    def remove_task(self, task_name):
        if task_name not in self._tasks:
            raise ValueError(f"Task '{task_name}' not found.")
        self._tasks.remove(task_name)
        return True

    def process_task(self, task_name):
        if task_name not in self._tasks:
            raise ValueError(f"Task '{task_name}' not found.")
        result = self._processor.process_task(task_name)
        if result == "success":
            self._processed_tasks.append(task_name)
            self._tasks.remove(task_name)
            return True
        else:
            return False

    def list_tasks(self):
        return sorted(self._tasks)

    def list_processed_tasks(self):
        return sorted(self._processed_tasks)
    def get_task_count(self):
        return len(self._tasks)
    def get_processed_task_count(self):
        return len(self._processed_tasks)
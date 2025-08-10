class CustomFileOpen:
    """Custom context manager for opening files."""

    def __init__(self, filename, mode):
        print(f'Inside CustomFileContextManager __init__ method')
        self.filename = filename
        self.mode = mode

    def __enter__(self):
        print(f'Inside CustomFileContextManager __enter__ method')
        self.f = open(self.filename, self.mode)
        return self.f

    def __exit__(self, *args):
        print(f'Inside CustomFileContextManager __exit__ method')
        self.f.close()


if __name__ == "__main__":
    with CustomFileOpen("file.txt", "wt") as f:
        f.write("contents go here")
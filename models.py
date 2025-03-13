class Task:
    def __init__(self, title, description, status="pending"):
        self.title = title
        self.description = description
        self.status = status

    def to_dict(self):
        return {
            "title": self.title,
            "description": self.description,
            "status": self.status
        }
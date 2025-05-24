init python:

    class Task:
        def __init__(self, title, description, priority, due_date, status):
            self.title = title
            self.priority = priority
            self.description = description
            self.due_date = due_date
            self.status = status

        def __eq__(self, other):
            return isinstance(other, Task) and (
                self.title == other.title and
                self.priority == other.priority and
                self.due_date == other.due_date
            )

        def __ne__(self, other):
            return not self.__eq__(other)
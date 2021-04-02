import os
import pickle
from datetime import date


class ToDoModel:
    def __init__(self, todo_id, name, description, due_date):
        self.todo_id = todo_id
        self.name = name
        self.description = description
        self.created_on = date.today()
        self.due_date = due_date
        self._is_done = False
        self._is_deleted = False

    def to_json(self):
        return {
            "name": self.name,
            "description": self.description,
            "created_on": self.created_on,
            "due_date": self.due_date,
            "is_done": self._is_done,
            "is_deleted": self._is_deleted,
        }

    def is_done(self):
        return self._is_done

    def mark_as_done(self):
        self._is_done = True

    def delete(self):
        self._is_deleted = True

    def is_deleted(self):
        return self._is_deleted


class ToDoDB:
    def __init__(self):
        self.todos = {}
        self.current_id = 0
        if os.path.isfile("db.pkl"):
            with open("db.pkl", "rb") as f:
                obj = pickle.load(f)
                self.todos = obj.todos
                self.current_id = obj.current_id

    def save(self):
        with open("db.pkl", "wb") as f:
            pickle.dump(self, f)

    def create(self, name, description=None, due_date=None):
        todo = ToDoModel(self.current_id, name, description, due_date)
        self.todos[self.current_id] = todo
        self.current_id += 1
        self.save()
        return todo

    def list(self):
        return [
            todo
            for todo in self.todos.values()
            if not todo.is_done() and not todo.is_deleted()
        ]

    def get_todo(self, todo_id):
        return self.todos[todo_id]

    def delete(self, todo_id):
        self.todos[todo_id].delete()
        self.save()
        return self.todos[todo_id]

    def update(self, todo_id, **kwargs):
        todo = self.todos[todo_id]

        for k, v in kwargs.items():
            todo.__dict__[k] = v
        self.save()
        return todo

from models import ToDoDB

ID_IS_REQUIRED = "ID is required"
INVALID_ID = "Invalid id"


class ToDoService:
    def __init__(self):
        self.db = ToDoDB()

    def create(self, params):
        return self.db.create(**params)

    def list(self):
        return self.db.list()

    def mark_as_done(self, params):
        try:
            todo_id = params["todo_id"]
        except KeyError:
            raise ToDoException(ID_IS_REQUIRED)

        try:
            todo = self.db.get_todo(todo_id)
        except KeyError:
            raise ToDoException(INVALID_ID)
        todo.mark_as_done()
        return todo

    def delete(self, params):
        try:
            todo_id = params["todo_id"]
        except KeyError:
            raise ToDoException(ID_IS_REQUIRED)

        try:
            todo = self.db.delete(todo_id)
        except KeyError:
            raise ToDoException(INVALID_ID)
        return todo

    def update(self, params):
        keys_param = ["name", "description", "due_date"]
        res_params = {}

        try:
            todo_id = params["todo_id"]
        except KeyError:
            raise ToDoException(ID_IS_REQUIRED)

        params.pop("todo_id")

        for k, v in params.items():
            if k in keys_param:
                res_params[k] = v
            else:
                raise ToDoException(f"Invalid argument: {k}")

        try:
            todo = self.db.update(todo_id, **res_params)
        except KeyError:
            raise ToDoException(INVALID_ID)

        return todo


class ToDoException(Exception):
    pass

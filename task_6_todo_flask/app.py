from flask import Flask, request

from service import ToDoException, ToDoService

app = Flask(__name__)
todo_service = ToDoService()


@app.route("/todo", methods=["POST"])
def create_todo():
    result = todo_service.create(request.get_json())
    return result.to_json()


@app.route("/todo_list", methods=["GET"])
def list_todo():
    result_list = todo_service.list()
    return {result.todo_id: result.to_json() for result in result_list}


@app.route("/todo_done", methods=["PUT"])
def todo_done():
    try:
        result = todo_service.mark_as_done(request.get_json())
    except ToDoException as e:
        return str(e), 400
    return result.to_json()


@app.route("/todo_delete", methods=["DELETE"])
def todo_delete():
    try:
        result = todo_service.delete(request.get_json())
    except ToDoException as e:
        return str(e), 400
    return result.to_json()


@app.route("/todo_update", methods=["PUT"])
def todo_update():
    try:
        result = todo_service.update(request.get_json())
    except ToDoException as e:
        return str(e), 400
    return result.to_json()


if __name__ == "__main__":
    app.run(debug=True)

from fastapi import FastAPI
from pydantic import BaseModel

app = FastAPI()

todos = []
# Pydantic Model for Todo item :
class Todo(BaseModel):
    id: int
    title: str
    completed: bool

# Create a new todo item :
@app.post("/todos")
def create_todo(todo: Todo):
    todos.append(todo)
    return {
    "message": "Todo created successfully", 
    "todo": todo
    }

# Get all todo items :
@app.get("/todos")
def get_todos():
   return todos

# Get a specific todo item by ID :
@app.get("/todos/{todo_id}")
def get_todo(todo_id: int):
    for todo in todos:
        if todo.id == todo_id:
            return todo
    return {"message": "Todo not found"}

# Update a specific todo item by ID :
@app.put("/todos/{todo_id}")
def update_todo(todo_id: int, updated_todo: Todo):
    for index, todo in enumerate(todos):
        if todo.id == todo_id:
            todos[index] = updated_todo
            return {
                "message": "Todo updated successfully", 
                "todo": updated_todo
            }
    return {"message": "Todo not found"}

# Delete a specific todo item by ID :
@app.delete("/todos/{todo_id}")
def delete_todo(todo_id: int):
    for index, todo in enumerate(todos):
        if todo.id == todo_id:
            todos.pop(index)
            return {"message": "Todo deleted successfully"}
    return {"message": "Todo not found"}
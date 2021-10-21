from model.model import Todo
from fastapi import FastAPI, HTTPException
from fastapi.middleware.cors import CORSMiddleware

from api.crud import fetch_todo, fetch_todos, create_todo, update_todo, remove_todo

origins = ["http://localhost:3000"]

app = FastAPI(
    title="Todo API - Demo Starter",
    description="A simple demo to show How FastAPI Interact with ReactJS & MongoDB",
    version="0.0.1",
)

# CORS
app.add_middleware(
    CORSMiddleware,
    allow_origins=origins,
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)


@app.get("/")
async def root():
    """
    Root route

    Returns:
        str: Welcome message
    """
    return {"message": "Hello World"}


@app.get("/api/todo")
async def list_todo():
    """
    List all todos

    Returns:
        [Todo] -- List of todos
    """
    response = await fetch_todos()
    return response


@app.get("/api/todo/{id}", response_model=Todo)
async def get_todo(id):
    """
    Get a todo by id

    Args:
        id (str): id of the todo

    Raises:
        HTTPException: 404 if todo not found

    Returns:
        Response: todo object
    """
    response = await fetch_todo(id)

    if response:
        return response
    raise HTTPException(404, f"there is no Todo with this id {id}")


@app.post("/api/todo")
async def post_todo(todo: Todo):
    """
    Create a todo

    Args:
        todo (Todo): todo object

    Raises:
        HTTPException: 400 if todo already exists

    Returns:
        Response: todo object
    """
    response = await create_todo(todo.__dict__)

    if response:
        return response
    raise HTTPException(400, "Bad request")


@app.put("/api/todo/{id}", response_model=Todo)
async def put_todo(id: str, description: str):
    """
    Update a todo

    Args:
        id (str): id of the todo
        description (str): new description of the todo

    Raises:
        HTTPException: 404 if todo not found

    Returns:
        Response: todo object
    """
    response = await update_todo(id, description)

    if response:
        return response
    raise HTTPException(400, "Bad request")


@app.delete("/api/todo/{id}")
async def delete_todo(id):
    """
    Delete a todo

    Args:
        id (str): id of the todo

    Raises:
        HTTPException: 404 if todo not found

    Returns:
        Response: todo object
    """
    response = await remove_todo(id)

    if response:
        return response
    raise HTTPException(400, "Bad request")

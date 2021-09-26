from fastapi import FastAPI, HTTPException
from fastapi.middleware.cors import CORSMiddleware
from model.model import Todo
from core.crud import (
    fetch_one_todo,
    fetch_all_todos,
    create_todo,
    update_todo,
    remove_todo
)

app = FastAPI(
    title="Farm Starter",
    description="Boilerplate code for quick docker implementation of FastAPI, ReactJS, MongoDB ✨",
    version="0.1.0",
)

origins = ["http://localhost:3000", "http://localhost:8080"]

app.add_middleware(
    CORSMiddleware,
    allow_origins=origins,
    allow_credentials=True,
    allow_methods=['*'],
    allow_headers=['*'],
)


@app.get('/')
def check_status():
    return {'Status': 'Ok'}


@app.get('/api/todo')
async def get_todo():
    response = await fetch_all_todos()
    return response


@app.get('/api/todo/{title}', response_model=Todo)
async def get_todo_by_id(title: str):
    response = await fetch_one_todo(title)
    if response:
        return response
    raise HTTPException(404, f'There is no todo item with this title {title}')


@app.post('/api/todo', response_model=Todo)
async def post_todo(todo: Todo):
    response = await create_todo(todo.dict())
    if response:
        return response
    raise HTTPException(400, 'Something went wrong/Bad Request')


@app.put('/api/todo/{title}', response_model=Todo)
async def put_todo(title: str, desc: str):
    response = await update_todo(title, desc)
    if response:
        return response
    raise HTTPException(404, f'There is no todo item with this title {title}')


@app.delete('/api/todo/{title}')
async def delete_todo(title: str):
    response = await remove_todo(title)
    if response:
        return 'Successfully deleted todo item!'
    raise HTTPException(404, f'There is no todo item with this title {title}')

from contextlib import asynccontextmanager
import os

from fastapi import FastAPI, status
from motor.motor_asyncio import AsyncIOMotorClient
from pydantic import BaseModel
from dal import ToDoDAL, ListSummary, ToDoList


COLLECTION_NAME = 'todo_lists'
MONGODB_URI = os.environ['MONGODB_URI']
DEBUG = os.environ.get('DEBUG', '').strip().lower() in {'1', 'true', 'on' 'yes'}

@asynccontextmanager
async def lifespan(app: FastAPI):
    client = AsyncIOMotorClient(MONGODB_URI)
    database = client.get_default_database()
    pong = await database.command('ping')
    if int(pong['ok']) != 1:
        raise Exception('Cluster connection is not okay!')
    todo_lists = database.get_collection(COLLECTION_NAME)
    app.todo_dal = ToDoDAL(todo_lists)
    yield
    client.close()

app = FastAPI(lifespan=lifespan, debug=DEBUG)

@app.get('/api/lists')
async def get_all_lists() -> list[ListSummary]:
    return [i async for i in app.todo_dal.list_todo_lists()]

class NewList(BaseModel):
    name: str
class NewListResponse(BaseModel):
    id: str
    name: str

@app.post('/api/lists', status_code=status.HTTP_201_CREATED)
async def create_todo_list(new_list: NewList) -> NewListResponse:
    return NewListResponse(
        id=await app.todo_dal.create_todo_list(new_list.name),
        name=new_list.name,
    )

@app.get('/api/lists/{list_id}')
async def get_lists(list_id: str) -> ToDoList:
    return await app.todo_dal.get_todo_list(list_id)

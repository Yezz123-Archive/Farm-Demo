import motor.motor_asyncio
from decouple import config

client = motor.motor_asyncio.AsyncIOMotorClient(config("MONGODB_URI"))

db = client.TodoList
collection = db.todo

from bson import ObjectId
from core.database import collection


async def fetch_todo(id):
    """
    Fetch a single todo by id

    Args:
        _id (str): The id of the todo to fetch

    Returns:
        dict: The todo document
    """
    document = await collection.find_one({"_id": ObjectId(id)})
    return {
        "id": str(document["_id"]),
        "title": document["title"],
        "description": document["description"],
    }


async def fetch_todos():
    """
    Fetch all todos

    Returns:
        list: A list of todo documents
    """
    todos = []
    cursor = collection.find({})
    async for document in cursor:
        todos.append(
            {
                "id": str(document["_id"]),
                "title": document["title"],
                "description": document["description"],
            }
        )

    return todos


async def create_todo(todo):
    """
    Create a new todo

    Args:
        todo (dict): The todo to create

    Returns:
        dict: The created todo document
    """
    document = todo
    result = await collection.insert_one(document)

    return {
        "id": str(document["_id"]),
        "title": document["title"],
        "description": document["description"],
    }


async def update_todo(id, title, description):
    """
    Update a todo

    Args:
        id (str): The id of the todo to update
        title (str): The new title of the todo
        description (str): The new description of the todo

    Returns:
        dict: The updated todo document
    """
    await collection.update_one(
        {
            "_id": ObjectId(id),
        },
        {"$set": {"title": title, "description": description}},
    )

    document = await collection.find_one({"_id": ObjectId(id)})

    return document


async def remove_todo(id):
    """
    Remove a todo

    Args:
        id (str): The id of the todo to remove

    Returns:
        dict: The removed todo document
    """
    collection.delete_one({"_id": ObjectId(id)})
    return {"status": "ok"}

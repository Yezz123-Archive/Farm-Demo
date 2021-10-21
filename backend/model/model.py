from pydantic import BaseModel


class Todo(BaseModel):
    """
    Todo model

    Args:
        BaseModel (pydantic.BaseModel): Base model for pydantic
    """

    title: str
    description: str

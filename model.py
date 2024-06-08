from pydantic import BaseModel

class Todo(BaseModel):
    id: int
    item1: str
    item2: str
    timestamp:str
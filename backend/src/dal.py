from bson import ObjectId
from motor.motor_asyncio import AsyncIOMotorCollection
from pymongo import ReturnDocument
from pydantic import BaseModel
from uuid import uuid4

class ListSummary(BaseModel):
    id: str
    name: str
    item_count: int
    @staticmethod
    def from_doc(doc) -> 'ListSummary':
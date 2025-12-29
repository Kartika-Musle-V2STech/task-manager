from pydantic import BaseModel, ConfigDict

class TaskTypeOut(BaseModel):
    """Schema returned in API responses when task types are fetched or listed"""
    id: int
    name: str

    model_config = ConfigDict(from_attributes=True)
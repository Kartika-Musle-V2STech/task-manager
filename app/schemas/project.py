from pydantic import BaseModel, ConfigDict
from datetime import date

class ProjectCreate(BaseModel):
    """
    Schema used when creating a new project
    """
    project_template_id: int
    start_date: date
    end_date: date | None = None
    created_by_id: int
    
class UserBasicInfo(BaseModel):
    """
    Basic user information for nested display
    """
    id: int
    name: str
    email: str
    
    model_config = ConfigDict(from_attributes=True)
    
class ProjectTemplateBasicInfo(BaseModel):
    """
    Basic project template information
    """
    id: int
    name: str
    description: str
    
    model_config = ConfigDict(from_attributes=True)
    
class ProjectOut(BaseModel):
    """
    Schema returned in API responses when a project is fetched or created
    """
    project_template_id: int
    start_date: date
    end_date: date | None
    created_by_id: int
    
    created_by: UserBasicInfo
    project_template: ProjectTemplateBasicInfo
    
    model_config = ConfigDict(from_attributes=True)
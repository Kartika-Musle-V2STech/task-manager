from pydantic import BaseModel, ConfigDict

class ProjectTemplateBase(BaseModel):
    """
    Base schema containing fields common to all project template schemas
    """
    name: str
    description: str | None = None

class ProjectTemplateCreate(ProjectTemplateBase):
    """
    Schema used when creating a new project template
    """
    pass

class ProjectTemplateOut(ProjectTemplateBase):
    """
    Schema returned in API responses when a project template is fetched or listed
    """
    id: int

    model_config = ConfigDict(from_attributes = True)
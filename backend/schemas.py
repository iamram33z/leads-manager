# Import Libraries
import datetime as _dt
import pydantic as _pydantic

# Class for User Base Model
class _UserBase(_pydantic.BaseModel):
    email: str

# Class for User Create Schema
class UserCreate(_UserBase):
    hashed_password: str

    class Config:
        orm_mode = True

# Class for User Schema
class User(_UserBase):
    id: int

    class Config:
        orm_mode = True

# Class for Lead Base Model
class _LeadBase(_pydantic.BaseModel):
    first_name: str
    last_name: str
    email: str
    company: str = ""
    note: str = ""

# Class for Lead Create Schema
class LeadCreate(_LeadBase):
    pass

# Class for Lead Schema
class Lead(_LeadBase):
    id: int
    owner_id: int
    created_at: _dt.datetime
    updated_at: _dt.datetime

    class Config:
        orm_mode = True
from typing import List, Optional
from pydantic import BaseModel, Field


class TaskBase(BaseModel):
    category: str
    title: str
    description: str
    state: bool
    url: str


class TaskIn(TaskBase):
    flag: str


class Task(TaskBase):
    class Config:
        orm_mode = True


class ItemBase(BaseModel):
    title: str
    description: Optional[str] = None


class ItemCreate(ItemBase):
    pass


class Item(ItemBase):
    id: int
    owner_id: int

    class Config:
        orm_mode = True


class UserBase(BaseModel):
    email: str = Field(..., min_length=5)


class UserCreate(UserBase):
    password: str = Field(..., min_length=8)


class User(UserBase):
    id: int
    is_active: bool
    items: List[Item] = []
    tasks: List[Task] = []

    class Config:
        orm_mode = True


class Token(BaseModel):
    access_token: str
    token_type: str


class TokenData(BaseModel):
    username: Optional[str] = None


class Status(BaseModel):
    message: str

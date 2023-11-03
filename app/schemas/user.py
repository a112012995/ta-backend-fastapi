from typing import Optional

from pydantic import BaseModel


# Shared properties
class UserBase(BaseModel):
    username: str
    is_super: bool = False
    puskesmas_id: Optional[int] = None


# Properties to receive via API on creation
class UserCreate(UserBase):
    username: str
    password: str
    is_super: bool = False
    puskesmas_id: Optional[int] = None


# Properties to receive via API on update
class UserUpdate(UserBase):
    password: Optional[str] = None


class UserInDBBase(UserBase):
    id: Optional[int] = None

    class Config:
        orm_mode = True


class User(UserInDBBase):
    pass


class UserInDB(UserInDBBase):
    hashed_password: str

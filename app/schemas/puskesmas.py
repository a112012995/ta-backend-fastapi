from typing import Optional

from pydantic import BaseModel


# Shared properties
class PuskesmasBase(BaseModel):
    name: str


# Properties to receive via API on creation
class PuskesmasCreate(PuskesmasBase):
    name: str


# Properties to receive via API on update
class PuskesmasUpdate(PuskesmasBase):
    pass


class PuskesmasInDBBase(PuskesmasBase):
    id: Optional[int] = None

    class Config:
        from_attributes = True


class Puskesmas(PuskesmasInDBBase):
    pass


class PuskesmasInDB(PuskesmasInDBBase):
    pass

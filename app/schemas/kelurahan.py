from typing import Optional

from pydantic import BaseModel


# Shared properties
class KelurahanBase(BaseModel):
    name: str
    kecamatan_id: int
    puskesmas_id: int


# Properties to receive via API on creation
class KelurahanCreate(KelurahanBase):
    name: str
    kecamatan_id: int
    puskesmas_id: int


# Properties to receive via API on update
class KelurahanUpdate(KelurahanBase):
    pass


class KelurahanInDBBase(KelurahanBase):
    id: Optional[int] = None

    class Config:
        from_attributes = True


class Kelurahan(KelurahanInDBBase):
    pass


class KelurahanInDB(KelurahanInDBBase):
    pass

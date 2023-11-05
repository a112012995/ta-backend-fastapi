from typing import Optional

from pydantic import BaseModel


# Shared properties
class KecamatanBase(BaseModel):
    name: str


# Properties to receive via API on creation
class KecamatanCreate(KecamatanBase):
    name: str


# Properties to receive via API on update
class KecamatanUpdate(KecamatanBase):
    pass


class KecamatanInDBBase(KecamatanBase):
    id: Optional[int] = None

    class Config:
        from_attributes = True


class Kecamatan(KecamatanInDBBase):
    pass


class KecamatanInDB(KecamatanInDBBase):
    pass

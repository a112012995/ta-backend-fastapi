from typing import Optional

from pydantic import BaseModel


# Shared properties
class PatientsBase(BaseModel):
    age: int
    gender: str
    addr_kota: str
    addr_kecamatan: str
    kecamatan_id: int
    addr_kelurahan: str
    kelurahan_id: int


# Properties to receive via API on creation
class PatientsCreate(PatientsBase):
    age: int
    gender: str
    addr_kota: str
    addr_kecamatan: str
    kecamatan_id: int
    addr_kelurahan: str
    kelurahan_id: int


# Properties to receive via API on update
class PatientsUpdate(PatientsBase):
    age: int
    gender: str
    addr_kota: str
    addr_kecamatan: str
    kecamatan_id: int
    addr_kelurahan: str
    kelurahan_id: int


class PatientsInDBBase(PatientsBase):
    id: Optional[int] = None

    class Config:
        from_attributes = True


class Patients(PatientsInDBBase):
    pass


class PatientsInDB(PatientsInDBBase):
    pass

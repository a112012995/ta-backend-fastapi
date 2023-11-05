from typing import Optional

from pydantic import BaseModel


# Shared properties
class TB_CasesBase(BaseModel):
    puskesmas_id: int
    patients_id: int
    diagnosis: str
    anatomy: str
    is_new: str
    is_dm: str
    is_hiv: str
    treatment_status: str
    created_at: str
    updated_at: str


# Properties to receive via API on creation
class TB_CasesCreate(TB_CasesBase):
    puskesmas_id: int
    patients_id: int
    diagnosis: str
    anatomy: str
    is_new: str
    is_dm: str
    is_hiv: str
    treatment_status: str
    created_at: str
    updated_at: str


# Properties to receive via API on update
class TB_CasesUpdate(TB_CasesBase):
    puskesmas_id: int
    patients_id: int
    diagnosis: str
    anatomy: str
    is_new: str
    is_dm: str
    is_hiv: str
    treatment_status: str
    created_at: str
    updated_at: str


class TB_CasesInDBBase(TB_CasesBase):
    id: Optional[int] = None

    class Config:
        from_attributes = True


class TB_Cases(TB_CasesInDBBase):
    pass


class TB_CasesInDB(TB_CasesInDBBase):
    pass

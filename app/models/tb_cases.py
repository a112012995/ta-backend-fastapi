from typing import TYPE_CHECKING

from sqlalchemy import Column, Integer, String, Boolean, Date, ForeignKey

from app.db.base_class import Base


if TYPE_CHECKING:
    from .puskesmas import Puskesmas
    from .patients import Patients


class TB_Cases(Base):
    id = Column(Integer, primary_key=True, index=True)
    puskesmas_id = Column(Integer, ForeignKey("puskesmas.id"))
    patients_id = Column(Integer, ForeignKey("patients.id"))
    diagnosis = Column(String(255), index=True, nullable=False)
    anatomy = Column(String(255), index=True, nullable=False)
    is_new = Column(Boolean, index=True, nullable=False)
    is_dm = Column(Boolean, index=True, nullable=False)
    is_hiv = Column(Boolean, index=True, nullable=False)
    treatment_status = Column(String(255), index=True, nullable=False)
    created_at = Column(Date, index=True, nullable=False)
    updated_at = Column(Date, index=True, nullable=False)

from typing import TYPE_CHECKING

from sqlalchemy import Column, Integer, String, ForeignKey

from app.db.base_class import Base


if TYPE_CHECKING:
    from .kecamatan import Kecamatan
    from .kelurahan import Kelurahan


class Patients(Base):
    id = Column(Integer, primary_key=True, index=True)
    age = Column(Integer, index=True, nullable=False)
    gender = Column(String(255), index=True, nullable=False)
    addr_kota = Column(String(255), index=True, nullable=False)
    addr_kecamatan = Column(String(255), index=True, nullable=False)
    kecamatan_id = Column(Integer, ForeignKey("kecamatan.id"))
    addr_kelurahan = Column(String(255), index=True, nullable=False)
    kelurahan_id = Column(Integer, ForeignKey("kelurahan.id"))

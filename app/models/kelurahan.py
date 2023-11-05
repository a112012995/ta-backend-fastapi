from typing import TYPE_CHECKING

from sqlalchemy import Column, Integer, String, ForeignKey

from app.db.base_class import Base


if TYPE_CHECKING:
    from .kecamatan import Kecamatan
    from .puskesmas import Puskesmas


class Kelurahan(Base):
    id = Column(Integer, primary_key=True, index=True)
    name = Column(String(255), unique=True, index=True, nullable=False)
    kecamatan_id = Column(Integer, ForeignKey("kecamatan.id"))
    puskesmas_id = Column(Integer, ForeignKey("puskesmas.id"))

from typing import TYPE_CHECKING

from sqlalchemy import Column, Integer, String, Boolean, ForeignKey
from sqlalchemy.orm import relationship

from app.db.base_class import Base

if TYPE_CHECKING:
    from .puskesmas import Puskesmas


class User(Base):
    id = Column(Integer, primary_key=True, index=True)
    username = Column(String(255), unique=True, index=True, nullable=False)
    hashed_password = Column(String(255), nullable=False)
    is_super = Column(Boolean, default=False)
    # puskesmas_id = Column(Integer, ForeignKey("puskesmas.id"))
    # puskesmas = relationship("Puskesmas", back_populates="workers")

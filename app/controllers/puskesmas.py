from typing import Any, Dict, Optional, Union

from sqlalchemy.orm import Session

from app.controllers.base import ControllerBase
from app.models.puskesmas import Puskesmas
from app.schemas.puskesmas import PuskesmasCreate, PuskesmasUpdate


class ControllerPuskesmas(ControllerBase[Puskesmas, PuskesmasCreate, PuskesmasUpdate]):
    def get_by_name(self, db: Session, *, name: str) -> Optional[Puskesmas]:
        return db.query(Puskesmas).filter(Puskesmas.name == name).first()

    def create(self, db: Session, *, obj_in: PuskesmasCreate) -> Puskesmas:
        db_obj = Puskesmas(
            name=obj_in.name,
        )
        db.add(db_obj)
        db.commit()
        db.refresh(db_obj)
        return db_obj

    def update(
        self, db: Session, *, db_obj: Puskesmas, obj_in: Union[PuskesmasUpdate, Dict[str, Any]]
    ) -> Puskesmas:
        if isinstance(obj_in, dict):
            update_data = obj_in
        else:
            update_data = obj_in.dict(exclude_unset=True)

        return super().update(db, db_obj=db_obj, obj_in=update_data)


puskesmas = ControllerPuskesmas(Puskesmas)

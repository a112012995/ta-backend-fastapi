from typing import Any, Dict, Optional, Union

from sqlalchemy.orm import Session

from app.controllers.base import ControllerBase
from app.models.kecamatan import Kecamatan
from app.schemas.kecamatan import KecamatanCreate, KecamatanUpdate


class ControllerKecamatan(ControllerBase[Kecamatan, KecamatanCreate, KecamatanUpdate]):
    def get_by_name(self, db: Session, *, name: str) -> Optional[Kecamatan]:
        return db.query(Kecamatan).filter(Kecamatan.name == name).first()

    def create(self, db: Session, *, obj_in: KecamatanCreate) -> Kecamatan:
        db_obj = Kecamatan(
            name=obj_in.name,
        )
        db.add(db_obj)
        db.commit()
        db.refresh(db_obj)
        return db_obj

    def update(
        self, db: Session, *, db_obj: Kecamatan, obj_in: Union[KecamatanUpdate, Dict[str, Any]]
    ) -> Kecamatan:
        if isinstance(obj_in, dict):
            update_data = obj_in
        else:
            update_data = obj_in.dict(exclude_unset=True)

        return super().update(db, db_obj=db_obj, obj_in=update_data)


kecamatan = ControllerKecamatan(Kecamatan)

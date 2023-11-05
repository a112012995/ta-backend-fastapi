from typing import Any, List

from fastapi import APIRouter, Body, Depends, HTTPException
from fastapi.encoders import jsonable_encoder
from sqlalchemy.orm import Session

from app import controllers, models, schemas
from app.api import dependencies as deps
from app.core.config import settings

router = APIRouter()


@router.get("/kecamatan", response_model=List[schemas.Kecamatan])
def read_kecamatan(
    db: Session = Depends(deps.get_db),
    skip: int = 0,
    limit: int = 100,
    current_user: models.User = Depends(deps.get_current_active_superuser),
) -> Any:
    """
    Retrieve kecamatan.
    """
    kecamatan = controllers.kecamatan.get_multi(db, skip=skip, limit=limit)
    return kecamatan


@router.get("/kecamatan/{kecamatan_id}", response_model=schemas.Kecamatan)
def read_kecamatan_by_id(
    kecamatan_id: int,
    db: Session = Depends(deps.get_db),
    current_user: models.User = Depends(deps.get_current_active_superuser),
) -> Any:
    """
    Get kecamatan by id.
    """
    kecamatan = controllers.kecamatan.get(db, id=kecamatan_id)
    if not kecamatan:
        raise HTTPException(
            status_code=404, detail="The kecamatan doesn't exists"
        )
    return kecamatan

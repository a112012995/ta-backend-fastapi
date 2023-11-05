from typing import Any, List

from fastapi import APIRouter, Body, Depends, HTTPException
from fastapi.encoders import jsonable_encoder
from sqlalchemy.orm import Session

from app import controllers, models, schemas
from app.api import dependencies as deps
from app.core.config import settings

router = APIRouter()


@router.get("/puskesmas", response_model=List[schemas.Puskesmas])
def read_puskesmas(
    db: Session = Depends(deps.get_db),
    skip: int = 0,
    limit: int = 100,
    current_user: models.User = Depends(deps.get_current_active_superuser),
) -> Any:
    """
    Retrieve puskesmas.
    """
    puskesmas = controllers.puskesmas.get_multi(db, skip=skip, limit=limit)
    return puskesmas


@router.get("/puskesmas/{puskesmas_id}", response_model=schemas.Puskesmas)
def read_puskesmas_by_id(
    puskesmas_id: int,
    db: Session = Depends(deps.get_db),
    current_user: models.User = Depends(deps.get_current_active_superuser),
) -> Any:
    """
    Get puskesmas by id.
    """
    puskesmas = controllers.puskesmas.get(db, id=puskesmas_id)
    if not puskesmas:
        raise HTTPException(
            status_code=404, detail="The puskesmas doesn't exists"
        )
    return puskesmas

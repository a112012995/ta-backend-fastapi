from sqlalchemy.orm import Session

from app import controllers, schemas
from app.core.config import settings
from app.db import base


def init_db(db: Session) -> None:

    user = controllers.user.get_by_username(
        db, username=settings.FIRST_SUPERUSER)
    if not user:
        user_in = schemas.UserCreate(
            username=settings.FIRST_SUPERUSER,
            password=settings.FIRST_SUPERUSER_PASSWORD,
            is_super=True,
            puskesmas_id=settings.FIRST_SUPERUSER_PUSKESMAS_ID,
        )
        user = controllers.user.create(db, obj_in=user_in)

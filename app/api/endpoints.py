from fastapi import APIRouter

from app.api.routers import login, users, puskesmas, kecamatan

api_router = APIRouter()

api_router.include_router(login.router, tags=["Login"])
api_router.include_router(users.router, tags=["Users"])
api_router.include_router(puskesmas.router, tags=["Puskesmas"])
api_router.include_router(kecamatan.router, tags=["Kecamatan"])
# api_router.include_router(prediction.router, tags=["forecast"])
# api_router.include_router(vulnerability.router, tags=["vulnerability"])
# api_router.include_router(intervention.router, tags=["intervention"])

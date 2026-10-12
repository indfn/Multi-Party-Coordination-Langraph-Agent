"""Mocks package — exposes consolidated mock routers."""

from app.mocks.routers.tos_ppt import router as tos_ppt_router
from app.mocks.routers.tos_tuas import router as tos_tuas_router
from app.mocks.routers.truck_system import router as truck_system_router
from app.mocks.routers.feeder import router as feeder_router
from app.mocks.routers.pcs import router as pcs_router

__all__ = [
    "tos_ppt_router",
    "tos_tuas_router",
    "truck_system_router",
    "feeder_router",
    "pcs_router",
]

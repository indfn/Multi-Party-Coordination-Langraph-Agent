"""Truck Management System — Road ITT Capacity endpoint (Tool 2)."""

from fastapi import APIRouter
from app.mocks.data import get_truck_data

router = APIRouter(prefix="/api/truck_system", tags=["Truck Management System"])


@router.get("/capacity")
async def check_road_itt_capacity():
    """Query Truck Management System for available trucks, transit time, and road conditions."""
    return get_truck_data()

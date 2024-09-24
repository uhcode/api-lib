from fastapi import APIRouter
from typing import Optional


from .current import *
from .historical import *
from .forecast import *


weather_route = APIRouter(
    prefix="/weather",
    tags=["Weather & Locational Resources"],
)

@weather_route.get("/current/{location}")
async def current_weather(
    api_key: str,
    location: str,
    units: Optional[str] = None,
    language: Optional[str] = None,
    callback: Optional[str] = None,
    ):
    """
    Get the current weather at a location.
    """

    data = await current(api_key, location, units, language, callback)
    return data

@weather_route.get("/historical/{location}")
async def historical_weather(
    api_key: str,
    location: str,
    date_start: str,
    date_end: str,
    hourly: Optional[str] = None,
    interval: Optional[str] = None,
    units: Optional[str] = None,
    language: Optional[str] = None,
    callback: Optional[str] = None
    ):
    """
    Get the historical weather at a location.
    """

    data = await historical(api_key, location, date_start, date_end, hourly, interval, units, language, callback)
    return data
    
@weather_route.get("/forecast/{location}")
async def forecast_weather(
        api_key: str,
        location: str,
        days: Optional[str] = None,
        hourly: Optional[str] = None,
        interval: Optional[str] = None,
        units: Optional[str] = None,
        language: Optional[str] = None,
        callback: Optional[str] = None
    ):
    """
    Get the forecasted weather at a location.
    """

    data = await forecast(api_key, location, days, hourly, interval, units , language, callback)
    return data
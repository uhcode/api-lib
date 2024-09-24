import aiohttp
from typing import Optional

async def historical(
        api_key: str,
        location: str,
        date_start: str,
        date_end: str,
        hourly: Optional[str],
        interval: Optional[str],
        units: Optional[str],
        language: Optional[str],
        callback: Optional[str],
    ):
    """
    View the historical weather at a location.

    You can get an API key at https://weatherstack.com.
    """

    if not api_key:
        return {"error": "API Key is missing."}

    params = {
        "query": str(location.lower()),
        "access_key": api_key,
        "historical_date_start": date_start,
        "historical_date_end": date_end,
    }

    if hourly:
        params.update({"hourly": hourly})
    elif interval:
        params.update({"interval": interval})
    elif units:
        params.update({"units": units})
    elif language:
        params.update({"language": language})
    elif callback:
        params.update({"callback": callback})

    async with aiohttp.ClientSession() as session:
        async with session.get(
            "http://api.weatherstack.com/historical",
            params=params
        ) as response:
            data = await response.json()
            if "request_failed" in data:
                return {"error": "You've likely entered a location that doesn't exist."}
            return data
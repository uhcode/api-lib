import aiohttp
from typing import Optional

async def current(
        api_key: str,
        location: str,
        units: Optional[str],
        language: Optional[str],
        callback: Optional[str],
    ):
    """
    View the current weather at a location.

    You can get an API key at https://weatherstack.com.
    """

    if not api_key:
        return {"error": "API Key is missing."}
    
    params = {
        "query": str(location.lower()),
        "access_key": api_key,
    }

    if units:
        params.update({"units": units})
    elif language:
        params.update({"language": language})
    elif callback:
        params.update({"callback": callback})

    async with aiohttp.ClientSession() as session:
        async with session.get(
            "http://api.weatherstack.com/current",
            params=params
        ) as response:
            data = await response.json()
            if "request_failed" in data:
                return {"error": "You've likely entered a location that doesn't exist."}
            return data
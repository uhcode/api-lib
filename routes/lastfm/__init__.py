import aiohttp
from typing import Optional, Union

from fastapi import APIRouter

from .track import *

# Initialize the LastFM API route.
lastfm_route = APIRouter(
    prefix="/lastfm",
    tags=["LastFM Statistics"],
)


@lastfm_route.get("/status")
async def status():
    """
    View the status of the Last.fm API.

    This will return a JSON response if the API is online or offline.

    You do not need any authentication to use this endpoint.
    """

    async with aiohttp.ClientSession() as session:
        async with session.get(
            "http://ws.audioscrobbler.com/2.0/",
        ) as response:
            data = response.url.host # Returns the host of the URL.
            if data:
                return {"status": "Online"} # Return a JSON response if the API is online or offline.
            return {"status": "Offline"}
        
@lastfm_route.get("/track")
async def get_track(
        mbid: str = None,
        track: str = None,
        artist: str = None,
        username: str = None,
        autocorrect: int = None,
        api_key: str = None,
    ):
    """
    Get a track's information from the popular site Last.fm.

    Get an API key at https://www.last.fm/api/account/create.
    """

    if not api_key:
        return {"error": "API Key is missing."}
    
    data = await lastfm_track(
        mbid=mbid,
        track=track,
        artist=artist,
        username=username,
        autocorrect=autocorrect,
        api_key=api_key,
    )
    return data

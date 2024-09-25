import aiohttp
from typing import Optional, Union


async def lastfm_track(
        mbid: Optional[str],
        track: Union[Optional[str], str],
        artist: Union[Optional[str], str],
        username: Optional[str],
        autocorrect: Optional[int],
        api_key: str,
    ):
    """
    Get a track's information from the popular site Last.fm.

    Get an API key at https://www.last.fm/api/account/create.
    """

    # Checks if the API key is missing.
    if not api_key:
        return {"error": "API Key is missing."}
    
    params = {
        "method": "track.getInfo",
        "api_key": api_key,
        "track": track,
        "artist": artist,
        "format": "json",
    }

    if mbid:
        params.update({"mbid": mbid}) # This is uncommon, but it's here just in case someone has one (they will not need to search author or track name).
    elif username:
        params.update({"username": username})
    elif autocorrect:
        if autocorrect == 1:
            params.update({"autocorrect": 1})
        elif autocorrect == 0:
            params.update({"autocorrect": 0})
        else:
            return {"error": "Autocorrect must be either 1 or 0."}

    async with aiohttp.ClientSession() as session:
        async with session.get(
            "http://ws.audioscrobbler.com/2.0/",
            params=params
        ) as response:
            data = await response.json()
            if "error" in data:
                return {"error": "You've likely entered a track or artist that doesn't exist."} # REturn an error if the track or artist doesn't exist.
            return data
        
    async def get_track_artist(
        mbid: Optional[str],
        track: str,
        artist: str,
        username: Optional[str],
        autocorrect: Optional[int],
        api_key: str,
    ):
        """
        Get a track's information from the popular site Last.fm.

        Get an API key at https://www.last.fm/api/account/create.
        """

        data = await lastfm_track(
            mbid=mbid,
            track=track,
            artist=artist,
            username=username,
            autocorrect=autocorrect,
            api_key=api_key,
        )

        return data['track']['artist']['name']
    
    async def get_track_album(
        mbid: Optional[str],
        track: str,
        artist: str,
        username: Optional[str],
        autocorrect: Optional[int],
        api_key: str,
    ):
        """
        Get a track's information from the popular site Last.fm.

        Get an API key at https://www.last.fm/api/account/create.
        """

        data = await lastfm_track(
            mbid=mbid,
            track=track,
            artist=artist,
            username=username,
            autocorrect=autocorrect,
            api_key=api_key,
        )

        return data['track']['album']['title']

    async def get_track_duration(
        mbid: Optional[str],
        track: str,
        artist: str,
        username: Optional[str],
        autocorrect: Optional[int],
        api_key: str,
    ):
        """
        Get a track's information from the popular site Last.fm.

        Get an API key at https://www.last.fm/api/account/create.
        """

        data = await lastfm_track(
            mbid=mbid,
            track=track,
            artist=artist,
            username=username,
            autocorrect=autocorrect,
            api_key=api_key,
        )

        return data['track']['duration']
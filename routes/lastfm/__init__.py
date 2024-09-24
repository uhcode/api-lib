from fastapi import APIRouter

lastfm_route = APIRouter(
    prefix="/lastfm",
    tags=["LastFM Statistics"],
)
from fastapi import APIRouter

spotify_route = APIRouter(
    prefix="/spotify",
    tags=["Spotify Statistics"],
)

@spotify_route.get("/status")
async def status():
    return {"status": "Online"}
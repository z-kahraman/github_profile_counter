from fastapi import FastAPI, Request
from fastapi.responses import Response
from utils import increment_view_count
from svg_generator import generate_svg_badge

app = FastAPI()

@app.get("/badge")
async def badge(request: Request, page_id: str):
    view_count = increment_view_count(page_id)
    svg_content = generate_svg_badge(page_id, view_count)
    return Response(content=svg_content, media_type="image/svg+xml")


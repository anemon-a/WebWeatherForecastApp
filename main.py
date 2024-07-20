from fastapi import FastAPI, Request, HTTPException
from fastapi.responses import HTMLResponse, RedirectResponse
from fastapi.staticfiles import StaticFiles
from fastapi.templating import Jinja2Templates
from jinja2 import Environment
from api.geocode import get_coordinates
from api.weather import get_weather_forecast, weather_icons

app = FastAPI()
app.mount("/static", StaticFiles(directory="static"), name="static")
templates = Jinja2Templates(directory="templates")


@app.get("/", response_class=HTMLResponse)
async def home(request: Request):
    return templates.TemplateResponse("index.html", {"request": request})


@app.get("/weather", response_class=HTMLResponse)
async def get_weather(request: Request, city: str = None):
    coordinates = await get_coordinates(city)
    if not coordinates:
        # raise HTTPException(status_code=404, detail="Location not found")
        return RedirectResponse(url="/")
    weather = await get_weather_forecast(
        coordinates["latitude"], coordinates["longitude"]
    )

    return templates.TemplateResponse(
        "forecast.html",
        {
            "request": request,
            "city": city,
            "weather": weather,
            "weather_icons": weather_icons,
        },
    )

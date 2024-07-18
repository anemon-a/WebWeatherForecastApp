from fastapi import FastAPI, Request
from fastapi.responses import HTMLResponse
from fastapi.staticfiles import StaticFiles
from fastapi.templating import Jinja2Templates
from geopy.adapters import AioHTTPAdapter
from geopy.geocoders import Nominatim
import httpx

app = FastAPI()
app.mount("/static", StaticFiles(directory="static"), name="static")
templates = Jinja2Templates(directory="templates")


# @app.get("/", response_class=HTMLResponse)
# async def home(request: Request):
#     return templates.TemplateResponse("base.html", {"request": request})
url = "https://api.open-meteo.com/v1/forecast"


@app.get("/weather", response_class=HTMLResponse)
async def get_weather(city: str):
    async with httpx.AsyncClient() as client:
        params = {"latitude": 40.7143, "longitude": -74.006, "hourly": "temperature_2m"}
        response = await client.get()
        weather_data = response.json()
        return {"city": city, "weather": weather_data}

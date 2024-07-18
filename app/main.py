from fastapi import FastAPI, Request
from fastapi.responses import HTMLResponse, RedirectResponse
from fastapi.staticfiles import StaticFiles
from fastapi.templating import Jinja2Templates
from geopy.adapters import AioHTTPAdapter
from geopy.geocoders import Nominatim
import httpx

app = FastAPI()
# app.mount("/static", StaticFiles(directory="static"), name="static")
templates = Jinja2Templates(directory="templates")

@app.get("/", response_class=HTMLResponse)
async def home(request: Request):
    return templates.TemplateResponse("base.html", {"request": request})

@app.get("/weather")
async def get_weather(city: str = None):
    # Здесь вы можете добавить логику для получения широты и долготы из строки поиска с использованием вашего метода или API геокодирования
    async with Nominatim(user_agent="WebWeatherForecastApp", adapter_factory=AioHTTPAdapter,) as geolocator:
        location = await geolocator.geocode(city)
        if location:
            latitude = location.latitude
            longitude = location.longitude

            url = f"https://api.open-meteo.com/v1/forecast?latitude={latitude}&longitude={longitude}&hourly=temperature_2m"
            async with httpx.AsyncClient() as client:
                    response = await client.get(url)
                    return {"city": city, "weather": response.json()}
        else:
            # return {"error": "Геоданные не найдены для указанного города"}
            return RedirectResponse(url="/")

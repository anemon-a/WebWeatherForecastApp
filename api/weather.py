import httpx
from datetime import datetime
from pydantic import BaseModel

WEATHER_API_URL = "https://api.open-meteo.com/v1/forecast"


class WeatherDataOutput(BaseModel):
    time: str
    temperature_2m: float
    relative_humidity_2m: int
    weather_code: int
    wind_speed_10m: float


weather_icons = {
    0: [
        "Солнечно",
        "sun.png",
    ],
    1: ["Облачно", "cloudy.png"],
    2: ["Облачно", "cloudy.png"],
    3: ["Пасмурно", "overcast.png"],
    45: ["Туман", "fog.png"],
    48: ["Туман", "fog.png"],
    51: ["Дождь", "rainy.png"],
    53: ["Дождь", "rainy.png"],
    55: ["Дождь", "rainy.png"],
    56: ["Дождь", "rainy.png"],
    57: ["Дождь", "rainy.png"],
    61: ["Дождь", "rainy.png"],
    63: ["Дождь", "rainy.png"],
    65: ["Дождь", "rainy.png"],
    66: ["Дождь", "rainy.png"],
    67: ["Дождь", "rainy.png"],
    71: ["Снег", "snowy.png"],
    73: ["Снег", "snowy.png"],
    75: ["Снег", "snowy.png"],
    77: ["Снег", "snowy.png"],
    80: ["Ливень", "shower.png"],
    81: ["Ливень", "shower.png"],
    82: ["Ливень", "shower.png"],
    85: ["Дождь со снегом", "rain_snow.png"],
    86: ["Дождь со снегом", "rain_snow.png"],
    95: ["Гроза", "storm.png"],
    96: ["Град", "hail.png"],
    99: ["Град", "hail.png"],
}


async def get_weather_forecast(latitude: float, longitude: float):
    params = {
        "latitude": latitude,
        "longitude": longitude,
        "hourly": "temperature_2m,relative_humidity_2m,weather_code,wind_speed_10m",
    }
    async with httpx.AsyncClient() as client:
        response = await client.get(WEATHER_API_URL, params=params)
        if response:
            return await transform_data(response.json()["hourly"])
        return None


async def transform_data(weather_data: dict):
    transformed_data = {}

    for i in range(len(weather_data["time"])):
        date_key = weather_data["time"][i][:10]
        date_key = datetime.strptime(date_key, "%Y-%m-%d")
        date_key = date_key.strftime("%d %B, %A")

        if date_key not in transformed_data:
            transformed_data[date_key] = []

        transformed_data[date_key].append(
            WeatherDataOutput(
                time=weather_data["time"][i][11:],
                weather_code=weather_data["weather_code"][i],
                temperature_2m=weather_data["temperature_2m"][i],
                relative_humidity_2m=weather_data["relative_humidity_2m"][i],
                wind_speed_10m=weather_data["wind_speed_10m"][i],
            )
        )
    return transformed_data

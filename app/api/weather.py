import httpx
import datetime
from pydantic import BaseModel

WEATHER_API_URL = "https://api.open-meteo.com/v1/forecast"


class WeatherDataOutput(BaseModel):
    time: str
    temperature_2m: float
    relative_humidity_2m: int
    weather_code: int
    wind_speed_10m: float


async def get_weather_forecast(latitude: float, longitude: float):
    # url = f"latitude=55.0415&longitude=82.9346&hourly=temperature_2m,relative_humidity_2m,weather_code,wind_speed_10m&timezone=GMT"
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
    print(weather_data)
    for i in range(len(weather_data["time"])):
        date_key = weather_data["time"][i][:10]  # Extract the date part (YYYY-MM-DD)
        if date_key not in transformed_data:
            transformed_data[date_key] = []

        transformed_data[date_key].append(
            WeatherDataOutput(
                time=weather_data["time"][i][11:],
                temperature_2m=weather_data["temperature_2m"][i],
                relative_humidity_2m=weather_data["relative_humidity_2m"][i],
                weather_code=weather_data["weather_code"][i],
                wind_speed_10m=weather_data["wind_speed_10m"][i],
            )
        )
    return transformed_data

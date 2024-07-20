import ssl
import certifi
from geopy.adapters import AioHTTPAdapter
from geopy.geocoders import Nominatim

ctx = ssl.create_default_context(cafile=certifi.where())


async def get_coordinates(city: str) -> dict:
    async with Nominatim(
        user_agent="WebWeatherForecastApp",
        adapter_factory=AioHTTPAdapter,
        ssl_context=ctx,
    ) as geolocator:
        location = await geolocator.geocode(city)
        if location:
            return {"latitude": location.latitude, "longitude": location.longitude}
        return None

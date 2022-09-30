import http

import dateutil
import dateutil.parser
import datetime
import NOAA_v1.Utils as Utils


class NOAAPeriod:
    def __init__(self, response, index: int = 0):
        period = response["properties"]["periods"][index]
        self.number: int = period["number"]
        self.name: str = period["name"]
        self.start_time: datetime = dateutil.parser.parse(period["startTime"])
        self.end_time: datetime = dateutil.parser.parse(period["endTime"])
        self.is_daytime: bool = period["isDaytime"]
        self.temperature: float = period["temperature"]
        self.temperature_unit: str = period["temperatureUnit"]
        self.temperature_trend: str = period["temperatureTrend"]
        self.wind_speed: str = period["windSpeed"]
        self.wind_direction: str = period["windDirection"]
        self.icon_url: http = period["icon"]
        self.icon = None
        if self.icon_url is not None:
            self.icon = Utils.get_icon_from_url(self.icon_url)
        self.short_forecast: str = period["shortForecast"]
        self.detailed_forecast: str = period["detailedForecast"]

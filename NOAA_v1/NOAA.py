# Provides access to the NOAA api ("national weather service", NWS).
# This is for obtaining current conditions and forecasts, not historical data.

from logging import exception

import requests
from requests.exceptions import HTTPError
import json

from NOAA_v1 import Utils


class NOAA:
    class_headers = {"User-Agent": "(python_weather_demo, johnstraub1954@gmail.com)"}

    def __init__(
            self,
            lat: float = None,
            lon: float = None,
            grid_id: str = None,
            grid_x: int = None,
            grid_y: int = None,
            station_id: str = None,
            office_id: str = None
    ):
        self.lat = lat
        self.lon = lon
        self.grid_id = grid_id
        self.grid_x = grid_x
        self.grid_y = grid_y
        self.station_id = station_id
        self.office_id = office_id

        self.units = None

        self.latest_response = None
        self.latest_error = None
        self.latest_url = None

    def get_glossary(self):
        url = "https://api.weather.gov/glossary/"
        response = self.__api_call(url, headers=self.class_headers)
        return response

    def get_latest_for_station(self, station_id):
        url = f"https://api.weather.gov/stations/{station_id}/observations/latest"
        parameters = None
        response = self.__api_call(url, headers=self.class_headers)
        return response

    def get_forecast(
            self,
            grid_id: str = None,
            grid_x: int = None,
            grid_y: int = None,
            hourly: bool = False
    ):
        if grid_id is None:
            grid_id = self.grid_id
        if grid_x is None:
            grid_x = self.grid_x
        if grid_y is None:
            grid_y = self.grid_y
        if grid_id is None or grid_x is None or grid_y is None:
            message = "invalid grid coordinates for forecast (" \
                      + f"(gridID={grid_id}, gridX={grid_x}, gridY={grid_y}" \
                      + "/forecast"
            raise exception(message)
        parameters = None
        if self.units is not None:
            parameters = {"units": self.units}
        url = "https://api.weather.gov/gridpoints/" \
              + f"{grid_id}/{grid_x},{grid_y}/forecast/"
        if hourly:
            url += "hourly/"
        response = self.__api_call(url, headers=self.class_headers, parameters=parameters)
        return response

    def get_station(self, station_id):
        url = f"https://api.weather.gov/stations/{station_id}"
        response = self.__api_call(url, headers=self.class_headers)
        return response

    def get_stations(self, grid_id=None, grid_x=None, grid_y=None):
        if grid_id is None:
            grid_id = self.grid_id
        if grid_x is None:
            grid_x = self.grid_x
        if grid_y is None:
            grid_y = self.grid_y
        if grid_id is None or grid_x is None or grid_y is None:
            message = "invalid grid coordinates for forecast (" \
                      + f"(gridID={grid_id}, gridX={grid_x}, gridY={grid_y}" \
                      + "/forecast"
            raise exception(message)
        url = "https://api.weather.gov/gridpoints/" \
              + f"{grid_id}/{grid_x},{grid_y}/stations"
        response = self.__api_call(url, headers=self.class_headers)
        return response

    def get_office(self, oid):
        url = f"https://api.weather.gov/offices/{oid}"
        response = self.__api_call(url, headers=self.class_headers)
        return response

    def get_grid_points(
            self,
            lat=None,
            lon=None,
            headers=class_headers
    ):
        if lat is None:
            lat = self.lat
        if lon is None:
            lon = self.lon
        if lat is None or lon is None:
            message = f"invalid latitude ({lat}) and/or longitude ({lon})"
            raise exception(message)
        url = f"https://api.weather.gov/points/{lat},{lon}"
        response = self.__api_call(url, headers=self.class_headers)
        if response is not None:
            props = response["properties"]
            self.grid_id = props["gridId"]
            self.grid_x = props["gridX"]
            self.grid_y = props["gridY"]
        return response

    def __api_call(self, url, headers=class_headers, parameters=None):
        print("__api_call/url: " + str(url))
        result = Utils.api_call(url, headers, parameters)
        self.latest_response = result[0]
        self.latest_error = result[1]

        return self.latest_response

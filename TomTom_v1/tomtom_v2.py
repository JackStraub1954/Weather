# https://api.tomtom.com/search/2/structuredGeocode.json?key=oQhlHO7xGCxugtxM5fTbqtXhHJxtpm0z&countryCode=US&postalCode=98045&
# https://api.tomtom.com/search/2/structuredGeocode.json?key=oQhlHO7xGCxugtxM5fTbqtXhHJxtpm0z&municipality=North Bend&countrySubdivision=WA
# https://api.tomtom.com/search/2/search/36.98844,-121.97483.json?key=oQhlHO7xGCxugtxM5fTbqtXhHJxtpm0z
# https://api.tomtom.com/search/2/poiSearch/36.98844,-121.97483.json?key=oQhlHO7xGCxugtxM5fTbqtXhHJxtpm0z
import requests
from requests.exceptions import HTTPError
import json


class TomTom:
    base_url = "https://api.tomtom.com/search/"
    api_key = "key=oQhlHO7xGCxugtxM5fTbqtXhHJxtpm0z"
    version = "2/"
    format = ".json"

    search_endpoint = "search/"
    geocode_endpoint = "structuredGeocode.json?"

    def __init__(
            self,
            lat: float = None,
            lon: float = None,
            city: str = None,
            country: str = None,
            country_sub: str = None,
            postal_code: str = None,
            street_number: str = None,
            street: str = None,
            country_set: str = None,
            poi: str = None
    ):
        self.lat = lat
        self.lon = lon
        self.city = city
        self.country = country
        self.country_sub = country_sub
        self.postal_code = postal_code
        self.street_number = street_number
        self.street = street
        self.country_set = country_set
        self.poi = poi

        self.response = None

    def search_by_region(self):
        url = TomTom.base_url + TomTom.version + TomTom.geocode_endpoint + TomTom.api_key
        params = dict()
        if self.city is not None:
            # url += "&municipality=" + self.city
            params["municipality"] = self.city
        if self.street_number is not None:
            #url += "&streetNumber=" + self.street_number
            params["streetNumber"] = self.street_number
        if self.street is not None:
            # url += "&streetName=" + self.street
            params["streetName"] = self.street
        if self.country is not None:
            # url += "&countryCode=" + self.country
            params["countryCode"] = self.country
        if self.country_sub is not None:
            # url += "&countrySubdivision=" + self.country_sub
            params["countrySubdivision"] = self.country_sub
        if self.postal_code is not None:
            # url += "&postalCode=" + self.postal_code
            params["postalCode"] = self.postal.code
        print("?????")
        print(url)
        api_response = self.__api_call(url, params=params)

        tom_tom_result = None
        if api_response is not None:
            result0 = api_response["results"][0]
            print(result0)
        return api_response

    def __api_call(self, url, headers=None, params=None):
        decoded_response = None
        try:
            response = requests.get(url, headers=headers, params=params)
            print(";;;;;")
            print(response.url)
            response.raise_for_status()
            if response.status_code == 200:
                decoded_response = json.loads(response.content.decode('utf-8'))
            else:
                return None
        except HTTPError as http_err:
            print(f'HTTP error occurred: {http_err}')
        except Exception as err:
            print(f'Other error occurred: {err}')

        return decoded_response



class TomTomResult:

    def __init__(
            self,
            lat: float = None,
            lon: float = None,
            city: str = None,
            country: str = None,
            country_sub: str = None,
            postal_code: str = None
    ):
        self.lat = lat
        self.lon = lon
        self.city = city
        self.country = country
        self.country_sub = country_sub
        self.postal_code = postal_code

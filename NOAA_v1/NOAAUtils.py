import http
import json

import PIL.Image
import io
import requests
from requests import HTTPError


def api_call(url, headers=None, parameters=None) -> list:
    print("api_call/initial url: " + str(url))
    decoded_response = None
    last_error = None
    try:
        response = requests.get(url, headers=headers, params=parameters)
        if response is not None:
            working_url = response.url
            print(f"api_call/formatted url: {working_url}")
        response.raise_for_status()

        if response.status_code == 200:
            decoded_response = json.loads(response.content.decode('utf-8'))

    except HTTPError as http_err:
        print(f'HTTP error occurred: {http_err}')
        last_error = http_err
    except Exception as err:
        print(f'Other error occurred: {err}')
        last_error = err

    ret_val = [decoded_response, last_error]
    return ret_val


def get_icon_from_url(url: str) -> http:
    icon = None
    try:
        response = requests.get(url)
        bitmap = io.BytesIO(response.content)
        icon = PIL.Image.open(bitmap)
    except Exception as exc:
        message = f'Error loading image {url}, {exc}'
        print(message)
    return icon

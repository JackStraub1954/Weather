import http
import PIL.Image
import io
import requests


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

from NOAA_v1.NOAA import NOAA
from NOAA_v1.NOAAForecastResponse import NoaaForecastResponse
from NOAA_v1.NOAAPeriod import NOAAPeriod
from datetime import datetime
import traceback


def print_indent(text: str, level: int = 1):
    indent = ""
    times = level
    while times > 0:
        indent += def_indent
        times -= 1
    print(indent + text)


# number of spaces to indent by, when indent required
def_indent = "    "


def format_time(dtime: datetime) -> str:
    f_time: str = dtime.strftime("%b %d, %Y  %I:%M:%S%p")
    return f_time


noaaObj = NOAA(lat=47.44840789954482, lon=-121.77699967729914)
try:
    response = noaaObj.get_grid_points()
    if response is None:
        raise Exception("no response from get_grid_points")
    response = noaaObj.get_forecast(hourly=False)
    fc_response = NoaaForecastResponse(response)
    coords = fc_response.coordinates(0)
    pstr = f'latitude: {coords["lat"]}'
    print(pstr)
    pstr = f'longitude: {coords["lon"]}'
    print(pstr)
    num_periods = fc_response.get_num_periods()
    print(f"num periods: {num_periods}")
    num_periods = min(24, num_periods)
    for inx in range(0, num_periods):
        period = NOAAPeriod(response, inx)
        name = period.name
        if name is None or not name:
            name = "NONE"
        print_indent(f'period: {period.number}, (name: {name})', 0)
        ftime = format_time(period.start_time)
        print_indent(f"start time: {ftime}", 1)
        ftime = format_time(period.end_time)
        print_indent(f"end time: {ftime}", 1)
        print_indent(f"daytime: {period.is_daytime}")
        print_indent(f"temperature: {period.temperature}")
        print_indent(f"temperature unit: {period.temperature_unit}")
        print_indent(f"wind speed: {period.wind_speed}")
        print_indent(f"wind direction: {period.wind_direction}")
        print_indent(period.icon_url, 1)
        if period.icon is not None:
            pass # period1.icon.show()
        print_indent(f"short forecast: {period.short_forecast}")
        print_indent(f"detailed forecast: {period.detailed_forecast}")
        print(period.detailed_forecast)

except Exception as exc:
    message = f"Error: {exc}"
    print(message)
    print(noaaObj.latest_error)
    traceback.print_exc()


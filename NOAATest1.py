from NOAA_v1 import NOAA

noaaObj = NOAA.NOAA(lat=47.4957, lon=-121.7868)
noaaObj.get_grid_points()
if noaaObj.latest_response is not None:
    message = f"id={noaaObj.grid_id},gridX={noaaObj.grid_x},gridY={noaaObj.grid_y}"
    print(message)
else:
    print(noaaObj.latest_error)

print("######## STATIONS ########")
response = noaaObj.get_stations()
if response is not None:
    print(">>> " + str(response))
else:
    print(">>> " + str(noaaObj.latest_error))

print("######## OFFICE ID ########")
response = noaaObj.get_office("SEW")
if response is not None:
    print(">>> " + str(response))
    print(">>> " + str(response["address"]))
else:
    print(">>> " + str(noaaObj.latest_error))

print("######## FORECAST ########")
response = noaaObj.get_forecast("SEW")
if response is not None:
    print(">>> " + str(response))
else:
    print(">>> " + str(noaaObj.latest_error))

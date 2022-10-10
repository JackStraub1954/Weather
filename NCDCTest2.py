import traceback

import Utils
from NOAA_v1.Datasets import NCDC
import traceback

ncdc = NCDC()
try:
    params = {'startdate': '2022-03-01', 'enddate': '2022-03-15', "locationid": "ZIP:98045"}
    response = ncdc.get_data('GHCND', parameters=params)
    if response is None:
        raise Exception("no response from get_data")
    print(response)
    Utils.print_formatted(response)
    # for x in response["results"]:
    #     print(x)

#    uid = response["results"][0]["id"]
#    response = ncdc.get_dataset(uid)
#    if response is None:
#        raise Exception("no response from get_dataset")
#    print(response)

except Exception as exc:
    message = f"Error: {exc}"
    print(message)
    print(ncdc.latest_error)
    traceback.print_exc()

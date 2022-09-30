import traceback

from NOAA_v1.Datasets import NCDC
import traceback

ncdc = NCDC()
try:
    response = ncdc.get_all_datasets()
    if response is None:
        raise Exception("no response from get_all_datasets")
    print(response["results"])
    for x in response["results"]:
        print(x)

    uid = response["results"][0]["id"]
    response = ncdc.get_dataset(uid)
    if response is None:
        raise Exception("no response from get_dataset")
    print(response)

except Exception as exc:
    message = f"Error: {exc}"
    print(message)
    print(ncdc.latest_error)
    traceback.print_exc()

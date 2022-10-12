from NOAA_v1.Datasets import NCDC
import Utils

ncdc = NCDC()
uid = "GSOM"
params = {\
    'startdate': '2022-04-01',\
    'enddate': '2022-06-01',\
    "locationid": "ZIP:98045"
}
try:
    result = ncdc.get_data(uid, parameters=params)
    Utils.print_formatted(result)
except Exception as exc:
    msg = "error calling get-dataset uid = GSOM: " + str(exc)

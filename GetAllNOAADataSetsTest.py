from NOAA_v1.Datasets import NCDC
import Utils

ncdc = NCDC()
try:
    result = ncdc.get_all_datasets()
    Utils.print_formatted(result)
except Exception as exc:
    msg = "get_all_datasets failed: " + str(exc)
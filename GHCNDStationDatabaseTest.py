from NOAA_v1.GHCNDStationDatabase import GHCNDStationDatabase
from NOAA_v1.GHCNDStationDatabase import GHCNDStationData


try:
    ghcnd_dbase = GHCNDStationDatabase()
#    first: str = GHCNDStationDatabase.database[0]
#    end = len(first) - 1
#    print(first)
#    print(">>" + first[end] + "<<")
#    print(">>" + first[end - 1] + "<<")
#    print(">>" + first[end - 2] + "<<")

    rec1 = GHCNDStationData(122045)
    print(122045)
    print(rec1)
    print(1)
    print(GHCNDStationData(1))
except Exception as err:
    print("error reading station database")
    print(err)

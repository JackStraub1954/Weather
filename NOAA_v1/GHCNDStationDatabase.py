from urllib.error import HTTPError, URLError
from urllib.request import urlopen


def print_station_rec(num: int = 0):
    print(GHCNDStationDatabase.database[num])


class GHCNDStationDatabase:
    # class variables
    databaseURL = "https://www1.ncdc.noaa.gov/pub/data/ghcn/daily/ghcnd-stations.txt"
    database: list = None
    http_error: HTTPError = None
    url_error: URLError = None

    def __init__(self):
        # global database
        if GHCNDStationDatabase.database is None:
            try:
                text = urlopen(GHCNDStationDatabase.databaseURL)
                GHCNDStationDatabase.database = list()
                for line in text:
                    line = str(line)
                    line_len = len(line)
                    line = line[2:line_len - 3]
                    GHCNDStationDatabase.database.append(line)
                    print(line)
                db_len = len(GHCNDStationDatabase.database)
                print(f'len={db_len}')
            except HTTPError as http_err:
                print(http_err)
                self.http_error = http_err
                raise(Exception("http error"))
            except URLError as url_err:
                print(url_err)
                self.url_error = url_err
                raise(Exception("url error"))


class GHCNDStationData:
    def __init__(self, num: int = -1):
        if GHCNDStationDatabase.database is None:
            GHCNDStationDatabase()
        if num < 0 or num >= len(GHCNDStationDatabase.database):
            msg = f'index ({num}) out of bounds'
            raise(Exception(msg))
        line: str = GHCNDStationDatabase.database[num]
        line_len = len(line)
        if line_len != 85:
            msg = f'record {num}: unexpected length ({line_len})'
            raise(Exception(msg))
        self.station_id = line[0:11]
        self.lat = line[12:20]
        self.lon = line[21:30]
        self.elevation = line[31:37]
        self.state = line[38:40]
        self.station_name = line[41:71]
        self.eh2 = line[72:80]
        self.eh3 = line[81:]

    def __str__(self) -> str:
        result = f'id=[{self.station_id}] '\
            + f'lat=[{self.lat}] '\
            + f'lon=[{self.lon}] '\
            + f'elevation=[{self.eh1}] '\
            + f'state=[{self.state}] '\
            + f'name=[{self.station_name}] '\
            + f'eh2=[{self.eh2}] '\
            + f'eh3=[{self.eh3}] '
        return result

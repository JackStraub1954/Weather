class NoaaForecastResponse:
    def __init__(self, json_response):
        self.response = json_response

    def coordinates(self, index: int = 0):
        if index > 4:
            message = f"Invalid index({index})"
            raise Exception(message)
        coords = self.response["geometry"]["coordinates"][0][index]
        lat = float(coords[1])
        lon = float(coords[0])
        result = {"lat": lat, "lon": lon}
        return result

    def get_num_periods(self) -> int:
        num_periods: int = len(self.response["properties"]["periods"])
        return num_periods

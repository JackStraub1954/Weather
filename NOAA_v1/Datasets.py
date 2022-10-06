from NOAA_v1 import Utils


class NCDC:
    ncdc_token: str = "kzjLcRPtaGGxirvbdPRCvFOMFIxzIXHa"
    ncdc_dataset_base_url: str = "https://www.ncei.noaa.gov/cdo-web/api/v2/datasets/"
    ncdc_data_base_url: str = "https://www.ncei.noaa.gov/cdo-web/api/v2/data"
    ncdc_headers = {"token": ncdc_token}

    def __int__(self):
        self.latest_response = None
        self.latest_error = None

    def get_all_datasets(self) -> object:
        response = self.__api_call(NCDC.ncdc_dataset_base_url)
        return response

    def get_dataset(self, uid: str, parameters: dict = dict()) -> object:
        url = NCDC.ncdc_dataset_base_url
        parameters['datasetid'] = uid
        response = self.__api_call(url, parameters=parameters)
        return response

    def get_data(self, uid: str, parameters: dict = dict()) -> object:
        url = NCDC.ncdc_data_base_url
        parameters['datasetid'] = uid
        response = self.__api_call(url, parameters=parameters)
        return response

    def __api_call(self, url, headers=None, parameters=None):
        if headers is None:
            headers = NCDC.ncdc_headers
        print("NCDC __api_call/url: " + str(url))
        result = Utils.api_call(url, headers, parameters)
        self.latest_response = result[0]
        self.latest_error = result[1]

        return self.latest_response

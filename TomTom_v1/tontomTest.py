# https://api.tomtom.com/search/2/structuredGeocode.json?key=oQhlHO7xGCxugtxM5fTbqtXhHJxtpm0z&municipality=North+Bend&streetNumber=16811&streetName=423rd+place+SE&countryCode=US&countrySubdivision=WA
from tomtom_v2 import TomTom


tomtom = TomTom(street_number="16811", street="423rd place SE", city="North Bend", country_sub="WA", country="US")
result = tomtom.search_by_region()
print("*********************")
print(result)
print(result["results"][0])

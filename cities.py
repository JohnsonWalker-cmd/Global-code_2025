from geopy.geocoders import Nominatim
from geopy.distance import geodesic

geolocator = Nominatim(user_agent="city_distance_calulator")

def city_distance_calculator():
  city1_name = input("Enter the name of city 1: ")
  city2_name = input("Enter the name of city 2: ")
  
  location_1 = geolocator.geocode(city1_name)
  location_2 = geolocator.geocode(city2_name)
  
  if location_1 and location_2:
    cords1 = (location_1.latitude , location_1.longitude)
    cords2 = (location_2.latitude , location_2.longitude)
  else:
    print("Could not find cities")
    exit()
    
  distance = geodesic(cords1 , cords2).km
  print(f"The distance between {city1_name} and {city2_name}  is {distance:.2f} km.")
  
city_distance_calculator()
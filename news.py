import requests

from datetime import date

TODAY = date.today()

NEWS_API_KEY = "1e8216bfdf904886a6aeed4dbe98c098"

BASE_URL = "https://newsapi.org/v2/everything"

params = {
  "q" : "Apple",
  "from" : TODAY,
  "sortBy" : "popularity",
  "apikey" : NEWS_API_KEY
}

response = requests.get(BASE_URL , params=params)

if response.status_code == 200:
  print("Request successful")
  
  
else:
  print(f"Request failed with status code: {response.status_code}")
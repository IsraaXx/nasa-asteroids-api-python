import requests
import os
from dotenv import load_dotenv
from datetime import date

class Asteroid:
    def __init__(self, name, diameter, close_approach_date, is_hazardous):
        self.name = name
        self.diameter = diameter
        self.close_approach_date = close_approach_date
        self.is_hazardous = is_hazardous

load_dotenv()

api_key = os.getenv("NASA_API_KEY")


today = date.today().isoformat()    # YYYY-MM-DD

url ="https://api.nasa.gov/neo/rest/v1/feed"

params = {
    "api_key": api_key,
    "start_date": today,
    "end_date": today
}

response = requests.get(url, params = params)

if response.status_code == 200:
    print("Request sent successfully")
    
    data = response.json()
    asteroids = data["near_earth_objects"][today]
    asteroid_objects = []
    for asteroid in asteroids:
        name = asteroid["name"]
        diameter = asteroid["estimated_diameter"]["kilometers"]["estimated_diameter_max"]
        close_approach_date = asteroid["close_approach_data"][0]["close_approach_date"]
        is_hazardous = asteroid["is_potentially_hazardous_asteroid"]
        asteroid_obj = Asteroid(name, diameter, close_approach_date, is_hazardous)
        asteroid_objects.append(asteroid_obj)

    for asteroid in asteroid_objects:
        print(f"Name: {asteroid.name}")
        print(f"Diameter (km): {asteroid.diameter}")
        print(f"Close Approach Date: {asteroid.close_approach_date}")
        print(f"Potentially Hazardous: {asteroid.is_hazardous}")
        print("-" * 40)
    
else:
    print("Request failed. Status code:", response.status_code)    


    
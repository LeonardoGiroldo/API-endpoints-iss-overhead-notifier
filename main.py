import requests
from datetime import datetime

#Defining my current location
MY_LAT = 39.585676 
MY_LNG = 2.679648 


def is_iss_overhead():
    '''
    this function gives the current latitude and longitude of the ISS satelite
    '''
    response = requests.get(url = "http://api.open-notify.org/iss-now.json")
    response.raise_for_status()
    data = response.json()

    iss_longitude = float(data['iss_position']['longitude'])
    iss_latitude = float(data['iss_position']['latitude'])

    if MY_LAT-5 <= iss_latitude <= MY_LAT +5 and MY_LNG-5 <= iss_latitude <= MY_LNG +5:
        return True


def is_night():
    '''
    This function tells us if it is night time
    '''
    parameters = {
        "lat" : MY_LAT,
        "lng" : MY_LNG,
        "formatted" : 0
    }
    response = requests.get("https://api.sunrise-sunset.org/json", params= parameters, verify = False)
    response.raise_for_status()
    data = response.json()
    sunrise = int(data['results']['sunrise'].split("T")[1].split(":")[0])
    sunset = int(data['results']['sunset'].split("T")[1].split(":")[0])

    time_now = datetime.now().hour

    if time_now >= sunset or time_now <= sunrise:
        return True

#If the ISS satelite is over our location so it will print Look UP
if is_iss_overhead() and is_night():
    print("Look up!!!!")

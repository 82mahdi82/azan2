import requests

def get_prayer_times(country, city):
    base_url = "https://api.aladhan.com/v1/timingsByCity"
    
    params = {
        "city": city,
        "country": country,
        "method": 5 
    }

    response = requests.get(base_url, params=params)

    if response.status_code == 200:
        data = response.json()
        prayer_times = data["data"]["timings"]
        return prayer_times
    
    else:
        return None
    

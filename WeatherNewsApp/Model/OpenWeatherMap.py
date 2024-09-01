import requests
import json

class OpenWeatherMap:
    API_KEY_JSON="WeatherNewsApp/api_key.json"
    GET_WEATHER_INFO_URL="http://api.openweathermap.org/data/2.5/weather"
    
    def _get_weather_info(city_name):
        with open(OpenWeatherMap.API_KEY_JSON, "r") as reader:
            api_key_json = reader.read()
        
        api_key = json.loads(api_key_json)["api_key"]
        params = {
            "q": city_name,
            "appid": api_key,
            "units": "metric",  # 温度を摂氏で取得する
            "lang": "ja"  # 日本語での天気情報を取得する
        }
        
        weather_info_response = requests.get(OpenWeatherMap.GET_WEATHER_INFO_URL, params=params)
        
        if weather_info_response.status_code == 200:
            data = weather_info_response.json()
            print(data)
            return data
        else:
            print("weather response is failed.")
            return None

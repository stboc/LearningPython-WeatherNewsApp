class WeatherData:
    def __init__(self, json_data):
        self.weather = json_data["weather"][0]["description"]
        self.temperature = json_data["main"]["temp"]
        self.humidity = json_data["main"]["humidity"]

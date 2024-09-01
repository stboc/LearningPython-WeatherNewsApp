import tkinter as tk
import WeatherNewsApp.Model.OpenWeatherMap as weather
import WeatherNewsApp.Model.WeatherData as wd

class WeatherView(tk.Frame):
    def __init__(self, parent, *args, **kwargs):
        super().__init__(parent, *args, **kwargs)
        
        self._main_frame = tk.Frame(self, relief="groove",bd=2, padx=5, pady=5)
        self._main_frame.pack()
        
        self._main_label = tk.Label(self._main_frame, text="CurrentWeathersInfo")
        self._main_label.pack()
        
        self._humidity_frame = tk.Frame(self._main_frame)
        self._humidity_frame.pack()
        self._humidity_lable = tk.Label(self._humidity_frame, text="湿度: ")
        self._humidity_lable.pack(side="left")
        self._humidity_data = tk.Label(self._humidity_frame, text="データなし")
        self._humidity_data.pack(side="left")

        self._temperature_frame = tk.Frame(self._main_frame)
        self._temperature_frame.pack()
        self._temperature_label = tk.Label(self._temperature_frame, text="温度: ")
        self._temperature_label.pack(side="left")
        self._temperature_data = tk.Label(self._temperature_frame, text="データなし")
        self._temperature_data.pack(side="left")
        
        self._weather_frame = tk.Frame(self._main_frame)
        self._weather_frame.pack()
        self._weather_label = tk.Label(self._main_frame, text="天気: ")
        self._weather_label.pack(side="left")
        self._weather_data = tk.Label(self._main_frame, text="データなし")
        self._weather_data.pack(side="left")

    def update_weather_info(self, city:str):
        self._main_label.config(text=city)
        weather_info = weather.OpenWeatherMap._get_weather_info(city)
        weather_data = wd.WeatherData(weather_info)
        print(f"Weather: {weather_data.weather}")
        self._weather_data.config(text=weather_data.weather)
        
        print(f"Temperature: {weather_data.temperature}")
        self._temperature_data.config(text=weather_data.temperature)
        
        print(f"Humidity: {weather_data.humidity}")
        self._humidity_data.config(text=weather_data.humidity)


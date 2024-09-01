import WeatherNewsApp.Controller.MainController as mc
import WeatherNewsApp.View.WeatherView as wv
import tkinter as tk

class MainView(tk.Tk):
    def __init__(self, mainController:mc.MainController):
        super().__init__()
        self._mainController = mainController
        
        self.title("Weather News App")
        self.geometry("300x400")
        
        self._weatherView = wv.WeatherView(self)
        self._weatherView.pack()
        
        cities = [ "Tokyo", "San Francisco" ]
        self._selectedCity = tk.StringVar()
        self._selectedCity.set(cities[0])
        self._citiesDropDown = tk.OptionMenu(self, self._selectedCity, *cities, command=self.cities_drop_down_selected_change)
        self._citiesDropDown.pack()
    
    def cities_drop_down_selected_change(self, value):
        print(f"Selectd is {value}")
        self._weatherView.update_weather_info(value)

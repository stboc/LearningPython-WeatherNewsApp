import WeatherNewsApp.View.MainView as mv
import WeatherNewsApp.Controller.MainController as mc
import WeatherNewsApp.Model.MainModel as mm

def main():
    model = mm.MainModel()
    controller = mc.MainController(model)
    view = mv.MainView(controller)
    view.mainloop()

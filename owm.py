import pyowm
owm = pyowm.OWM('71adf362bb14852c2f8ed5448d847297', language = "ru")

place = input("В каком городе/стране: ")

observation = owm.weather_at_place(place)
w = observation.get_weather()

temp=w.get_temperature('celsius')["temp"]

print("В городе "+ place+" сейчас " + w.get_detailed_status() +" и " + str(temp) +" градусов C")

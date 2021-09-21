import json
import tkinter as tk
from tkinter.constants import ANCHOR, CENTER, NW
import requests
import time

# Weather Api 
def getWeather(canvas):
    city = textfield.get()
    api = "http://api.openweathermap.org/data/2.5/weather?q=" + city + "&appid=894bcd2a64486e2282fa83569f402343"
    json_data = requests.get(api).json()
    condition = json_data['weather'][0]['main']
    temp = int(json_data['main']['temp']-273.15)
    min_temp = int(json_data['main']['temp_min']-273.15)
    max_temp = int(json_data['main']['temp_max']-273.15)
    pressure = json_data['main']['pressure']
    humidity = json_data['main']['humidity']
    wind = json_data['wind']['speed']
    
    final_info = condition + '\n' + str(temp) + "°C"
    final_data = "\n" + "Max Temp: " + str(max_temp) + " °C\n" + "Min Temp: " + str(min_temp) + " °C\n" + "Pressure: " + str(pressure) + " mb\n" + "Humidity: " + str(humidity) + " %\n" + "Wind Speed: " + str(wind)+" km/h"

    label1.config(text = final_info)
    label2.config(text = final_data)




canvas = tk.Tk()
canvas.geometry("600x400")
canvas.title("Weather App")
canvas.config(bg='cyan')
f = ("arial", 15,"bold")
t = ("poppins",35,"bold")

textfield = tk.Entry(canvas,font=t,bg='powderblue',border=1,justify=CENTER)
textfield.pack(pady=50)
textfield.focus()
textfield.bind("<Return>",getWeather)

label1=tk.Label(canvas,font = f,bg='cyan')

label1.pack()

label2 = tk.Label(canvas,font=f,bg='cyan')
label2.pack()

canvas.mainloop()


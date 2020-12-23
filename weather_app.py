import requests
from bs4 import BeautifulSoup
from tkinter import Label
from tkinter import Tk
from PIL import ImageTk, Image

url = "https://weather.com/pt-BR/clima/hoje/l/51da9a165cab1e511ca9ff049057ad34a2ce06898990e33c5ed2c4bdd5a76bc5"
master = Tk()
master.title("Weather App")
master.config(bg = "white")

img = Image.open("C:/Users/NE57006b/Desktop/py4e/weather_app/image.png")
img = img .resize((300, 300))
img = ImageTk.PhotoImage(img)

def getWeather():
    page = requests.get(url)
    soup = BeautifulSoup(page.content, "html.parser")
    location = soup.find('h1', class_="CurrentConditions--location--1Ayv3").text
    temperature = soup.find('span', class_="CurrentConditions--tempValue--3KcTQ").text
    weatherPrediction = soup.find('div', class_="CurrentConditions--phraseValue--2xXSr").text
    weatherDetail1 = soup.find('div', class_ ="ListItem--listItem--1r7mf WeatherDetailsListItem--WeatherDetailsListItem--3w7Gx").text
    weatherDetail2 = soup.find('div', class_ ="TodayDetailsCard--feelsLikeTemp--2GFqN").text
    weatherDetail3 = soup.find('div', class_ ="CurrentConditions--precipValue--RBVJT").text

    locationLabel.config(text=location)
    temperatureLabel.config(text=temperature)
    weatherPredictionLabel.config(text=weatherPrediction)
    weatherDetail1Label.config(text=weatherDetail1)
    weatherDetail2Label.config(text=weatherDetail2)
    weatherDetail3Label.config(text=weatherDetail3)

    temperatureLabel.after(60000, getWeather)
    weatherDetail2Label.after(60000, getWeather)
    weatherDetail3Label.after(60000, getWeather)
    master.update()

locationLabel = Label(master, font= ("Verdana",22), bg="white")
locationLabel.grid(row=0, stick="N", padx=110)
temperatureLabel = Label(master, font= ("Verdana bold",80), bg="white")
temperatureLabel.grid(row=1, stick="W", padx=50)
Label(master, image = img, bg="white").grid(row=1, sticky="E")
weatherPredictionLabel = Label(master, font=("Verdana",15), bg="white")
weatherPredictionLabel.grid(row=2, stick="W", padx=30)
weatherDetail1Label = Label(master, font=("Verdana",15), bg="white")
weatherDetail1Label.grid(row=1, stick="WS", padx=30)
weatherDetail2Label = Label(master, font=("Verdana",15), bg="white")
weatherDetail2Label.grid(row=3, stick="WS", padx=30)
weatherDetail3Label = Label(master, font=("Verdana",15), bg="white")
weatherDetail3Label.grid(row=4, stick="WS", padx=30)

getWeather()
master.mainloop()
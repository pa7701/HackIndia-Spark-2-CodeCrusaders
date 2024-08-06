from tkinter import *
from tkinter import ttk
import requests
from datetime import datetime

def data_get():
    city = city_name.get()
    api_key = "7cb507869db01af80a0841597f118513"  # Replace with your actual API key
    url = f"http://api.openweathermap.org/data/2.5/forecast?q={city}&appid={api_key}"
    
    try:
        response = requests.get(url)
        response.raise_for_status()  # Check if the request was successful
        data = response.json()
        
        # Process the forecast data
        forecast_data = data["list"]
        for i in range(5):
            forecast = forecast_data[i * 8]  # Get one data point per day
            dt = datetime.fromtimestamp(forecast["dt"])
            weather = forecast["weather"][0]
            main = forecast["main"]
            
            # Update labels
            labels[i][0].config(text=weather["main"])
            labels[i][1].config(text=weather["description"])
            labels[i][2].config(text=f"{int(main['temp'] - 273.15)}°C")  # Convert from Kelvin to Celsius
            labels[i][3].config(text=f"{main['pressure']} hPa")
            dates[i].config(text=dt.strftime("%Y-%m-%d"))

    except requests.exceptions.RequestException as e:
        for i in range(5):
            labels[i][0].config(text="Error")
            labels[i][1].config(text=str(e))
            labels[i][2].config(text="N/A")
            labels[i][3].config(text="N/A")
            dates[i].config(text="N/A")

win = Tk()
win.title("4-Day Weather Forecast")
win.config(bg="cyan")
win.geometry("1200x800")

name_label = Label(win, text="4-Day Weather Forecast", font=("Times New Roman", 30, "bold"))
name_label.place(x=25, y=50, height=50, width=450)

city_name = StringVar()
list_name = ["Andhra Pradesh", "Arunachal Pradesh", "Assam", "Bihar", "Chhattisgarh", "Goa", "Gujarat", 
             "Haryana", "Himachal Pradesh", "Jammu and Kashmir", "Jharkhand", "Karnataka", "Kerala", 
             "Madhya Pradesh", "Maharashtra", "Manipur", "Meghalaya", "Mizoram", "Nagaland", "Odisha", 
             "Punjab", "Rajasthan", "Sikkim", "Tamil Nadu", "Telangana", "Tripura", "Uttar Pradesh", 
             "Uttarakhand", "West Bengal", "Andaman and Nicobar Islands", "Chandigarh", 
             "Dadra and Nagar Haveli", "Daman and Diu", "Lakshadweep", "National Capital Territory of Delhi", 
             "Puducherry"]
com = ttk.Combobox(win, values=list_name, font=("Times New Roman", 20, "bold"), textvariable=city_name)
com.place(x=25, y=120, height=50, width=450)

# Create labels for displaying forecast data
dates = []
weather_labels = []
description_labels = []
temp_labels = []
pressure_labels = []

for i in range(5):
    y_offset = 200 + i * 100
    date_label = Label(win, text="", font=("Times New Roman", 15, "bold"))
    date_label.place(x=25, y=y_offset, height=50, width=100)
    dates.append(date_label)
    
    weather_label = Label(win, text="", font=("Times New Roman", 15, "bold"))
    weather_label.place(x=150, y=y_offset, height=50, width=150)
    weather_labels.append(weather_label)
    
    description_label = Label(win, text="", font=("Times New Roman", 15))
    description_label.place(x=310, y=y_offset, height=50, width=200)
    description_labels.append(description_label)
    
    temp_label = Label(win, text="", font=("Times New Roman", 15))
    temp_label.place(x=520, y=y_offset, height=50, width=100)
    temp_labels.append(temp_label)
    
    pressure_label = Label(win, text="", font=("Times New Roman", 15))
    pressure_label.place(x=630, y=y_offset, height=50, width=100)
    pressure_labels.append(pressure_label)

labels = [weather_labels, description_labels, temp_labels, pressure_labels]

done_button = Button(win, text="Get Forecast", font=("Times New Roman", 20), command=data_get)
done_button.place(y=700, height=40, width=150, x=150)

win.mainloop()

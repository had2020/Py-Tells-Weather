# Import modules
from tkinter import *
import tkinter as tk
from geopy.geocoders import Nominatim
from tkinter import ttk,messagebox
from timezonefinder import TimezoneFinder
from datetime import datetime
import requests
import pytz


# Define constants
API_KEY = "your_api_key_here" # Replace with your own API key
WEATHER_API_URL = "http://api.weatherapi.com/v1/marine.json?key=" + API_KEY # Replace with your own weather API URL

# Create a root window
root = tk.Tk()  # This creates a root window object
root.title("Weather App")  # This sets the title of the window
root.geometry("400x300")  # This sets the size of the window
root.resizable(False, False)  # This prevents the window from being resized

# Define global variables
city_name = ""  # The city name entered by user
city_list = []  # The list of available cities
city_var = tk.StringVar()  # The variable that stores the selected city name
text_value = tk.StringVar()  # The variable that stores the text value for the text widget


# Define functions

def get_city_list():
    # This function returns a list of available cities based on their names
    global city_list
    response = requests.get(WEATHER_API_URL + "&q=auto:ip") # Add the parameter q and use auto:ip as the value
    data = response.json()
    if "status" in data and data["status"] == "OK": # Check if status key exists and is equal to "OK"
        cities = data["data"]["cities"]
        city_list.clear()
        for city in cities:
            city_list.append(city["name"])
    else:
        print("Error:", data.get("error", {}).get("message", "Unknown")) # Print the error message or "Unknown" if not found


def get_city():
    # This function gets and displays the weather data for a given city name
    global city_name
    if city_name != "":  # Check if the city name is not empty
        response = requests.get(WEATHER_API_URL + "&q=" + city_name)
        data = response.json()
        if "status" in data and data["status"] == "OK":  # Check if status key exists and is equal to "OK"
            temp_celsius = int(data["data"]["main"]["temp"] - 273)  # Convert temperature from Kelvin to Celsius
            temp_fahrenheit = (temp_celsius * 9 / 5) + 32  # Convert temperature from Celsius to Fahrenheit
            humidity_percent = int(
                data["data"]["main"]["humidity"]) * 100  # Convert humidity from percentage scale to integer scale
            wind_speed_miles_per_hour = int(data["data"]["wind"][
                                                "speed"] * 2.237)  # Convert wind speed from kilometers per hour scale to miles per hour scale
            description = data["data"]["weather"][0]["description"]  # Get description of current weather condition

            text_value.set(
                f"City: {city_name}\nTemperature (Celsius): {temp_celsius}°\nTemperature (Fahrenheit): {temp_fahrenheit}°\nHumidity (%): {humidity_percent}%\nWind Speed (mph): {wind_speed_miles_per_hour} mph\nDescription: {description}")  # Format text value with new information

        else:
            print("Error:",
                  data.get("error", {}).get("message", "Unknown"))  # Print the error message or "Unknown" if not found
    else:
        print("Please enter a valid city name")  # Print a message asking the user to enter a valid city name


def update_city():
    # This function updates the selected city name based on user input or selection

    global city_name

    if len(city_list) > 0:
        index = city_listbox.curselection()  # Get the index of the selected item in the listbox
        if index:  # If the index is not empty
            city_name = city_list[index[0]]  # Get the city name from the list
        else:  # If the index is empty
            city_name = city_entry.get()  # Get the city name from the entry
        city_var.set(city_name)  # Update the city_var with the new city name
        get_city()  # Call the get_city function to display the weather data
    else:
        print("Please wait for the city list to load")


# Create widgets and buttons

# Create a label for the title
title_label = tk.Label(root, text="Weather App", font=("Arial", 20, "bold"))
title_label.pack(pady=10)

# Create a frame for the city input and selection
city_frame = tk.Frame(root)
city_frame.pack()

# Create a label for the city entry
city_label = tk.Label(city_frame, text="Enter a city name:")
city_label.grid(row=0, column=0, padx=5, pady=5)

# Create an entry for the city name
city_entry = tk.Entry(city_frame, textvariable=city_var)
city_entry.grid(row=0, column=1, padx=5, pady=5)

# Create a button to update the city name
city_button = tk.Button(city_frame, text="Update", command=update_city)
city_button.grid(row=0, column=2, padx=5, pady=5)

# Create a label for the city listbox
city_list_label = tk.Label(city_frame, text="Or select from the list:")
city_list_label.grid(row=1, column=0, padx=5, pady=5)

# Create a listbox for the city list
city_listbox = tk.Listbox(city_frame, height=5, width=20)
city_listbox.grid(row=1, column=1, padx=5, pady=5)

# Create a scrollbar for the listbox
city_scrollbar = tk.Scrollbar(city_frame, orient="vertical")
city_scrollbar.grid(row=1, column=2, sticky="ns")
city_listbox.config(yscrollcommand=city_scrollbar.set)  # Link the scrollbar with the listbox
city_scrollbar.config(command=city_listbox.yview)  # Link the listbox with the scrollbar

# Create a label for the weather data
weather_label = tk.Label(root, height=10, width=40, font=("Courier", 14, "bold"))
weather_label.pack(pady=10)
weather_label.config(state="disabled") # Disable editing of the label
weather_label.config(textvariable=text_value) # Link the label with the text_value variable

# Call the get_city_list function to populate the listbox
get_city_list()
for city in city_list:
    city_listbox.insert("end", city)  # Insert each city name into the listbox

# Start the main loop
root.mainloop()

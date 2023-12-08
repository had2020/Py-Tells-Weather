# Py-Tells-Weather
A python tkinter weather app that checks the api of api.weatherapi.com for the weather 

By: Hadrian Lazic Date: 12/7/23

<img width="499" alt="Screenshot 2023-12-07 at 8 14 31 PM" src="https://github.com/had2020/Py-Tells-Weather/assets/59424667/cb086b82-a60c-4cd8-9482-71ad0063292e">


# steps my code takes 
1. The user interacts with the Python program by choosing a city from a list or typing in their desired location. This input is then sent to the API provided by `weatherapi.com`.

2. To send this request, the Python program uses an HTTP library like `requests` to make a GET request to the weather API's endpoint. The URL for this request would be something like: https://www.weatherapi.com/forecast.json?key=YOUR_API_KEY&q=New York
   - Here, "YOUR_API_KEY" is a unique identifier provided by `weatherapi.com` that allows the app to access their data, and "New York" is the city name specified by the user.

3. The API receives this request and processes it using its own data sources to gather information about the weather conditions for that specific location. It returns a response containing details such as temperature, humidity, wind speed, etc.

4. This response is then received by the Python program, which parses and interprets the data provided by the API. The app can now display this information to the user in an easy-to-understand format.

5. If the user wants to check weather for another city or location, they simply repeat steps 1 through 4 with their new input. This process continues until the user is satisfied with the information provided by the simple weather app.

6. In addition to displaying current and forecasted weather conditions, some apps may also offer additional features like severe weather alerts, local news updates related to climate events, or even personalized recommendations for activities based on current conditions. These extra functionalities would require additional code that interacts with other APIs or databases as needed.

Overall, the purpose of a simple weather app is to provide users with real-time and forecasted information about their desired location's climate patterns in an easy-to-understand format. The code functions by sending requests to trusted API sources like `weatherapi.com`, parsing and interpreting the data received, and displaying it accordingly for user consumption.

--------------------------

# how to run the app or edit the app
python requirements 

-tkinter
-requests

--------------------------

# about weather apps
A weather app serves the purpose of providing users with real-time and forecasted information about the current and future weather conditions in their desired location. This can be useful for various reasons, such as planning outdoor activities, dressing appropriately for the day's weather, or even just being aware of potential changes in climate patterns.

Weather apps typically use APIs from trusted sources like `weatherapi.com` to gather data about temperature, humidity, wind speed, precipitation, and other relevant factors. This information is then processed by the app itself, which can display it in a user-friendly format such as graphs or charts.

In addition to providing weather forecasts, some apps may also offer additional features like severe weather alerts, local news updates related to climate events, or even personalized recommendations for activities based on current conditions. Overall, the purpose of a weather app is to help users stay informed and prepared when it comes to their environment's ever-changing weather patterns.

--------------------------

Documentation 
-https://www.weatherapi.com/docs/
-https://docs.python.org/3/library/tkinter.html
-https://requests.readthedocs.io/en/latest/ 

--------------------------

Have a Wonderful day! :D

# WeatherText

WeatherText allows you to get the weather on any location around the world, by texting your Twilio number the zipcode of the location when the script inbound.py is running. 

# Usage

1. To use WeatherText, first make an Accuweather developer count and create a new app. You will then get an app key that you can set the variable ` accu_key` equal to your app key.

2. Run inbound.py in your python console by typing in `python inbound.py` in the terminal.

3. Set up ngrok by running `./ngrok http 5000` in a separate terminal window.

4. Go to your Twilio Developer Console and then to your active numbers and replace the `A MESSAGE COMES IN:` field with your ngrok link.

5. Text your Twilio number your zipcode and you'll get the weather back!

from flask import Flask, request
import json
from twilio.twiml.messaging_response import MessagingResponse
import requests


accu_key = "HIDDEN" 

app = Flask(__name__)
@app.route('/sms', methods=['POST', 'GET'])

def weather():
	
	message_body = request.form['Body']
	url = 'http://dataservice.accuweather.com/forecasts/v1/daily/1day/{}?apikey=%091{}&language=en-us&details=false&metric=false'.format(message_body, accu_key)

	d = requests.get(url = url)

	data = d.json()

	minimum = data['DailyForecasts'][0]['Temperature']['Minimum']['Value']
	maximum = data['DailyForecasts'][0]['Temperature']['Maximum']['Value']
	day = data['DailyForecasts'][0]['Day']['IconPhrase']
	night = data['DailyForecasts'][0]['Night']['IconPhrase']

	
	resp = MessagingResponse()
	resp.message("Here's the weather for {}, with all tempartures in Fahrenheit: \n Minimum:{} \n Maximum:{} \n Day:{} \n Night:{}".format(message_body, minimum, maximum, day, night))
	return str(resp)

if __name__=="__main__":
	app.run(debug=True)
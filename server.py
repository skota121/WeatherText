from flask import Flask, request, redirect
from twilio.twiml.messaging_response import MessagingResponse

app = Flask(__name__)

@app.route("/", methods = ['GET', 'POST'])

def weather():
	# Get weather from Accuweather API 
	resp = MessagingResponse().message()
	return str(resp)
if __name__ = "__main__":
	app.run(debug=True)
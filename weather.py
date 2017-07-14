from twilio.rest import Client
from flask import Flask, request, redirect
from twilio.twiml.messaging_response import MessagingResponse
import requests
import json

account_sid = "XXXXXXXXX"
auth_token = "XXXXXXXX"
accu_key = "XXXXXXX" 
app = Flask(__name__)
@app.route("/", methods = ['GET', 'POST'])



def weather():
	# Get weather from Accuweather API 
	resp = MessagingResponse().message()
	return str(resp)
client = Client(account_sid, auth_token)
message = client.api.account.messages.create(to = "+XXXXXXX", from_="+XXXXX", body="")

if __name__ = "__main__":
	app.run(debug=True)
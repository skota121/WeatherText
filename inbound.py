from flask import Flask, request
import json
from twilio import twiml

account_sid = "XXXXXXXXX"
auth_token = "XXXXXXXX"
accu_key = "XXXXXXX" 

app = Flask(__name__)
@app.route('/sms', methods=['POST', 'GET'])



def sms():
	message_body = request.form['Body']
	resp = twiml.Response()

	resp.message('')

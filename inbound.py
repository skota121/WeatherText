from flask import Flask, request
import json
from twilio import twiml

app = Flask(__name__)
@app.route('/sms', methods=['POST', 'GET'])

def sms():
	message_body = request.form['Body']
	resp = twiml.Response()

	resp.message('')

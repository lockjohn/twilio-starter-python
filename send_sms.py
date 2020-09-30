from twilio.rest import Client
import os

# get env var
TWILIO_ACCOUNT_SID = os.environ.get('TWILIO_ACCOUNT_SID')
TWILIO_AUTH_TOKEN = os.environ.get('TWILIO_AUTH_TOKEN')
TWILIO_PHONE_NUMBER = os.environ.get('TWILIO_PHONE_NUMBER')


# Your Account SID from twilio.com/console
account_sid = TWILIO_ACCOUNT_SID
# Your Auth Token from twilio.com/console
auth_token  = TWILIO_AUTH_TOKEN

client = Client(account_sid, auth_token)

message = client.messages.create(
    to="+19724395426", 
    from_=TWILIO_PHONE_NUMBER,
    body="Hello from Python!")

print(message.sid)
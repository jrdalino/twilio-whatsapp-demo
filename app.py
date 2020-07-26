# Download the helper library from https://www.twilio.com/docs/python/install
from twilio.rest import Client


# Your Account Sid and Auth Token from twilio.com/console
# DANGER! This is insecure. See http://twil.io/secure
account_sid = '<REPLACE_ME>'
auth_token = '<REPLACE_ME>'
client = Client(account_sid, auth_token)

message = client.messages.create(
                              body='Your Owl Taxi with plate number SBA-123 will arrive at 3:30 PM!',
                              from_='whatsapp:+14155238886',
                              to='whatsapp:<+REPLACE_ME>'
                          )

print(message.sid)
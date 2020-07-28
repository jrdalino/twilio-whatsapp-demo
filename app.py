from twilio.rest import Client
from config import ACCOUNT_SID, AUTH_TOKEN


account_sid = ACCOUNT_SID
auth_token = AUTH_TOKEN
client = Client(account_sid, auth_token)

message = client.messages.create(
                              body='Your Owl Taxi with plate number SBA-123 will arrive at 7:30 PM!',
                              from_='whatsapp:+14155238886',
                              to='whatsapp:+6591730420'
                          )

print(message.sid)
# Twilio WhatsApp Demo

## Quickstart
- Sign up for Twilio and activate the Sandbox. Note Account SID and Auth Token

- Set up your development environment to send and receive messages
```
python3 -m venv venv
source venv/bin/activate
```

- create requirements.txt
```
twilio
```

- installs dependencies
```
pip install -r requirements.txt
```

- Opt-in to the Sandbox by using Whats app to send this 
```
Send "join light-division" to +14155238886
```

- Create app.py which will send a message with WhatsApp
```
# Download the helper library from https://www.twilio.com/docs/python/install
from twilio.rest import Client


# Your Account Sid and Auth Token from twilio.com/console
# DANGER! This is insecure. See http://twil.io/secure
account_sid = 'your_account_sid'
auth_token = 'your_auth_token'
client = Client(account_sid, auth_token)

message = client.messages.create(
                              body='Hello there!',
                              from_='whatsapp:+14155238886',
                              to='whatsapp:<+REPLACE_ME>'
                          )

print(message.sid)
```

- Run your application
```
$ cd ~/environment/twilio-whatsapp-demo
$ python3 app.py
```

## References
- https://www.twilio.com/docs/whatsapp/quickstart/python
# Twilio WhatsApp Demo

## Requirements
- a Twilio account – sign up for free
- Python 2.x or 3.x
- the Twilio Python helper library

## Environment and project setup
- Sign up for Twilio and activate the Sandbox. Note Account SID and Auth Token

- Opt-in to the Sandbox by using Whats app to send this 
```
Send "join light-division" to +14155238886
```

- Install and activate virtualenv
```
$ python3 -m venv venv
$ source venv/bin/activate
```

- Create requirements.txt
```
twilio
```

- Installs dependencies
```
$ pip install -r requirements.txt
```

## App
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
$ source venv/bin/activate
$ python3 app.py
```

## References
- https://www.twilio.com/docs/whatsapp/quickstart/python